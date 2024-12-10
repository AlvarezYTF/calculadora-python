class VistaCalculadora:
    def obtener_entrada(self):
        while True:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                return a, b
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")

    def obtener_operacion(self):
        while True:
            print("\nSeleccione una operación:")
            print("1: Sumar")
            print("2: Restar")
            print("3: Multiplicar")
            print("4: Dividir")
            print("5: Ver historial")
            print("6: Salir")
            try:
                opcion = int(input("Ingrese el número de la operación: "))
                if opcion in {1, 2, 3, 4, 5, 6}:
                    return opcion
                else:
                    print("Opción no válida. Seleccione un número entre 1 y 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entre 1 y 6.")

    def mostrar_resultado(self, resultado):
        print(f"\nEl resultado es: {resultado:.2f}")

    def mostrar_historial(self, historial):
        if not historial:
            print("\nEl historial está vacío.")
        else:
            print("\nHistorial de operaciones (últimas 10):")
            for registro in historial:
                print(f"{registro[1]}({registro[2]}, {registro[3]}) = {registro[4]:.2f}")

    def mostrar_error(self, mensaje_error):
        print(f"\nError: {mensaje_error}")

    def despedida(self):
        print("\n¡Gracias por usar la calculadora! Hasta luego.")
