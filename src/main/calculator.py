"""
Calculator app
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
Modified by: Snely, 2025
"""
class Calculator:
    def __init__(self):
        self.last_result = 0

    def get_hello_message(self):
        """ Show welcome message """
        return "== Calculatrice v1.0 =="

    def addition(self, v1, v2):
        """ Add 2 values """
        self.last_result = v1 + v2
        return self.last_result

    def subtraction(self, v1, v2):
        """ Subtract 2 values """
        self.last_result = v1 - v2
        return self.last_result

    def multiplication(self, v1, v2):
        """ Multiply 2 values. """
        self.last_result = v1 * v2
        return self.last_result

    def division(self, v1, v2):
        """ Divide 2 values. Show an error if V2 is zero. """
        if (v2 != 0):
            self.last_result = v1 / v2
            return self.last_result
        else:
            self.last_result = "Error"
            return "Erreur : division par zéro"

my_calculator = Calculator()
print(my_calculator.get_hello_message())

is_running = True

while is_running:
    print("\n=== Menu ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une option (1-5) : ")

    if choix == "5":
        print("Au revoir !")
        is_running = False
        continue

    if choix in ["1", "2", "3", "4"]:
        try:
            val_x = float(input("Saisissez la valeur 1 : "))
            val_y = float(input("Saisissez la valeur 2 : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
            continue

        if choix == "1":
            my_calculator.addition(val_x, val_y)
            print(f"V1 + V2 = {my_calculator.last_result}")
        elif choix == "2":
            my_calculator.subtraction(val_x, val_y)
            print(f"V1 - V2 = {my_calculator.last_result}")
        elif choix == "3":
            my_calculator.multiplication(val_x, val_y)
            print(f"V1 * V2 = {my_calculator.last_result}")
        elif choix == "4":
            result = my_calculator.division(val_x, val_y)
            print(f"V1 / V2 = {result}")

    else:
        print("Option invalide, choisissez entre 1 et 5.")