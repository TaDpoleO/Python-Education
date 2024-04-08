def main():
    with open('input.txt') as fin:
        map_set = set(fin.readline().split())
        words = fin.readline().split()

        result = []
        for word in words:
            found = False

            for i in range(1, len(word)):                
                if (w := word[:i]) in map_set:
                    result.append(w)
                    found = True
                    break
            
            if not found:
                result.append(word)

        print(' '.join(result))


if __name__ == '__main__':
    main()