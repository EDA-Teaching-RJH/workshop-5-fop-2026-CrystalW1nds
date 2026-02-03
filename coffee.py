def main():
    balance = 0

    while balance < 75:
        coin = int(input("Insert 75p: (50p, 20p, 10p, 5p)"))

        if coin == 50 or coin == 20 or coin == 10 or coin == 5:
            balance = balance + coin
        
        else:
            print("Invalid coin, refunding... ")

        print("Balance: ", balance)

    change = balance - 75

    print("Change: ", change)
    print("Dispensing change... ")

    print("Preparing coffee...")


main()