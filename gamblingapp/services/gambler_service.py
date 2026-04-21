from config.db import get_connection

def create_gambler():
    name = input("Enter name: ")
    stake = float(input("Enter initial stake: "))
    win_limit = float(input("Enter win limit: "))
    loss_limit = float(input("Enter loss limit: "))

    if stake <= 0:
        print("Invalid stake")
        return

    if win_limit <= stake or loss_limit >= stake:
        print("Invalid limits")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO gambler (name, initial_stake, current_stake, win_limit, loss_limit)
    VALUES (%s, %s, %s, %s, %s)
    """, (name, stake, stake, win_limit, loss_limit))

    conn.commit()
    conn.close()

    print("Gambler created")


def view_gamblers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gambler")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_gambler():
    gid = int(input("Enter gambler ID: "))
    new_stake = float(input("Enter new stake: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE gambler SET current_stake=%s WHERE id=%s",
        (new_stake, gid)
    )

    conn.commit()
    conn.close()

    print("Updated")


def validate_gambler():
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT current_stake FROM gambler WHERE id=%s",
        (gid,)
    )
    result = cursor.fetchone()

    conn.close()

    if result and result[0] > 0:
        print("Eligible")
    else:
        print("Not eligible")


def reset_gambler():
    gid = int(input("Enter gambler ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE gambler
    SET current_stake = initial_stake,
        total_bets = 0,
        wins = 0,
        losses = 0
    WHERE id=%s
    """, (gid,))

    conn.commit()
    conn.close()

    print("Reset done")