from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self,productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self,producto):
        self._productos.append(producto)
    
    def  calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + "|"
        return f"Orden: {self._id_orden},Productos: {productos_str}"

if __name__ == "__main__":
    Producto1 = Producto("Camisa",100.00)
    producto2 = Producto("Pantalon",500.00)
    productos = [Producto1,producto2]
    print(productos)

    orden1 = Orden(productos)
    print(orden1)
    
    

