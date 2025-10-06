from datetime import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class Empleado:
    id: str
    nombre: str
    salario: float

class FormateadorReporte:
    def formatear(self, empleados: List[Empleado]) -> str:
        raise NotImplementedError()

class FormateadorCSV(FormateadorReporte):
    def formatear(self, empleados: List[Empleado]) -> str:
        return ''.join(f"{e.id};{e.nombre};{e.salario}\n" for e in empleados)

class NotificadorReporte:
    def enviar(self, contenido: str) -> None:
        raise NotImplementedError()

class EmailNotificadorReporte(NotificadorReporte):
    def enviar(self, contenido: str) -> None:
        # Simular envío de correo
        print(f"Enviando correo con contenido:\n{contenido}")

class PersistenciaReporte:
    def guardar(self, contenido: str) -> None:
        raise NotImplementedError()

class ArchivoPersistenciaReporte(PersistenciaReporte):
    def guardar(self, contenido: str) -> None:
        # Simular persistencia en archivo
        print(f"Guardando reporte en archivo:\n{contenido}")

class Auditor:
    def registrar(self, tipo: str, longitud: int, fecha: datetime) -> None:
        raise NotImplementedError()

class AuditorSimple(Auditor):
    def registrar(self, tipo: str, longitud: int, fecha: datetime) -> None:
        # Simular registro de auditoría
        print(f"Auditando {tipo}, longitud: {longitud}, fecha: {fecha}")

class ReporteEmpleadosService:
    def __init__(self, formateador: FormateadorReporte, notificador: NotificadorReporte,
                 persistencia: PersistenciaReporte, auditor: Auditor) -> None:
        self.formateador = formateador
        self.notificador = notificador
        self.persistencia = persistencia
        self.auditor = auditor

    def generar_reporte(self, empleados: List[Empleado]) -> str:
        contenido = self.formateador.formatear(empleados)
        self.notificador.enviar(contenido)
        self.persistencia.guardar(contenido)
        self.auditor.registrar("REPORTE", len(contenido), datetime.now())
        return contenido

if __name__ == "__main__":
    empleados = [
        Empleado("001", "Ana Pérez", 1200),
        Empleado("002", "Luis Gómez", 1500),
        Empleado("003", "Carla Ruiz", 1000),
    ]

    formateador = FormateadorCSV()
    notificador = EmailNotificadorReporte()
    persistencia = ArchivoPersistenciaReporte()
    auditor = AuditorSimple()

    servicio = ReporteEmpleadosService(formateador, notificador, persistencia, auditor)
    servicio.generar_reporte(empleados)
