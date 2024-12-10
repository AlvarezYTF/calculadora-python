class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        self.modelo.crear_tabla()
        while True:
            operacion = self.vista.obtener_operacion()
            
            if operacion == 6:  # Salir
                self.vista.despedida()
                break

            if operacion == 5:  # Historial
                historial = self.modelo.obtener_historial()
                self.vista.mostrar_historial(historial)
                continue

            a, b = self.vista.obtener_entrada()

            try:
                if operacion == 1:
                    resultado = self.modelo.sumar(a, b)
                elif operacion == 2:
                    resultado = self.modelo.restar(a, b)
                elif operacion == 3:
                    resultado = self.modelo.multiplicar(a, b)
                elif operacion == 4:
                    resultado = self.modelo.dividir(a, b)
                self.vista.mostrar_resultado(resultado)
            except Exception as e:
                self.vista.mostrar_error(str(e))

        self.modelo.cerrar_conexion()
