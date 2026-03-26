
'''Starter code:

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")
Goal: build a slot machine with 3 spinning slots

Rules:

Each spin shows 3 random symbols V
The player starts with 50 money V
Before each spin, ask the user how much they want to bet
The bet must be between 1 and the current money
The user can choose to quit the game
Update the player’s money after each round
Winning rules:

All 3 symbols different → player loses the bet

2 of a kind → player gets bet * rate
3 of a kind → player gets bet * 777 * rate
Spin examples:

🍒 🍋 ⭐ → all different → lose
💎 💎 🍋 → 2 of a kind → win bet * 11
⭐ ⭐ ⭐ → 3 of a kind → win bet * 777 * 9
🔔 🍒 🔔 → 2 of a kind → win bet * 7
Important:

The correct rate depends on the matching symbol
Example: 3 × 🍋 → use rate 3
Example: 2 × 💎 → use rate 11
Game ends when:

The player chooses to quit
OR the player runs out of money
Hints:

Use random.choice or random.randint
Keep track of symbol indexes to match the correct rate
First check for 3 matches, then for 2 matches
Good luck'''



import random
def player_bet(money):

def spinning_symbol(symbols) -> list:
    machine_screen = list()
    for x in range(3):
        _symbol_in_machine = random.choice(symbols)
        machine_screen.append(_symbol_in_machine)
    return machine_screen


rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")


while money > 0:
    bet = player_bet(money)
    machine_screen = spinning_symbol(symbols)
    print(machine_screen)

print("=== GAME OVER === \n" f"you have {money} money left")


