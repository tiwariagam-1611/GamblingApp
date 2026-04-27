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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preferences (
        gambler_id INT,
        min_bet DOUBLE,
        max_bet DOUBLE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stake_transaction (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gambler_id INT,
        type VARCHAR(50),
        amount DOUBLE,
        balance_before DOUBLE,
        balance_after DOUBLE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()