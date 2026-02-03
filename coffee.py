# Statement of Requirements:
# Program will only accept 50, 20, 10, or 5 as inputs
# Program will output the balance each time a coin is added
# Change is calculated by subtracting 75 from the full balance to find the remainder
# Amount due is calculated by subtracting the balance from 75
# The system should crash if a string is entered to the coin variable (fixed now)

def getCoin():
    coin = input("Insert 75p: (50p, 20p, 10p, 5p) ")

    if coin == "50" or coin == "20" or coin == "10" or coin == "5":
        coin = int(coin)
    else:
        print("Invalid")
        coin = 0

    return coin

def updateTotal(due, coin):
    total = due - coin
    print("Due: ", total)
    return total

def dispenseProduct(due):
    change = 0 - due
    print("Change: ", change)
    print("Dispensing coffee...")
    print("Have a nice day! ")

def main():
    due = 75

    while due > 0:
        coin = getCoin()
        due = updateTotal(due, coin)

    dispenseProduct(due)
        


main()