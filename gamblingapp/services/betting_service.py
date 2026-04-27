import random
from config.db import get_connection
from services.stake_service import update_stake
from models.transaction import TransactionType
from models.strategy import get_strategy

def place_bet():
    gid = int(input("Enter ID: "))
    amount = float(input("Enter bet amount: "))

    print("1 Easy 2 Medium 3 Hard")
    strategy = get_strategy(input("Choose strategy: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_stake FROM gambler WHERE id=%s", (gid,))
    current = cursor.fetchone()[0]

    if amount > current:
        print("Insufficient balance")
        return

    before = current

    if random.random() < strategy.probability:
        outcome = "win"
        win_amount = amount * strategy.multiplier
        after = update_stake(gid, win_amount, TransactionType.BET_WIN)
    else:
        outcome = "loss"
        after = update_stake(gid, -amount, TransactionType.BET_LOSS)

    cursor.execute("""
    INSERT INTO bets
    (gambler_id, amount, probability, outcome, strategy, stake_before, stake_after)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (gid, amount, strategy.probability, outcome, strategy.name, before, after))

    conn.commit()
    conn.close()

    print("Result:", outcome)