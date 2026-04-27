from config.db import get_connection
from models.transaction import TransactionType
from services.safe_input import get_positive_stake, get_float
from services.validator_service import InputValidator

validator = InputValidator()


def create_gambler():
    name = input("Enter name: ")

    stake = get_positive_stake("Enter stake: ")
    win_limit = get_float("Enter win limit: ")
    loss_limit = get_float("Enter loss limit: ")

    try:
        validator.validate_limits(stake, win_limit, loss_limit)
    except Exception as e:
        print("Error:", e)
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO gambler (name, initial_stake, current_stake, win_limit, loss_limit)
    VALUES (%s,%s,%s,%s,%s)
    """, (name, stake, stake, win_limit, loss_limit))

    gid = cursor.lastrowid

    cursor.execute("""
    INSERT INTO stake_transaction
    (gambler_id, type, amount, balance_before, balance_after)
    VALUES (%s,%s,%s,%s,%s)
    """, (gid, TransactionType.INITIAL, stake, 0, stake))

    conn.commit()
    conn.close()

    print("Gambler created")


def view_gambler():
    gid = int(input("Enter ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gambler WHERE id=%s", (gid,))
    row = cursor.fetchone()

    conn.close()

    if row:
        print(row)
    else:
        print("Not found")


def update_gambler():
    gid = int(input("Enter ID: "))

    name = input("New name: ")
    win_limit = get_float("New win limit: ")
    loss_limit = get_float("New loss limit: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE gambler
    SET name=%s, win_limit=%s, loss_limit=%s
    WHERE id=%s
    """, (name, win_limit, loss_limit, gid))

    conn.commit()
    conn.close()

    print("Updated")


def validate_gambler():
    gid = int(input("Enter ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT current_stake, win_limit, loss_limit FROM gambler WHERE id=%s
    """, (gid,))
    data = cursor.fetchone()

    conn.close()

    if not data:
        print("Not found")
        return

    current, win_limit, loss_limit = data

    if current <= 0:
        print("Not eligible")
    elif current >= win_limit:
        print("Win condition reached")
    elif current <= loss_limit:
        print("Loss condition reached")
    else:
        print("Eligible")


def reset_gambler():
    gid = int(input("Enter ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT initial_stake FROM gambler WHERE id=%s", (gid,))
    data = cursor.fetchone()

    if not data:
        print("Not found")
        return

    initial = data[0]

    cursor.execute("""
    UPDATE gambler
    SET current_stake=%s, total_bets=0, wins=0, losses=0
    WHERE id=%s
    """, (initial, gid))

    cursor.execute("""
    INSERT INTO stake_transaction
    (gambler_id, type, amount, balance_before, balance_after)
    VALUES (%s,%s,%s,%s,%s)
    """, (gid, TransactionType.RESET, 0, 0, initial))

    conn.commit()
    conn.close()

    print("Reset done")