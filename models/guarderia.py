from models.boa import Boa  
from models.huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [
            Boa("Perla", 2.3, 4, "Colombia", 526),
            Boa("Nagini", 3.0, 3, "Perú", 0.04)
        ]
        self.hurones = [
            Huron("German", 4.0, 4, "Colombia", 356.10),
            Huron("Muchuu", 2.5, 2, "Canada", 1000.10)
        ]

    def alimentar_boa(self, boa, cantidad_ratones):
        try:
            if boa is None:
                return "Esta Boa no existe!"
            
            # Verificar si la boa es válida y está en la lista
            if boa not in self.boas:
                return "Esta Boa no existe!"
            
            # Alimentar a la boa y manejar su respuesta
            return boa.alimentar(cantidad_ratones)
        
        except Exception as e:
            # Captura de cualquier error inesperado
            return f"Error inesperado: {e}"

