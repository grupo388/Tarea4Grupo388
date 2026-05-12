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

#Realizo la clase abstracta Servicio (ABC) (Andrés Felipe Restrepo Moreno)
class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base
    @abstractmethod
    def calcular_costo(self):
        pass
    @abstractmethod
    def descripcion(self):
        pass

#Realizo la Reserva de Sala para la Herencia (Andrés Felipe Restrepo Moreno)
class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        return self.costo_base * horas
    def description(self):
        return "Servicio de reserva de sala"
    
#Realizo la clase de alquiler de equipos para el polimorfismo de la herencia (Andrés Felipe Restrepo Moreno)
class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias=1):
        return self.costo_base * dias
    def descripcion (self):
        return "Servicio de alquiler de equipos"

#Realizo la clase de asesoría especializada para los servicios especializados (Andrés Felipe Restrepo Moreno)
class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones=1):
        return self.costo_base * sesiones
    def descripcion(self):
        return "Servicio de asesoría especializada"


#Realizo la clase de reserva de salapara el polimorfismo de la herencia.
class Reserva:
    def __init__(self, cliente, servicio, duración):
        if duración <= 0:
            raise ValidacionError("La duración debe ser mayor a cero.")
        self.cliente = cliente
        self.servicio = servicio
        self.duración = duración
        self.estado = "Pendiente"

#Realizo el método para la confirmación de la reserva.
    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo(self.duración)
            if costo <= 0:
                raise Exception ("El costo no es válido.")
            self.estado = "confirmada"
            print("Reserva confirmada")
            print(f"Costo total: ${costo}")
#Realizo el método para la cancelación de la reserva.
        except Exception as e:
            logging.error(f"Error al confirmar reswerva: {e}")
            raise ClienteError("No fue posible confirmar la reserva") from e
    def cancelar(self):
        self.estado = "Cancelada"
        print("Resewrva cancelada")
#Realizo el método para mostrar el estado de la reserva.
    def mostrar_reserva(self):
        print("\n==== RESERVA ====")
        self.cliente.mostrar_info()
        print(f"Servicio: {self.servicio.descripción()}")
        print(f"Estado: {self.estado}")

clientes = []
reservas = []

try:

    # CLIENTE VÁLIDO
    cliente1 = Cliente(
        "Juan Pérez",
        "juan@gmail.com",
        "3001234567"
    )

    clientes.append(cliente1)

    # CLIENTE INVÁLIDO
    cliente2 = Cliente(
        "",
        "correo_malo",
        "abc"
    )

    clientes.append(cliente2)

except ValidacionError as e:

    logging.error(e)
    print(f"Error de validación: {e}")

else:

    print("Clientes registrados correctamente")

finally:

    print("Proceso de clientes finalizado")


try:

    servicio1 = ReservaSala("Sala VIP", 50000)

    reserva1 = Reserva(cliente1, servicio1, 3)

    reserva1.confirmar()

    reservas.append(reserva1)

    reserva1.mostrar_reserva()

except Exception as e:

    logging.error(e)
    print(f"Ocurrió un error: {e}")

finally:

    print("Sistema ejecutado correctamente")
