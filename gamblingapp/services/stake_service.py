from config.db import get_connection
from models.transaction import TransactionType
from services.boundary_service import check_boundaries
import random

def place_bet():
    gid = int(input("Enter ID: "))
    amount = float(input("Enter bet amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT current_stake, win_limit, loss_limit, total_bets, wins, losses
    FROM gambler WHERE id=%s
    """, (gid,))
    data = cursor.fetchone()

    if not data:
        print("Not found")
        return 
    
    current, win_limit, loss_limit, bets, wins, losses = data

    if amount > current:
        print("Insufficient balance")
        return

    before = current

    result = random.choice(["win", "loss"])

    if result == "win":
        after = current + amount
        wins += 1
        ttype = TransactionType.BET_WIN
    else:
        after = current - amount
        losses += 1
        ttype = TransactionType.BET_LOSS

    bets += 1

    cursor.execute("""
    UPDATE gambler
    SET current_stake=%s, total_bets=%s, wins=%s, losses=%s
    WHERE id=%s
    """, (after, bets, wins, losses, gid))

    cursor.execute("""
    INSERT INTO stake_transaction
    (gambler_id, type, amount, balance_before, balance_after)
    VALUES (%s, %s, %s, %s, %s)
    """, (gid, ttype, amount, before, after))

    check_boundaries(after, win_limit, loss_limit)

    conn.commit()
    conn.close()

    print("Result:", result, "Balance:", after)