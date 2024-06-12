import random


def main():
    balance = 100

    print("-----------------------")
    print("Welcome to Python Slots")
    print("-----------------------")
    print("Symbols: 🍒 🍉 🍋 🛎️ ⭐️")
    print("-----------------------")

    while balance > 0:
        print("Current Balance: $", balance)

        bet = input("Place Your Bet: ")

        if not bet.isdigit():
            print("Please Enter A Valid Number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds! Place A Lower Bet")
            continue

        if bet <= 0:
            print("Bet Must Be Greater Than Zero")

        balance -= bet

        row = spin_row()

        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print("You Won $", payout)
        else:
            print("You Lost This Round")

        balance += payout

        play_again = input("Do You Want To Play Again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("--------------------------------------------")
    print("Game Over! Your Final Balance Was $", balance)
    print("--------------------------------------------")


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🛎️", "⭐️"]
    result = []
    for i in range(3):
        result.append(random.choice(symbols))
    return result


def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🛎️":
            return bet * 10
        elif row[0] == "⭐️":
            return bet * 20
    return 0


if __name__ == "__main__":
    main()
