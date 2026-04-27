from config.db import get_connection
from models.transaction import TransactionType

def create_gambler():
    name = input("Enter name: ")
    stake = float(input("Enter stake: "))
    win_limit = float(input("Enter win limit: "))
    loss_limit = float(input("Enter loss limit: "))

    if stake <= 0 or win_limit <= stake or loss_limit >= stake:
        print("Invalid input")
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
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gambler WHERE id=%s", (gid,))
    row = cursor.fetchone()

    conn.close()

    if row:
        print(row)
    else:
        print("Not found")


def view_all_gamblers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gambler")

    for row in cursor.fetchall():
        print(row)

    conn.close()


def update_gambler():
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gambler WHERE id=%s", (gid,))
    if not cursor.fetchone():
        print("Not found")
        conn.close()
        return

    name = input("Enter new name (leave blank to skip): ")
    win_limit = input("Enter new win limit (blank to skip): ")
    loss_limit = input("Enter new loss limit (blank to skip): ")

    if name:
        cursor.execute("UPDATE gambler SET name=%s WHERE id=%s", (name, gid))

    if win_limit:
        cursor.execute("UPDATE gambler SET win_limit=%s WHERE id=%s", (float(win_limit), gid))

    if loss_limit:
        cursor.execute("UPDATE gambler SET loss_limit=%s WHERE id=%s", (float(loss_limit), gid))

    conn.commit()
    conn.close()

    print("Updated")


def validate_gambler():
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT current_stake, win_limit, loss_limit
    FROM gambler WHERE id=%s
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
        print("Reached win condition")
    elif current <= loss_limit:
        print("Reached loss condition")
    else:
        print("Eligible to play")


def reset_gambler():
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT initial_stake FROM gambler WHERE id=%s
    """, (gid,))
    data = cursor.fetchone()

    if not data:
        print("Not found")
        conn.close()
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