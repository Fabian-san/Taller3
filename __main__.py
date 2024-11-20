# __main__.py

from models.guarderia import Guarderia

def main():
    guarderia = Guarderia()
    
    # Alimentar las boas
     # Boa 1 ha comido 3 ratones
    print(guarderia.alimentar_boa(guarderia.boas[0], 4)) 
    
    # Boa 1 ha comido 4 ratones 
    print(guarderia.alimentar_boa(guarderia.boas[0], 7))  
    
    # Error: Demasiados Ratones
    print(guarderia.alimentar_boa(guarderia.boas[0], 4))  
    
     # Boa 2 ha comido 5 ratones
    print(guarderia.alimentar_boa(guarderia.boas[1], 5)) 
    
    # Esta Boa no existe!
    print(guarderia.alimentar_boa(None, 2))  
    
    
    # Esta Boa no existe!
    print(guarderia.alimentar_boa("Boa 3", 3))  


if __name__ == "__main__":
    main()
