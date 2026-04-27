from services.win_loss_service import WinLossCalculator

calculator = WinLossCalculator()

def place_bet():
    gid = int(input("Enter ID: "))
    amount = float(input("Enter bet: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_stake FROM gambler WHERE id=%s", (gid,))
    current = cursor.fetchone()[0]

    if amount > current:
        print("Insufficient balance")
        return

    probability = 0.5

    result = calculator.process(amount, probability, current)

    after = update_stake(
        gid,
        result.winnings,
        TransactionType.BET_WIN if result.outcome == "win" else TransactionType.BET_LOSS
    )

    cursor.execute("""
    INSERT INTO bets
    (gambler_id, amount, probability, outcome, stake_before, stake_after)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (gid, amount, probability, result.outcome, current, after))

    conn.commit()
    conn.close()

    result.display()