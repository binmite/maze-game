import os

class Utilities:

     def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu():
        clear()
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

    def choice(min_val, max_val):
    while True:
        try:
            user_input = int(input())
            if min_val <= user_input <= max_val:
                return user_input
            print(f"Пожалуйста, введите число от {min_val} до {max_val}:")
        except ValueError:
            print(f"Пожалуйста, введите число от {min_val} до {max_val}:")

    def start():
        while True():
            int(choice) = choice(1, 3)
            match choice:
                case 1:
                    #тут будет отрисовываться карта для изи
                    break
                case 2:
                    #тут будет отрисовываться карта для медиума
                    break
                case 3:
                    ##тут будет отрисовываться карта для харда
                    break
            