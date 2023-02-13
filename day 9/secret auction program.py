print("Welcome to my secret auction")

bidders = True
highest = 0
winner = ""
all_bids = {}

while bidders:
    name = input("Enter name here: ")
    bid = int(input("How much are you bidding: $"))
    all_bids[name] = bid

    if bid > highest:
        highest = bid
        winner = name

        other = input(" Are there any other bidders, 'yes' or 'no': ")

        if other == "no":
            bidders = False

print(f"Total list of bids made where {all_bids}")
print(f"The winner is {winner} with a total of ${highest}")