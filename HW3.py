
'''Starter code:

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")
Goal: build a slot machine with 3 spinning slots

Rules:

Each spin shows 3 random symbols V
The player starts with 50 money V
Before each spin, ask the user how much they want to bet V
The bet must be between 1 and the current money V
The user can choose to quit the game V
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
    while True:
        coins = int(input("How much are you betting"))
        if coins > money:
            print("You have not enough money")
            continue
        elif money >= coins >= 1:
            money -= coins
            return money

def spinning_symbol(symbols) -> list:
    machine_screen = list()
    for x in range(3):
        _symbol_in_machine = random.choice(symbols)
        machine_screen.append(_symbol_in_machine)
    return machine_screen

def calculation(bet, rate, machine_screen, symbols):
    _option = [machine_screen[0], machine_screen[1], machine_screen[2]]

    if _option[0] == _option[1] == _option[2]:
        _factor = rate.index[symbols.index(machine_screen[0])] * bet * 777
        return _factor
    elif _option[0] == _option[1] or _option[0] == _option[2]:
        _factor = rate.index[symbols.index(machine_screen[0])] * bet
        return _factor
    elif _option[1] == _option[2]:
        _factor = rate.index[symbols.index(machine_screen[1])] * bet
        return _factor
    else:
        return -bet


rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")

while money > 0:
    game = int(input("for game press 1, for quit press 2"))
    if game == 1:
        bet = player_bet(money)
        machine_screen = spinning_symbol(symbols)
        print(machine_screen)
        money += calculation(bet, rate, machine_screen, symbols)
        if money > 0:
            print(f"You have {money}")
    elif game == 2:
        break

print("=== GAME OVER === \n" f"you have {money} money left")


