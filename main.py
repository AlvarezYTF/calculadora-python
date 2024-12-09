from view.view_calculator import CalculatorView
from model.model_calculator import CalculatorModel
from controller.controller_calculator import CalculatorController

if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    controller.run()
