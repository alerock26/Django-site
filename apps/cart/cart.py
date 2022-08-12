class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro']={}
        else:
            self.carro = carro

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto_id] = {
                'producto_id' : producto.id,
                'nombre' : producto.nombre,
                'imagen' : producto.imagen.url,
                'precio' : str(producto.precio),
                'cantidad' : 1
            }
        else:
            for key, value in self.carro.items():
                if key == producto.id:
                    #value['cantidad'] = value['cantidad'] + 1
                    value['cantidad'] += 1
                    break
        self.save_cart()

    def save_cart(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro.keys():
            del self.carro[producto_id]
            self.save_cart()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == producto.id:
                value['cantidad'] = value['cantidad'] - 1
                if value['cantidad'] < 1:
                    self.eliminar(producto)
                break
        self.save_cart()

    def clear_cart(self):
        self.session['carro'] = {}
        self.session.modified = True