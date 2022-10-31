import random

user_wins = 0
computer_wins = 0

options = ["b", "k", "g"]

while True:
    user_input = input("Ketik B untuk Batu/ K untuk Kertas/ G untuk Gunting atau Q untuk keluar: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "b" and computer_pick == "g":
        print("Kamu menang!")
        user_wins += 1
        continue

    elif user_input == "k" and computer_pick == "b":
        print("Kamu menang!")
        user_wins += 1

    elif user_input == "g" and computer_pick == "k":
        print("Kamu menang!")
        user_wins += 1

    else:
        print("Kamu kalah!")
        computer_wins += 1

print("Kamu menang", user_wins, "kali.")
print("Komputer menang", computer_wins, "kali.")
print("Sampai jumpa!")