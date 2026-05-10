from abc import ABC, abstractmethod
import logging

# Realizo la configuración del sistema de logs
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
#Realizo las excepciones personalizadas
class ClienteError(Exception):
    pass
class ValidacionError(Exception):
    pass

#Realizo la clase abstracta Entidad
class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

    #Realizo la clase cliente que hereda de la clase Entidad
    class Cliente(Entidad):
        def __init__(self, nombre, correo, telefono):
            if not nombre.strip():
                raise ValidacionError("El nombre no puede estar vacío.")
            if "@" not in correo:
                raise ValidacionError("Correo electrónico no válido.")
            if not telefono.isdigit():
                raise ValidacionError("El telefono debe contener solo números")
            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

        #Realizo el método getter para la encapsulación de los atributos
        def get_nombre(self):
            return self.__nombre
        def get_correo(correo):
            return self.__correo
        def get_telefono(telefono):
            return self.__telefono
        
        #Realizo el método setters para las validaciones de los atributos
        def set_nombre(self, nombre):
            self.__nombre = nombre
        def set_correo(self, correo):
            self.__correo = correo
        def set_telefono(self, telefono):
            self.__telefono = telefono
        #Realizo el método mostrar_info para mostrar la información del cliente.
        def mostrar_info(self):
            print(f"Cliente: {self.__nombre}")
            print(f"Correo: {self.__correo}")
            print(f"Telefono: {self.__telefono}")
