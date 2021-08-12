
def parse_line(line):
    elem = line.split()
    return (int(elem[0]), elem[1])


def parse_snapshot():
    with open('testdata/libs.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        counts = list(map(parse_line, lines))
        print(counts)


def main():
    print("Hello World")
    parse_snapshot()


if __name__ == '__main__':
    main()
