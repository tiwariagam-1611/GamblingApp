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
    CREATE TABLE IF NOT EXISTS bets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gambler_id INT NOT NULL,
        amount DOUBLE NOT NULL,
        probability DOUBLE NOT NULL,
        outcome VARCHAR(10),
        strategy VARCHAR(50),
        stake_before DOUBLE,
        stake_after DOUBLE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        gambler_id INT NOT NULL,
        status VARCHAR(50),
        start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        end_time TIMESTAMP NULL,
        total_games INT DEFAULT 0,
        final_stake DOUBLE,
        end_reason VARCHAR(50)
    )
    """)

    conn.commit()
    conn.close()