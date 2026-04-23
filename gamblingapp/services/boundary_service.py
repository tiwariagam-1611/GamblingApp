def check_boundaries(balance, win_limit, loss_limit):
    if balance >= win_limit:
        print("Win limit reached")
    elif balance <= loss_limit:
        print("Loss limit reached")

    if balance <= loss_limit * 1.2:
        print("Warning near loss limit")

    if balance >= win_limit * 0.8:
        print("Approaching win limit")