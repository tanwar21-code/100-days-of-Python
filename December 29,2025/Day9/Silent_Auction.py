import art

print("WELCOME TO THE SILENT AUCTION!\n")
print(art.logo[0])

def main_fucntion():
    auction_data = {}
    while True:
        user_name = input("What is your name:-\n")
        try:
            bid_price = int(input("What is your Bid:-\n"))
        except ValueError:
            print("Please enter a valid integer for the bid.")
            continue

        auction_data[user_name] = bid_price
        final_ask = input("Are there any other bidders? type yes or no \n").strip().lower()
        if final_ask == 'yes':
            print("\n" * 100)
            continue
        else:
            break

    if auction_data:
        winner = max(auction_data, key=auction_data.get)
        winning_bid = auction_data[winner]
        print(f'{winner} has the maximum bid of ${winning_bid}')
    else:
        print('No bids were placed.')

if __name__ == '__main__':
    main_fucntion()