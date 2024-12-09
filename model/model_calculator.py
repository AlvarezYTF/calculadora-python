from model.conection import Conection

class CalculatorModel(Conection):
    def __init__(self):
        super().__init__()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operation VARCHAR(50),
                operand1 FLOAT,
                operand2 FLOAT,
                result FLOAT
            )
        ''')
        self.conn.commit()

    def add(self, a, b):
        result = a + b
        self.save_to_db("sumar", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.save_to_db("restar", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.save_to_db("multiplicar", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        result = a / b
        self.save_to_db("dividir", a, b, result)
        return result

    def save_to_db(self, operation, operand1, operand2, result):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO history (operation, operand1, operand2, result)
            VALUES (%s, %s, %s, %s)
        ''', (operation, operand1, operand2, result))
        self.conn.commit()

    def fetch_history(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM history ORDER BY id DESC LIMIT 10')
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()
