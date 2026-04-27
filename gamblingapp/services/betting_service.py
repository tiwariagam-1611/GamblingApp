import random
from config.db import get_connection
from services.stake_service import update_stake
from models.transaction import TransactionType
from services.validator_service import InputValidator
from services.safe_input import get_float
from services.win_loss_service import WinLossCalculator
from models.strategy import get_strategy

validator = InputValidator()
calculator = WinLossCalculator()


def place_bet():
    gid = int(input("Enter ID: "))
    amount = get_float("Enter bet amount: ")

    print("Choose Strategy")
    print("1 Easy  2 Medium  3 Hard")
    strategy = get_strategy(input("Choice: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT current_stake FROM gambler WHERE id=%s", (gid,))
    data = cursor.fetchone()

    if not data:
        print("Gambler not found")
        return

    current = data[0]

    try:
        validator.validate_bet_amount(amount, current)
        validator.validate_probability(strategy.probability)
    except Exception as e:
        print("Error:", e)
        return

    before = current

    result = calculator.process(amount, strategy.probability, current)

    after = update_stake(
        gid,
        result.winnings,
        TransactionType.BET_WIN if result.outcome == "win" else TransactionType.BET_LOSS
    )

    cursor.execute("""
    INSERT INTO bets
    (gambler_id, amount, probability, outcome, strategy, stake_before, stake_after)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        gid,
        amount,
        strategy.probability,
        result.outcome,
        strategy.name,
        before,
        after
    ))

    conn.commit()
    conn.close()

    result.display()