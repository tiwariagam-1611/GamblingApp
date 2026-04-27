from config.db import get_connection


class GameStatusDisplay:

    def display_current_status(self, gid):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT current_stake, total_bets, wins, losses
        FROM gambler WHERE id=%s
        """, (gid,))

        data = cursor.fetchone()
        conn.close()

        if not data:
            print("Gambler not found")
            return

        stake, bets, wins, losses = data

        print("\n--- CURRENT STATUS ---")
        print("Stake:", stake)
        print("Total Bets:", bets)
        print("Wins:", wins)
        print("Losses:", losses)
        print("----------------------")


class SessionSummary:

    def display_summary(self, gid):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT initial_stake, current_stake, total_bets, wins, losses
        FROM gambler WHERE id=%s
        """, (gid,))

        data = cursor.fetchone()
        conn.close()

        if not data:
            print("No data")
            return

        initial, current, bets, wins, losses = data

        profit = current - initial
        win_rate = (wins / bets * 100) if bets else 0

        print("\n=== SESSION SUMMARY ===")
        print("Initial Stake:", initial)
        print("Final Stake:", current)
        print("Profit/Loss:", profit)
        print("Total Bets:", bets)
        print("Wins:", wins)
        print("Losses:", losses)
        print("Win Rate:", win_rate)
        print("=======================")


class InteractiveMenu:

    def display_menu(self):
        print("\n===== MENU =====")
        print("1 Create Gambler")
        print("2 View Gambler")
        print("3 Update Gambler")
        print("4 Validate Gambler")
        print("5 Reset Gambler")
        print("6 Deposit")
        print("7 Withdraw")
        print("8 Place Bet")
        print("9 View Status")
        print("10 Stake Report")
        print("11 Start Session")
        print("12 End Session")
        print("13 Win/Loss Stats")
        print("14 Exit")

    def get_choice(self):
        return input("Enter choice: ")