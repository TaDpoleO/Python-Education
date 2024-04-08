class LineFragmentInit(Exception):
    pass

class TextElement():
    def get_height(self):
        raise NotImplementedError

    def get_width(self):
        raise NotImplementedError

class Word(TextElement):
    def __init__(self, text, letter_height, letter_width) -> None:
        self.text = text        
        self.height = letter_height
        self.width = letter_width*len(text)

    def __str__(self) -> str:
        return f"[WORD: '{self.text}']"
    
    def get_height(self):
        return self.height    

    def get_width(self):
        return self.width
           
class Image(TextElement):
    def __init__(self, id, params) -> None:
        self.id = id
        self.params = self.parse_image(params)

    def __str__(self) -> str:
        return f'[IMAGE: id={self.id}, params={self.params}]'

    def parse_image(self, image):
        def parse_param(param):
            buffer = param.split('=')

            if len(buffer) != 2:
                return None, None
            else:
                return param.split('=')
        
        params = dict()

        buffer = image.split()
        for param in buffer:
            key, val = parse_param(param)
            params[key] = val

        if None in params: del params[None]

        return params
    
    def get_id(self):
        return self.id
    
    def get_image_param(self, param):
        return self.params.get(param, None)
    
    def get_width(self):
        return int(self.get_image_param('width'))
        
    def get_height(self):
        return int(self.get_image_param('height'))
    
    def get_layout(self):
        return self.get_image_param('layout')

class LineFragment():
    IMAGE_LAYOUT_EMBEDDED = 'embedded'
    IMAGE_LAYOUT_SURROUNDED = 'surrounded'
    IMAGE_LAYOUT_FLOATING = 'floating'

    def __init__(self, position, width, space_width, elements: list[TextElement]=None) -> None:
        self.position = position
        self.width = width
        self.space_width = space_width

        self.cur_dx = 0

        if elements is None:
            self.elements = []
        else:
            cur_element = 0
            while (cur_element < len(elements)) and (self.add_element(elements[cur_element])):
                cur_element += 1

            if len(self.elements) != len(elements):
                raise LineFragmentInit('fragment width is too small to add all elements')

    def __str__(self) -> str:
        return f'[FRAGMENT: pos={self.position}, width={self.width}, elements={[str(x) for x in self.elements]}]'

    def get_position(self):
        return self.position
   
    def get_width(self):
        return self.width
        
    def isAddable(self, element: TextElement):
        element_type = type(element)

        if (element_type is Word) or ((element_type is Image) and ((layout := Image.get_layout(element)) == self.IMAGE_LAYOUT_EMBEDDED)):           
            if self.cur_dx == 0:
                x_pos = self.cur_dx
            else:
                x_pos = self.cur_dx+self.space_width
            width = element.get_width()

            if self.get_width()-x_pos >= width:
                return self.get_position()+x_pos

        elif element_type is Image:          
            if layout == self.IMAGE_LAYOUT_SURROUNDED:
                x_pos = self.cur_dx
                width = element.get_width()

                if self.get_width()-x_pos >= width:
                    return self.get_position()+x_pos
    
    def add_element(self, element: TextElement):      
        if (x0 := self.isAddable(element)) is not None:
            self.elements.append(element)
            # if self.cur_dx > 0: self.cur_dx += self.space_width
            self.cur_dx = x0-self.get_position()+element.get_width()

            return x0
        
    def split_fragment(self, split_width):
        if self.cur_dx == 0:
            if split_width >= self.get_width():
                return None, None
            else:
                return None, LineFragment(self.get_position()+split_width, self.get_width()-split_width, self.space_width)
        else:
            if split_width >= self.get_width()-self.cur_dx:
                self.width = self.cur_dx
                return self, None
            else:                
                old_width = self.get_width()
                self.width = self.cur_dx
                return self, LineFragment(self.get_position()+split_width+self.cur_dx, old_width-split_width-self.cur_dx, self.space_width)

