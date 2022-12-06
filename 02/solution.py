values = {
    "scissors" : 1,
    "paper" : 2,
    "rock" : 3
    }

elf_map = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors"
}

my_map = {
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}

def main():
    with open("input.txt", "r") as f:
        score = 0
        for line in f.readlines():
            opponentChoiceRaw = line[0]
            myChoiceRaw = line[2]
            score += calculate_score(opponentChoiceRaw, myChoiceRaw)
        print(score)

def calculate_score(opp, mine):
    # oppChoiceScore = values[elf_map[opp]]
    myChoiceScore  = values[my_map[mine]]
    myChoice = my_map[mine]
    oppChoice = elf_map[opp]
    if (myChoice ==  "rock" and oppChoice == "scissors") or (myChoice == "paper" and oppChoice == "rock") or (myChoice == "scissors" and oppChoice == "paper"):
        return myChoiceScore + 6
    elif myChoice == oppChoice:
        return myChoiceScore + 3
    else:
        return myChoiceScore

if __name__ == "__main__":
    main()
