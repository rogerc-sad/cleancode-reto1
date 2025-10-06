from unittest.mock import Mock
import pytest
from domain.pedido import Pedido
from domain.carrito import Carrito, ItemCarrito
from use_cases.generar_pedido import GenerarPedido

def test_generar_pedido():
    # Mock de repositorio
    repositorio_mock = Mock()
    carrito = Carrito(id_cliente='1')
    carrito.agregar_item(ItemCarrito(producto=Mock(precio=100), cantidad=2))

    caso_uso = GenerarPedido(repositorio=repositorio_mock)
    pedido = caso_uso.ejecutar(carrito)

    repositorio_mock.guardar.assert_called_once_with(pedido)
