Python Gambling Simulation System

Overview

The Python Gambling Simulation System is a console-based application developed using Python. The project simulates a gambling environment where users can create gambler accounts, place bets, calculate odds, track transactions, and monitor wins and losses.

The project demonstrates important Python programming concepts including:

* Object-Oriented Programming
* Classes and Objects
* Static Methods
* Exception Handling
* Database Connectivity
* Modular Programming
* Enums
* Functions
* Random Module
* SQL Operations

---

Project Features

1. Gambler Management

* Create gambler accounts
* Store gambler details
* Maintain current stake
* Track total bets
* Track wins and losses
* Set win and loss boundaries

2. Betting System

* Place bets using stake amount
* Validate bet amount
* Randomly determine game result
* Update gambler balance
* Maintain betting statistics

3. Odds Calculation
   Supports multiple odds systems:

* Fixed Odds
* Probability-Based Odds
* Decimal Odds
* American Odds

4. Transaction Management

* Store betting transactions
* Record wins and losses
* Maintain transaction history

5. Boundary Checking

* Stop betting when win limit is reached
* Stop betting when loss limit is exceeded
* Protect gambler from excessive losses

---

Project Structure

project/
│
├── config/
│   └── db.py
│
├── models/
│   ├── gambler.py
│   ├── transaction.py
│   └── odds.py
│
├── services/
│   ├── betting_service.py
│   ├── transaction_service.py
│   └── boundary_service.py
│
├── exceptions/
│   └── custom_exceptions.py
│
├── main.py
└── README.txt

---

Modules Explanation

1. db.py
   Purpose:

* Establishes database connection
* Creates SQLite database connection

Concepts Used:

* Functions
* SQLite3 module
* Database connection handling

Example:
def get_connection():
return sqlite3.connect("gambling.db")

---

2. gambler.py
   Purpose:

* Represents gambler entity

Concepts Used:

* Class
* Constructor
* Object creation

Example:
class Gambler:
def **init**(self, name, stake):
self.name = name
self.stake = stake

---

3. transaction.py
   Purpose:

* Stores transaction types

Concepts Used:

* Enum

Why Enum?
Enum helps store fixed constant values like:

* WIN
* LOSS
* BET

Example:
from enum import Enum

class TransactionType(Enum):
WIN = "WIN"
LOSS = "LOSS"

Advantages of Enum:

* Better readability
* Prevents invalid values
* Improves code safety

---

4. odds.py
   Purpose:

* Calculates different betting odds

Concepts Used:

* Class
* Static Methods

Example:
class Odds:

```
@staticmethod
def fixed(multiplier, amount):
    return amount * multiplier
```

Why Static Method?
Static methods are used because:

* No object data is required
* Utility calculation methods
* Can directly call using class name

Example:
Odds.fixed(2, 100)

---

5. betting_service.py
   Purpose:

* Handles betting logic

Functions:

* Accepts bet amount
* Checks balance
* Randomly determines win/loss
* Updates database

Concepts Used:

* Functions
* Random module
* SQL queries
* Exception handling

Random Module:
Used to simulate gambling outcome.

Example:
import random
result = random.choice(["WIN", "LOSS"])

---

6. boundary_service.py
   Purpose:

* Checks gambling boundaries

Functions:

* Verify win limit
* Verify loss limit

Importance:
Prevents excessive gambling.

---

7. custom_exceptions.py
   Purpose:

* Stores user-defined exceptions

Concepts Used:

* Exception inheritance

Example:
class BetValidationException(Exception):
pass

Why “pass” is used?
pass means:

* No additional code inside class
* Empty placeholder class

Purpose of custom exceptions:

* Better error handling
* Specific error messages
* Cleaner code

---

Python Concepts Used

1. Classes
   Classes are blueprints for creating objects.

Example:
class Gambler:
pass

Advantages:

* Code reusability
* Better structure
* Easy maintenance

---

2. Objects
   Objects are instances of classes.

Example:
g1 = Gambler()

---

3. Constructor
   Constructor initializes object data.

Example:
def **init**(self, name):
self.name = name

---

4. Static Methods
   Methods independent of object data.

Example:
@staticmethod

Advantages:

* Utility methods
* Memory efficient
* No object creation needed

---

5. Exception Handling
   Used to manage runtime errors.

Example:
try:
amount = int(input())
except ValueError:
print("Invalid input")

Advantages:

* Prevents program crash
* Improves reliability
* Better user experience

---

6. Custom Exceptions
   User-defined exceptions for specific errors.

Example:
class InvalidBet(Exception):
pass

---

7. Enums
   Used for fixed constants.

Example:
TransactionType.WIN

Advantages:

* Better readability
* Safer code
* Organized constants

---

8. Functions
   Reusable blocks of code.

Example:
def place_bet():
pass

Advantages:

* Reduces repetition
* Improves readability
* Easy debugging

---

9. Database Connectivity
   Used SQLite database.

Advantages:

* Lightweight
* Easy to use
* No server required

Operations Used:

* INSERT
* SELECT
* UPDATE

---

10. Random Module
    Used to simulate gambling results.

Example:
random.choice()

---

Program Flow

1. Start application
2. Connect database
3. Display menu
4. Create or select gambler
5. Enter bet amount
6. Validate bet
7. Generate random result
8. Update stake
9. Store transaction
10. Display updated statistics
11. Repeat until exit

---

Sample Menu

1. Create Gambler
2. Place Bet
3. View Statistics
4. View Transactions
5. Exit

---

Sample Output

Enter ID: 1
Enter Bet Amount: 100

Result: WIN
Amount Won: 200

Updated Stake: 1200

---

Advantages of the Project

* Demonstrates real-world simulation
* Covers core Python concepts
* Uses database integration
* Implements exception handling
* Follows modular programming
* Easy to extend and maintain

---

Future Improvements

* GUI implementation using Tkinter
* Online multiplayer betting
* Authentication system
* Advanced statistics
* Different game modes
* Web application integration

---

Technologies Used

* Python
* SQLite
* Random Module
* Enum Module

---

Conclusion

The Python Gambling Simulation System is a practical project that demonstrates both beginner and intermediate Python concepts. It combines object-oriented programming, database operations, exception handling, and modular coding practices into a single real-world application.

The project helps in understanding:

* Python architecture
* Database integration
* Business logic handling
* Error management
* Modular application design
