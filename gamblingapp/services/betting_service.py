import random
from config.db import get_connection
from services.stake_service import update_stake
from models.transaction import TransactionType


def choose_strategy():
    print("Choose Strategy")
    print("1 Easy (High win, low reward)")
    print("2 Medium (Balanced)")
    print("3 Hard (Low win, high reward)")

    choice = input("Enter choice: ")

    if choice == "1":
        return 0.7, 1
    elif choice == "2":
        return 0.5, 2
    elif choice == "3":
        return 0.3, 3
    else:
        print("Invalid choice, default Medium")
        return 0.5, 2


def place_bet():
    gid = int(input("Enter ID: "))
    amount = float(input("Bet amount: "))

    probability, multiplier = choose_strategy()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_stake FROM gambler WHERE id=%s", (gid,))
    data = cursor.fetchone()

    if not data:
        print("Not found")
        return

    current = data[0]

    if amount > current:
        print("Insufficient balance")
        return

    before = current

    if random.random() < probability:
        outcome = "win"
        win_amount = amount * multiplier
        after = update_stake(gid, win_amount, TransactionType.BET_WIN)
    else:
        outcome = "loss"
        after = update_stake(gid, -amount, TransactionType.BET_LOSS)

    cursor.execute("""
    INSERT INTO bets
    (gambler_id, amount, probability, outcome, stake_before, stake_after)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (gid, amount, probability, outcome, before, after))

    conn.commit()
    conn.close()

    print("Result:", outcome)