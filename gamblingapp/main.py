from services.gambler_service import *

while True:
    print("\nGambling App")
    print("1. Create Gambler")
    print("2. View Gamblers")
    print("3. Update Gambler")
    print("4. Validate Gambler")
    print("5. Reset Gambler")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_gambler()
    elif choice == "2":
        view_gamblers()
    elif choice == "3":
        update_gambler()
    elif choice == "4":
        validate_gambler()
    elif choice == "5":
        reset_gambler()
    elif choice == "6":
        break
    else:
        print("Invalid choice")