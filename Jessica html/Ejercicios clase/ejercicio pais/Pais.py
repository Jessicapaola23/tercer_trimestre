class Pais:
    def __init__(self, nombre, poblacion, superficie,altura):
        self.__nombre=nombre
        self.__poblacion=poblacion
        self.__superficie=superficie
        self.__altura=altura
        
    def info(self):
        return f"{self.__nombre} {self.__poblacion} {self.__superficie} {self.__altura}"
    
    def getNombre(self):
        return self.__nombre
    
    def getPoblacion(self):
        return self.__poblacion
    
    def getSuperficie(self):
        return self.__superficie
    
    def getAltura(self):
        return self.__altura 