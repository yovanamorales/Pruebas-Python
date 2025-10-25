class TarjetaCredito:
    tarjetas = []

    #Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses
    def __init__(self, limite_credito, intereses, saldo_pagar = 0):
        #(Aquí va los atributos de instancia y sus asignaciones de valor)
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas.append(self)
    
    
    #Crea el método compra para la clase TarjetaCredito
    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Compra rechazada: excede el límite de crédito.")
        else:
            self.saldo_pagar += monto
        return self
  
    #Crea el método pago para la clase TarjetaCredito
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
    
    #Crea el método mostrar_info_tarjeta para la clase TarjetaCredito
    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.2f}")

    #Crea el método cobrar_interes para la clase TarjetaCredito
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self
       
#bonus
    @classmethod
    def mostrar_todas(cls):
        print("\n--- Información de todas las tarjetas ---")
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {i}: Disponible = ${tarjeta.limite_credito:.2f}  "
                  f"Deuda Actual = ${tarjeta.saldo_pagar:.2f}, "
                  f"Interés = {tarjeta.intereses * 100:.1f}%, {tarjeta.saldo_pagar * tarjeta.intereses:.2f}  "
                  f"Saldo = ${(tarjeta.limite_credito-tarjeta.saldo_pagar):.2f}  ")

#Crea 3 tarjetas
#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.

tarjeta1 = TarjetaCredito(limite_credito=500000, intereses=0.05)
tarjeta1.compra(50000).compra(120000).cobrar_interes().mostrar_info_tarjeta()


#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta;
#  todo esto en una sola línea a través de la encadenación.

tarjeta2 = TarjetaCredito(limite_credito=200000, intereses = 0.02)
tarjeta2.compra(30000).compra(60000).compra(80000).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.

tarjeta3 = TarjetaCredito(limite_credito=300000, intereses= 0.03)
tarjeta3.compra(100000).compra(80000).compra(40000).compra(5000).compra(50000).cobrar_interes().mostrar_info_tarjeta()

tarjeta4 = TarjetaCredito(limite_credito=300000, intereses= 0.02)
tarjeta4.compra(100000).compra(200000).compra(120000).compra(5000).compra(50000).cobrar_interes().mostrar_info_tarjeta()

#BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. 
# En el capítulo pasado te dimos algunas pistas de cómo realizarlo.

TarjetaCredito.mostrar_todas()

