class CalculatorView:
    def get_input(self):
        while True:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                return a, b
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")

    def get_operation(self):
        while True:
            print("\nSeleccione una operación:")
            print("1: Sumar")
            print("2: Restar")
            print("3: Multiplicar")
            print("4: Dividir")
            print("5: Ver historial")
            print("6: Salir")
            try:
                option = int(input("Ingrese el número de la operación: "))
                if option in {1, 2, 3, 4, 5, 6}:
                    return option
                else:
                    print("Opción no válida. Seleccione un número entre 1 y 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entre 1 y 6.")

    def display_result(self, result):
        print(f"\nEl resultado es: {result:.2f}")

    def display_history(self, history):
        if not history:
            print("\nEl historial está vacío.")
        else:
            print("\nHistorial de operaciones (últimas 10):")
            for record in history:
                print(f"{record[1]}({record[2]}, {record[3]}) = {record[4]:.2f}")

    def display_error(self, error_message):
        print(f"\nError: {error_message}")

    def goodbye(self):
        print("\n¡Gracias por usar la calculadora! Hasta luego.")
