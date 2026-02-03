def main():
    fullWord = input("Please enter a full word to convert to snake case: ")
    snakeWord = ""

    for char in fullWord:
        if char.isupper():
            snakeWord += "_" + char.lower()
        else:
            snakeWord += char

    print(snakeWord)

main()