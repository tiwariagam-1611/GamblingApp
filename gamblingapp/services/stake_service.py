from config.db import get_connection
from models.transaction import TransactionType

def update_stake(gid, amount, ttype):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT current_stake, win_limit, loss_limit, total_bets, wins, losses
    FROM gambler WHERE id=%s
    """, (gid,))
    data = cursor.fetchone()

    if not data:
        return None

    current, win_limit, loss_limit, bets, wins, losses = data

    before = current
    after = current + amount

    if ttype == TransactionType.BET_WIN:
        wins += 1
        bets += 1
    elif ttype == TransactionType.BET_LOSS:
        losses += 1
        bets += 1

    cursor.execute("""
    UPDATE gambler
    SET current_stake=%s, total_bets=%s, wins=%s, losses=%s
    WHERE id=%s
    """, (after, bets, wins, losses, gid))

    cursor.execute("""
    INSERT INTO stake_transaction
    VALUES (NULL,%s,%s,%s,%s,%s,NOW())
    """, (gid, ttype, amount, before, after))

    conn.commit()
    conn.close()

    return after


def deposit():
    gid = int(input("Enter ID: "))
    amount = float(input("Amount: "))
    update_stake(gid, amount, TransactionType.DEPOSIT)


def withdraw():
    gid = int(input("Enter ID: "))
    amount = float(input("Amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_stake FROM gambler WHERE id=%s", (gid,))
    current = cursor.fetchone()[0]
    conn.close()

    if amount > current:
        print("Insufficient")
        return

    update_stake(gid, -amount, TransactionType.WITHDRAW)


def stake_report():
    gid = int(input("Enter ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, amount, balance_before, balance_after
    FROM stake_transaction WHERE gambler_id=%s
    """, (gid,))

    for row in cursor.fetchall():
        print(row)

    conn.close()