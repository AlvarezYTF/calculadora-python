from model.conection import Conexion

class ModeloCalculadora(Conexion):
    def __init__(self):
        super().__init__()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial (
                id INT AUTO_INCREMENT PRIMARY KEY,
                operacion VARCHAR(50),
                operando1 FLOAT,
                operando2 FLOAT,
                resultado FLOAT
            )
        ''')
        self.conn.commit()

    def sumar(self, a, b):
        resultado = a + b
        self.guardar_en_db("sumar", a, b, resultado)
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self.guardar_en_db("restar", a, b, resultado)
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.guardar_en_db("multiplicar", a, b, resultado)
        return resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        resultado = a / b
        self.guardar_en_db("dividir", a, b, resultado)
        return resultado

    def guardar_en_db(self, operacion, operando1, operando2, resultado):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO historial (operacion, operando1, operando2, resultado)
            VALUES (%s, %s, %s, %s)
        ''', (operacion, operando1, operando2, resultado))
        self.conn.commit()

    def obtener_historial(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM historial ORDER BY id DESC LIMIT 10')
        return cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
