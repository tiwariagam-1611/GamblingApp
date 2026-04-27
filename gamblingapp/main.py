from services.gambler_service import *
from services.stake_service import *
from services.betting_service import place_bet, calculator
from services.session_service import *
from services.stats_service import get_stats
from services.ui_service import GameStatusDisplay, SessionSummary, InteractiveMenu
from database.create_table import create_table

create_table()

ui = InteractiveMenu()
status_display = GameStatusDisplay()
summary = SessionSummary()

current_gid = None

while True:
    ui.display_menu()
    c = ui.get_choice()

    if c == "1":
        create_gambler()

    elif c == "2":
        view_gambler()

    elif c == "3":
        update_gambler()

    elif c == "4":
        validate_gambler()

    elif c == "5":
        reset_gambler()

    elif c == "6":
        deposit()

    elif c == "7":
        withdraw()

    elif c == "8":
        place_bet()

    elif c == "9":
        gid = int(input("Enter ID: "))
        status_display.display_current_status(gid)

    elif c == "10":
        stake_report()

    elif c == "11":
        gid = int(input("Enter ID: "))
        current_gid = gid
        start_session(gid)

    elif c == "12":
        gid = int(input("Enter ID: "))
        end_session(gid)
        summary.display_summary(gid)

    elif c == "13":
        calculator.stats()

    elif c == "14":
        print("Exiting...")
        break

    else:
        print("Invalid choice")