class PageLine():
    IMAGE_LAYOUT_EMBEDDED = 'embedded'
    IMAGE_LAYOUT_SURROUNDED = 'surrounded'
    IMAGE_LAYOUT_FLOATING = 'floating'

    def __init__(self, x_position, y_position, width, height, fragments: list[LineFragment]=None) -> None:
        self.x_pos = x_position
        self.y_pos = y_position
        self.height = height
        self.width = width

        if fragments is None:
            self.fragments = []
            self.cur_fragment = None
        else:
            self.fragments = fragments
            self.cur_fragment = 0

    def __str__(self) -> str:
        return f'LINE: ({self.x_pos}, {self.y_pos}), height={self.height}, width={self.width}, fragments={[str(x) for x in self.fragments]}'

    def get_x_position(self):
        return self.x_pos
    
    def get_y_position(self):
        return self.y_pos 

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def add_fragment(self, fragment: LineFragment):
        if len(self.fragments) == 0:
            if fragment.get_position()+fragment.get_width()-1 < self.get_width():
                self.fragments.append(fragment)
                return True
            else:
                return False
        else:
            if (fragment.get_position() > self.fragments[-1].get_position()+self.fragments[-1].get_width()-1) and \
                    (fragment.get_position()+fragment.get_width()-1 < self.get_width()):
                self.fragments.append(fragment)
                return True                
            else:
                return False
            
    def get_cur_fragment(self):
        return self.cur_fragment
    
    def set_cur_fragment(self, index):
        N = len(self.fragments)

        if (index >= 0) and (index < N):
            self.cur_fragment = index
            return True
        else:
            return False
               
    def add_element(self, element: TextElement):
        element_type = type(element)

        if (element_type is Word) or ((element_type is Image) and ((layout := Image.get_layout(element)) == self.IMAGE_LAYOUT_EMBEDDED)):
            N = len(self.fragments)
            
            while (self.cur_fragment < N) and ((x0 := LineFragment.add_element(self.fragments[self.cur_fragment], element)) is None):
                self.cur_fragment += 1

            if self.cur_fragment != N:
                self.height = max(self.height, element.get_height())
                return x0, self.get_y_position()
            
        elif element_type is Image:
            if layout == self.IMAGE_LAYOUT_SURROUNDED:
                N = len(self.fragments)
                               
                while (self.cur_fragment < N) and ((x0 := LineFragment.isAddable(self.fragments[self.cur_fragment], element)) is None):
                    self.cur_fragment += 1

                if self.cur_fragment != N:
                    fst_frag, scn_frag = LineFragment.split_fragment(self.fragments[self.cur_fragment], element.get_width())

                    if (fst_frag is None) and (scn_frag is None):
                        self.fragments.remove(self.fragments[self.cur_fragment]) # !!! Change self.fragments from List to LinkedList !!! O(n**2) now
                    elif (fst_frag is not None) and (scn_frag is not None):
                        self.fragments = self.fragments[:self.cur_fragment]+[fst_frag, scn_frag]+self.fragments[self.cur_fragment+1:]
                        self.cur_fragment += 1
                    elif (fst_frag is not None):
                        self.fragments[self.cur_fragment] = fst_frag
                        self.cur_fragment += 1
                    else:
                        self.fragments[self.cur_fragment] = scn_frag

                    return x0, self.get_y_position()

