from TarjetaCredito import TarjetaCredito

#Actualizar el método __init__ de la clase Usuario
class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [] #lista TarjetaCredito tener varias tarjetas. 

    #actualizar tu clase de Usuario con el objetivo de asociar la clase de TarjetaCredito. 
    def agregar_tarjeta(self, limite_credito, intereses):
        tarjeta = TarjetaCredito(limite_credito,intereses)
        self.tarjetas.append(tarjeta)
        print(f"{self.nombre}: limite Credito $ {limite_credito}, Taza de interes {intereses *100:.1f} %")
        return self
    
    #Actualiza el método hacer_compra de la clase Usuario
    def hacer_compra(self, monto,numero_tarjeta = 0):
        if not self.tarjetas:
            print("El usuario no tiene tarjeta registrada")
            return self
        if self.tarjetas:
            self.tarjetas[numero_tarjeta].compra(monto)
        else:
            print(" Usuario tiene {len(self.tarjetas)} tarjeta(s).")
        return self

    #Actualiza el método pagar_tarjeta de la clase Usuario
    def pagar_tarjeta(self,monto,numero_tarjeta =0):
        if not self.tarjetas:
            print("No hay tarjeta que operar.")
            return self
        
        if 0 <= numero_tarjeta < len(self.tarjetas):
            self.tarjetas[numero_tarjeta].pago(monto)
        else:
            print(f"El usuario tiene {len(self.tarjetas)} tarjeta(s).")
        return self

    #Actualiza el método mostrar_saldo_usuario de la clase Usuario
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}{self.email}")
        if not self.tarjetas:
            print("No hay tarjeta que operar.")
            return self

        for i, tarjeta in enumerate(self.tarjetas, start=1):
            print(f"Tarjeta {i}:")
            tarjeta.mostrar_info_tarjeta()
        return self


usuario1= Usuario("yovana" , "Morales", "yovana@correo.com")
usuario1.agregar_tarjeta(100000,0.05).hacer_compra(50000).pagar_tarjeta(10000).mostrar_saldo_usuario()
