import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args()

    with open(args.filename) as lines:
        for number, line in enumerate(lines, start=1):
            line = line.rstrip("\n")

            if args.ignore_case:
                if args.pattern.lower() in line.lower():
                    print(f"{number}: {line}")
            else:
                if args.pattern in line:
                    print(f"{number}: {line}")


if __name__ == "__main__":
    main()