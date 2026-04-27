from services.gambler_service import *
from services.stake_service import *
from services.betting_service import place_bet
from services.session_service import *
from services.stats_service import get_stats
from database.create_table import create_table

create_table()

while True:
    print("\nMenu")
    print("1 Create Gambler")
    print("2 View Gambler")
    print("3 Update Gambler")
    print("4 Validate Gambler")
    print("5 Reset Gambler")
    print("6 Deposit")
    print("7 Withdraw")
    print("8 Place Bet")
    print("9 Stake Report")
    print("10 Start Session")
    print("11 End Session")
    print("12 Stats")
    print("13 Exit")

    c = input()

    if c == "1": create_gambler()
    elif c == "2": view_gambler()
    elif c == "3": update_gambler()
    elif c == "4": validate_gambler()
    elif c == "5": reset_gambler()
    elif c == "6": deposit()
    elif c == "7": withdraw()
    elif c == "8": place_bet()
    elif c == "9": stake_report()
    elif c == "10": start_session(int(input("ID: ")))
    elif c == "11": end_session(int(input("ID: ")))
    elif c == "12": get_stats(int(input("ID: ")))         
    elif c == "13": break