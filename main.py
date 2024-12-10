from view.view_calculator import VistaCalculadora
from model.model_calculator import ModeloCalculadora
from controller.controller_calculator import ControladorCalculadora

if __name__ == "__main__":
    modelo = ModeloCalculadora()
    vista = VistaCalculadora()
    controlador = ControladorCalculadora(modelo, vista)
    controlador.ejecutar()
