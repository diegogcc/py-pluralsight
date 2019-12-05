import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        print(line)             # Gives double space paragraph

        sys.stdout.write(line)  # Gives single space paragraph
    f.close()

if __name__ == '__main__':
    main(sys.argv[1])