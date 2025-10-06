class CuentaBancaria:
    # Clase que representa una cuenta bancaria.

    def __init__(self, titular: str, saldo: float = 0.0):
        # Atributos encapsulados
        self.titular = titular
        self.saldo = saldo
    
    def retirar(self, monto: float) -> bool:
        # Validamos si el monto es valido
        if monto <= 0:
            return False

        # Retira fondos de la cuenta si hay saldo suficiente.
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def depositar(self, monto: float) -> None:
        # Valida que el monto sea positivo antes de depositar
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto debe ser mayor a cero.")

    def obtener_saldo(self) -> float:
        #Devuelve el saldo actual
        return self.saldo


class Transferencia:
    # Clase que gestiona la transferencia entre dos cuentas.
    # se cambia el nombre de la funcion para evitar confusiones
    def transferir(origen: CuentaBancaria, destino: CuentaBancaria, monto: float) -> None:
        # Realiza la transferencia de una cuenta a otra.
        if origen.retirar(monto):
            destino.depositar(monto)
            print(f"Transferencia de {monto} realizada con éxito.")
        else:
            print("No se pudo realizar la transferencia.")


if __name__ == "__main__":
    # Instanciamos las cuentas para la transferencia
    cuenta_a = CuentaBancaria("A", 1000)
    cuenta_b = CuentaBancaria("B", 500)

    # Transferencia de fondos
    Transferencia.transferir(cuenta_a, cuenta_b, 200)

    # Mostramos los saldos despues de la transferencia
    print(cuenta_a.obtener_saldo(), cuenta_b.obtener_saldo())