from dataclasses import dataclass

# Interfaces
class GeneradorInforme:
    def generar(self, data: 'InformeData') -> None:
        raise NotImplementedError()

class Notificador:
    def notificar(self, data: 'InformeData') -> None:
        raise NotImplementedError()

class Repositorio:
    def guardar(self, data: 'InformeData') -> None:
        raise NotImplementedError()

# Implementaciones concretas
class InformePDF(GeneradorInforme):
    def generar(self, data: 'InformeData') -> None:
        # Lógica para generar PDF
        pass

class EmailNotificador(Notificador):
    def notificar(self, data: 'InformeData') -> None:
        # Lógica para enviar email
        pass

class InformeRepositorio(Repositorio):
    def guardar(self, data: 'InformeData') -> None:
        # Lógica para guardar en base de datos
        pass

# Servicio coordinador
class InformeService:
    def __init__(self, generador: GeneradorInforme, notificador: Notificador, repositorio: Repositorio) -> None:
        self.generador = generador
        self.notificador = notificador
        self.repositorio = repositorio

    def procesar(self, data: 'InformeData') -> None:
        self.generador.generar(data)
        self.notificador.notificar(data)
        self.repositorio.guardar(data)

# Datos del informe
@dataclass
class InformeData:
    contenido: str = ""
