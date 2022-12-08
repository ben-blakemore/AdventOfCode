def main():
    total = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            a, b = line.split(",")
            first_a = a.split("-", 1)[0]
            first_b = b.split("-", 1)[0]
            last_a = a.split("-", 1)[1]
            last_b = b.split("-", 1)[1]
            if ((first_a >= first_b and last_a <= last_b) or (first_b >= first_a and last_b <= last_a)):
                total += 1
        print(total)

if __name__ == "__main__":
    main()
