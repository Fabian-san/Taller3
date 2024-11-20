class Huron:

    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def hacer_sonido(self):
        return "¡Eek Eek!"
    
    def calcular_flete(self):
        
        valor_flete = self._peso * self._impuestos
        
        return valor_flete
