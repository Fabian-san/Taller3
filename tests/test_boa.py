
import unittest
from models.boa import Boa

class Testboa(unittest.TestCase):

    def setUp(self):
        
        self.boa = Boa(  nombre = "Perla"
                         , peso = 2.3
                         , edad = 4
                         , pais_origen = "Colombia"
                         , impuestos = 520.0
                        )

   
        
    def test_hacer_sonido(self):
        """Prueba el método hacer_sonido."""
        self.assertEqual(self.boa.hacer_sonido(), "¡Tssss!")




    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 1209.8) 

    

    def test_calcular_flete_negativo(self):

        self.boa = Boa(  nombre = "Perla"
                         , peso = 2.3
                         , edad = 4
                         , pais_origen = "Colombia"
                         , impuestos = -520.0
                        )
        self.assertEqual(self.boa.calcular_flete(), -1209.8) 



        self.boa = Boa(  nombre = "Perla"
                         , peso = 2.3
                         , edad = 4
                         , pais_origen = "Colombia"
                         , impuestos = 0
                        )

        self.assertEqual(self.boa.calcular_flete(), 0)



    
    def test_getter_cantidad_ratones_comidos(self):
        self.assertEqual(self.boa.cantidad_ratones_comidos, 0)



    def test_setter_cantidad_ratones_comidos(self):
        self.boa.cantidad_ratones_comidos = 11
        self.assertEqual(self.boa.cantidad_ratones_comidos, 11) 

    
    


if __name__ == '__main__':
    unittest.main()
