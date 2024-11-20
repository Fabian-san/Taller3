

class Boa():

    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuestos:float):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        self._comer = 0 
        
    def hacer_sonido(self):
        return "¡Tssss!"  
         
    def calcular_flete(self):
        valor_flete = self._peso * self._impuestos
        return valor_flete

    @property
    def cantidad_ratones_comidos(self):
        return self._comer
        
    @cantidad_ratones_comidos.setter
    def cantidad_ratones_comidos(self, nuevo_raton: int):
        if not isinstance(nuevo_raton, int):
            raise ValueError('Expected Int')

        if self._comer + nuevo_raton > 20:
            raise ValueError('Demasiados Ratones')
        
        self._comer += nuevo_raton

    def alimentar(self, cantidad_ratones: int):
        self.cantidad_ratones_comidos = cantidad_ratones
        return f"Boa {self._nombre} ha comido {self._comer} ratones."
    
     
      