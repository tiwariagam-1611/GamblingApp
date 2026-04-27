from config.db import get_connection

def start_session(gid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sessions (gambler_id, status, total_games, final_stake)
    VALUES (%s, 'ACTIVE', 0, 0)
    """, (gid,))

    conn.commit()
    conn.close()

    print("Session started")


def end_session(gid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT current_stake FROM gambler WHERE id=%s
    """, (gid,))
    stake = cursor.fetchone()[0]

    cursor.execute("""
    UPDATE sessions
    SET status='ENDED', end_time=NOW(), final_stake=%s
    WHERE gambler_id=%s AND status='ACTIVE'
    """, (stake, gid))

    conn.commit()
    conn.close()

    print("Session ended")