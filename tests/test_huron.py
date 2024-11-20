
import unittest
from models.huron import Huron  # Importar la clase Huron desde el módulo models.huron

class TestHuron(unittest.TestCase):

    def setUp(self):
        
        self.huron = Huron(  nombre = "Gregorio"
                           , peso = 2.0
                           , edad = 4
                           , pais_origen = "USA"
                           , impuestos = 2000.10
                           )
        
    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")


    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 4000.2) #Este valor es correcto
        #self.assertEqual(self.huron.calcular_flete(), 4000.1) #Este valor es incorrecto 

    
    
    def test_calcular_flete_negativo(self):

        self.huron = Huron(  nombre = "Gregorio"
                           , peso = 2.0
                           , edad = 4
                           , pais_origen = "USA"
                           , impuestos = -2000.10
                           )
        self.assertEqual(self.huron.calcular_flete(), -4000.2) #Este valor es correcto
        #self.assertEqual(self.huron.calcular_flete(), 4000.2) #Este valor es incocorrecto
        



    def test_calcular_flete_zero(self):
        self.huron = Huron(  nombre = "Gregorio"
                           , peso = 2.0
                           , edad = 4
                           , pais_origen = "USA"
                           , impuestos = 0
                           )

        self.assertEqual(self.huron.calcular_flete(), 0) #Este valor es correcto
        #self.assertEqual(self.huron.calcular_flete(), 4000.2) #Este valor es Incorrecto



        
# Si este archivo se ejecuta directamente, se ejecutan las pruebas
if __name__ == '__main__':
    unittest.main()
