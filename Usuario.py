from TarjetaCredito import *

#Actualizar el método __init__ de la clase Usuario
class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [] #lista TarjetaCredito tener varias tarjetas. 

    def agregar_tarjetas(self, tarjeta):
        if isinstance(tarjeta,TarjetaCredito):
            self.tarjetas.append(tarjeta)
        else:
            print("la tarjeta indicada no existe")
        return self

    def hacer_compra(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
            tarjeta.compra(monto)
            print(f"{self.nombre}: Compra por ${monto:.2f} realizada con éxito en la tarjeta {tarjeta.numero}.")
        else:
            print("tarjeta no pertenece al usuario.")
        return self
        
    def pagar_tarjeta(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
           tarjeta.pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"usuario:{self.nombre} {self.apellido},{self.email} Saldo a Pagar:")
        print("Saldo de tarjetas:")
        for tarjeta in self.tarjetas:
             tarjeta.mostrar_info_tarjeta()
        return self



master_card = TarjetaCredito(200000,0.03)
usuario1= Usuario("yovana" , "Morales", "yovana@correo.com")
usuario1.agregar_tarjetas(master_card)
usuario1.hacer_compra(50000,master_card)
usuario1.pagar_tarjeta(10000,master_card)
usuario1.mostrar_saldo_usuario()
