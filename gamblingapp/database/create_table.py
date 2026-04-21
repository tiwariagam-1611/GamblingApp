from config.db import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gambler (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        initial_stake DOUBLE,
        current_stake DOUBLE,
        win_limit DOUBLE,
        loss_limit DOUBLE,
        total_bets INT DEFAULT 0,
        wins INT DEFAULT 0,
        losses INT DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()