class TextEditor():
    ELEM_WORD = 0
    ELEM_IMAGE = 1

    IMAGE_LAYOUT_EMBEDDED = 'embedded'
    IMAGE_LAYOUT_SURROUNDED = 'surrounded'
    IMAGE_LAYOUT_FLOATING = 'floating'

    def __init__(self, text, line_width, letter_height, letter_width) -> None:
        self.line_width = line_width
        self.default_letter_height = letter_height
        self.default_letter_width = letter_width
        self.images = {}

        self.paragraphs: list[list[TextElement]] = self.parse_paragraphs(text)        
        self.lines: list[PageLine] = self.split_paragraphs_to_lines()        

    def get_paragraphs(self):
        return [[str(y) for y in x] for x in self.paragraphs]
    
    def get_lines(self):
        return self.lines
       
    def get_image_pos_by_id(self, id):
        if id not in self.images: return None
        
        x, y, image = self.images[id]
        width = Image.get_width(image)
        height = Image.get_height(image)

        return x, y, width, height
    
    def get_image_coordinates(self):
        result = []
        for key in sorted(self.images.keys()):
            x, y, _ = self.images[key]

            result.append((x, y))

        return result

    def parse_paragraphs(self, text):
        if not text: return []

        paragraphs = [[]]
        for line in text:      
            if line != '\n':
                line = line.strip()
                paragraphs[-1].append(line)
            else:
                paragraphs[-1] = ' '.join(paragraphs[-1])
                paragraphs.append([])

        paragraphs[-1] = ' '.join(paragraphs[-1])

        image_id = 0
        for i in range(len(paragraphs)):
            paragraphs[i], image_id = self.parse_elements(paragraphs[i], image_id) 

        return paragraphs

    def parse_elements(self, paragraph, image_id):
        def isLetter(letter):
            return letter.isalpha() or letter.isdigit() or (letter in (".", ",", ":", ";", "!", "?", "-", "'"))
        
        paragraph = paragraph.strip()

        elements = []

        cur_elem = None
        for ch in paragraph:
            if cur_elem is None:
                buffer = []
                
                if isLetter(ch):
                    cur_elem = self.ELEM_WORD                    
                elif ch == '(':
                    cur_elem = self.ELEM_IMAGE
            
            if cur_elem == self.ELEM_WORD:
                if isLetter(ch):
                    buffer.append(ch)
                elif ch == ' ':
                    elements.append(Word(''.join(buffer), self.default_letter_height, self.default_letter_width))
                    cur_elem = None
            elif cur_elem == self.ELEM_IMAGE:
                if ch == ')':
                    elements.append(Image(image_id, ''.join(buffer)))
                    image_id += 1
                    cur_elem = None
                elif ch != '(':
                    buffer.append(ch)

        if cur_elem == self.ELEM_WORD:
                elements.append(Word(''.join(buffer), self.default_letter_height, self.default_letter_width))
        elif cur_elem == self.ELEM_IMAGE:
                pass

        return elements, image_id

    def split_paragraphs_to_lines(self):
        def get_busy_fragments(cur_x, cur_y, width, height):
            busy_fragments = []          
                        
            for fragment in self.images:                
                if Image.get_layout(self.images[fragment][2]) == self.IMAGE_LAYOUT_SURROUNDED:                    
                    image_pos = self.get_image_pos_by_id(fragment)                    

                    if image_pos:
                        x, y, width, height = image_pos
                        if (cur_y >= y) and (cur_y <= (y+height-1)):
                            busy_fragments.append((x, x+width-1))

            busy_fragments.sort()

            return busy_fragments

        def create_new_line():
            if len(editor_lines) == 0:
                cur_line = PageLine(0, 0, self.line_width, self.default_letter_height, [LineFragment(0, self.line_width, self.default_letter_width)])                
            else:
                cur_x = 0
                cur_y = editor_lines[-1].get_y_position()+editor_lines[-1].get_height()

                busy_fragments = get_busy_fragments(cur_x, cur_y, editor_lines[-1].get_width(), editor_lines[-1].get_height())
                
                if len(busy_fragments) == 0:
                    cur_line = PageLine(cur_x, cur_y, self.line_width, self.default_letter_height, [LineFragment(0, self.line_width, self.default_letter_width)])
                else:
                    cur_line = PageLine(cur_x, cur_y, self.line_width, self.default_letter_height)                   

                    for fragment in busy_fragments:
                        if (fragment[0]-cur_x) > 0:
                            cur_line.add_fragment(LineFragment(cur_x, fragment[0]-cur_x, self.default_letter_width))
                        cur_x = fragment[1]+1
                    
                    if (cur_line.get_width()-cur_x) > 0:
                        cur_line.add_fragment(LineFragment(cur_x, cur_line.get_width()-cur_x, self.default_letter_width))

                    cur_line.set_cur_fragment(0)
            
            editor_lines.append(cur_line)
            return cur_line
        
        def add_floating_image(element: Image, last_element: tuple[int, int, int, int]):
            # last_element = (None, None, 0, 0) or (x, y, width, height)
            image_width = element.get_width()
            image_dx = int(element.get_image_param('dx'))

            image_height = element.get_height()
            image_dy = int(element.get_image_param('dy'))

            if last_element[0] is None:                
                x0 = cur_line.get_x_position()+image_dx
                x1 = x0+image_width-1

                y0 = cur_line.get_y_position()+image_dy
                y1 = y0+image_height-1
            else:
                x_last = last_element[0]+last_element[2]
                y_last = last_element[1]

                x0 = x_last+image_dx
                x1 = x0+image_width-1

                y0 = y_last+image_dy
                y1 = y0+image_height-1

            if x0 < 0:
                delta = -x0
            elif x1 >= self.line_width:
                delta = self.line_width-x1-1
            else:
                delta = 0

            x0 += delta
            x1 += delta

            return x0, y0

        if not self.paragraphs: return []

        editor_lines: list[PageLine] = []
        
        for paragraph in self.paragraphs:           
            last_element = (None, None, 0, 0) # x, y, width, height

            cur_line = create_new_line()

            for element in paragraph:
                elem_type = type(element)

                if (elem_type is Word) or ((elem_type is Image) and ((layout := Image.get_layout(element)) in [self.IMAGE_LAYOUT_EMBEDDED, self.IMAGE_LAYOUT_SURROUNDED])):
                    while not (res := cur_line.add_element(element)):
                        cur_line = create_new_line()
                        
                    x0, y0 = res
                    if elem_type is Image: self.images[Image.get_id(element)] = (x0, y0, element)

                elif elem_type is Image:
                    if layout == self.IMAGE_LAYOUT_FLOATING:
                        x0, y0 = add_floating_image(element, last_element)
                        self.images[Image.get_id(element)] = (x0, y0, element)

                last_element = (x0, y0, element.get_width(), element.get_height())

        return editor_lines

def main():
    with open('input.txt') as fin:
        W, H, C = [int(x) for x in fin.readline().split()]
        text = fin.readlines()

        editor = TextEditor(text, W, H, C)

        coordinates = editor.get_image_coordinates()
        for coordinate in coordinates:
            print(*coordinate)


if __name__ == '__main__':
    main()