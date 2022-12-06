values = {
    "scissors" : 1,
    "paper" : 2,
    "rock" : 3
    }

my

def main():
    with open("input.txt", "r") as f:
        for line in f.readLines():
            opponentChoice = line[0]
            myChoice = line[2]
            print(opponentChoice)
            print(myChoice)

if __name__ == "__main__":
    main()
