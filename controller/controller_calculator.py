class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.create_table()
        while True:
            operation = self.view.get_operation()
            
            if operation == 6:  # Salir
                self.view.goodbye()
                break

            if operation == 5:  # Historial
                history = self.model.fetch_history()
                self.view.display_history(history)
                continue

            a, b = self.view.get_input()

            try:
                if operation == 1:
                    result = self.model.add(a, b)
                elif operation == 2:
                    result = self.model.subtract(a, b)
                elif operation == 3:
                    result = self.model.multiply(a, b)
                elif operation == 4:
                    result = self.model.divide(a, b)
                self.view.display_result(result)
            except Exception as e:
                self.view.display_error(str(e))

        self.model.close_connection()
