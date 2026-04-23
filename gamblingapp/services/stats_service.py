from config.db import get_connection

def get_stats(gid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT initial_stake, current_stake, total_bets, wins, losses
    FROM gambler WHERE id=%s
    """, (gid,))

    data = cursor.fetchone()
    conn.close()

    if not data:
        print("Not found")
        return

    initial, current, bets, wins, losses = data

    profit = current - initial
    win_rate = (wins / bets * 100) if bets > 0 else 0

    print("Initial:", initial)
    print("Current:", current)
    print("Profit:", profit)
    print("Win rate:", win_rate)