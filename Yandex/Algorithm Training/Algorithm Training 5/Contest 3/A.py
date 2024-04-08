def main():
    with open('input.txt') as fin:
        N = int(fin.readline())

        fin.readline()
        result = set(fin.readline().split())

        for _ in range(N-1):
            fin.readline()
            curr_playlist = set(fin.readline().split())
            result = result & curr_playlist

        print(len(result))
        print(' '.join(sorted(result)))


if __name__ == '__main__':
    main()