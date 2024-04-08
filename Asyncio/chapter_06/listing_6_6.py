import time
from collections import defaultdict

def main():
    time_start = time.time()

    words_counter = defaultdict(int)
    with open('./chapter_06/googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as fin:      
        for line in fin:
            word, year, word_count, books_count = line.split('\t')
            word_count, books_count = [int(x) for x in [word_count, books_count]]
            
            words_counter[word] += word_count
            
    time_end = time.time()
    return words_counter, time_end-time_start


if __name__ == '__main__':    
    counter, res_time = main()
    print(f"Aardvark встречается {counter['Aardvark']} раз.")
    print(f'Подсчет занял: {res_time:.4f} с')