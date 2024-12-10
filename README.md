# Calculadora con MVC en Python
Este proyecto implementa una calculadora utilizando el patrón de diseño Modelo-Vista-Controlador (MVC) en Python. La calculadora permite realizar operaciones básicas, almacenar el historial en una base de datos MySQL y consultar las últimas 10 operaciones realizadas.

## Características
- Operaciones básicas: suma, resta, multiplicación y división.
- Validación para evitar divisiones por cero.
- Historial de operaciones almacenado en una base de datos MySQL.
- Interfaz de usuario basada en texto con mensajes claros para guiar al usuario.
- Patrón MVC que separa la lógica de negocio, la presentación y el control.

## Requisitos

- Python 3.8 o superior.
- MySQL instalado y configurado.
- Biblioteca mysql-connector-python para conectar Python con MySQL.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/AlvarezYTF/calculadora-python
   cd calculadora-python
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install mysql-connector-python
   ```

## Configuración

1. Base de datos:
- Crea una base de datos llamada calculator en MySQL.
- Asegúrate de que el usuario y contraseña configurados en Conection coincidan con tu entorno MySQL.
   ```sql
   CREATE DATABASE calculator;
   ```

2. Estructura de la tabla:
- La tabla `historial` se crea automáticamente al iniciar el programa, si no existe.

3. Utiliza las funciones de la clase `Database` para interactuar con la base de datos.

## Estructura de carpetas:

   ```css
   .
   ├── model/
   │   ├── conection.py
   │   ├── model_calculator.py
   ├── view/
   │   ├── view_calculator.py
   ├── controller/
   │   ├── controller_calculator.py
   ├── main.py
   └── README.md
   ```

## Cómo usar

1. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

2. Interfaz de usuario:
- Selecciona una operación del menú.
- Ingresa los números solicitados.
- Consulta el historial de operaciones si lo necesitas.
- Sal de la aplicación seleccionando la opción correspondiente.

## Estructura del Proyecto

1. Modelo (`model`)
Encargado de interactuar con la base de datos. Define métodos para realizar las operaciones y almacenar/consultar el historial.

2. Vista (`view`)
Proporciona la interfaz de usuario basada en texto. Recoge entradas y muestra resultados o mensajes.

3. Controlador (`controller`)
Gestiona la interacción entre el modelo y la vista. Maneja la lógica de la aplicación y los flujos de trabajo.

## Funciones futuras
- Soporte para operaciones más avanzadas (potencias, raíces, etc.).
- Exportar el historial a un archivo CSV.
- Interfaz gráfica con herramientas como Tkinter o PyQt.

## Contribuciones
Si deseas contribuir a este proyecto, realiza un fork, haz tus modificaciones y envía un pull request. ¡Tus aportes son bienvenidos!
