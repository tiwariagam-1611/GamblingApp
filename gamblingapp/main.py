from services.gambler_service import *
from services.stake_service import *
from services.stats_service import get_stats
from services.betting_service import place_bet
from database.create_table import create_table

create_table()

while True:
    print("\nMenu")
    print("1 Create Gambler")
    print("2 View Gambler")
    print("3 View All Gamblers")
    print("4 Update Gambler")
    print("5 Validate Gambler")
    print("6 Reset Gambler")
    print("7 Deposit")
    print("8 Withdraw")
    print("9 Place Bet")
    print("10 View Transactions")
    print("11 View Stats")
    print("12 Exit")

    c = input("Choice: ")

    if c == "1":
        create_gambler()

    elif c == "2":
        view_gambler()

    elif c == "3":
        view_all_gamblers()

    elif c == "4":
        update_gambler()

    elif c == "5":
        validate_gambler()

    elif c == "6":
        reset_gambler()

    elif c == "7":
        deposit()

    elif c == "8":
        withdraw()

    elif c == "9":
        place_bet()

    elif c == "10":
        stake_report()

    elif c == "11":
        get_stats(int(input("Enter ID: ")))

    elif c == "12":
        break

    else:
        print("Invalid choice")