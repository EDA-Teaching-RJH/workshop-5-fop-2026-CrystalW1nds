# Statement of Requirements:
# Program will only accept 50, 20, 10, or 5 as inputs
# Program will output the balance each time a coin is added
# Change is calculated by subtracting 75 from the full balance to find the remainder
# Amount due is calculated by subtracting the balance from 75
# The system should crash if a string is entered to the coin variable (fixed now)


def main():
    balance = 0

    while balance < 75:
        coin = input("Insert 75p: (50p, 20p, 10p, 5p)")

        if coin == "50" or coin == "20" or coin == "10" or coin == "5":
            coin = int(coin)
            balance = balance + coin
            due = 75 - balance
        
        else:
            print("Invalid coin, refunding... ")

        print("Amount due: ", due)
        print("Balance: ", balance)

    change = balance - 75

    print("Change: ", change)
    print("Dispensing change... ")

    print("Preparing coffee...")


main()