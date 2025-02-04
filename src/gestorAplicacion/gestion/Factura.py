from datetime import date
import Cliente
from produccion import Tienda, Transporte, Producto

class Factura:
    _id = 0
    _fecha = date(2000, 1, 1)
    _tienda: Tienda = Tienda()
    _cliente: Cliente = Cliente()
    _transporte: Transporte = Transporte()
    _listaProductos:list[Producto()]
    _costoEnvio: float
    _total: float
    totalCreados: int
    def __init__(self, tienda, cliente, transporte, listaP, costoEnvio, fecha) -> None:
        self._id = self.totalCreados + 1
        self._fecha = fecha        
        self._tienda = tienda
        self._cliente = cliente
        self._transporte = transporte
        self._listaProductos = listaP
        self._costoEnvio = costoEnvio
        self.totalCreados += 1 