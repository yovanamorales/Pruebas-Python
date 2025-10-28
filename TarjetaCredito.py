class TarjetaCredito:
    tarjetas = []

    #Crea la clase TarjetaCredito con los atributos de saldo_pagar, limite_credito, intereses
    def __init__(self, limite_credito, intereses, saldo_pagar = 0):
        #(atributos de instancia y sus asignaciones de valor)
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.numero = len(TarjetaCredito.tarjetas) +1
        TarjetaCredito.tarjetas.append(self)
    
    
    #Crea el método compra para la clase TarjetaCredito
    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print(f"Tarjeta {self.numero}: rechazada has alcanzado tu límite de crédito")
            print(f"Saldo a pagar: ${self.saldo_pagar:.2f} pesos")
        else:
            self.saldo_pagar += monto
            print(f"tarjeta {self.numero:} Compra realizada ${monto:.2f} pesos.")
            print("")
        return self
  
    #Crea el método pago para la clase TarjetaCredito
    def pago(self, monto):
        if (monto > self.saldo_pagar):
            print(" El monto ingresado (${monto:.2f}) supera el saldo a pagar(${self.saldo_pagar:.2f})en la tarjeta {self.numero}.")
        else:
            self.saldo_pagar -= monto
            print(f"Realizo pago {monto:.2f} ==> Nuevo saldo: ${self.saldo_pagar:.2f}.")
        return self
    
    #Crea el método mostrar_info_tarjeta para la clase TarjetaCredito
    def mostrar_info_tarjeta(self):
        print(f"\n ===== Información de la Tarjeta {self.numero} ===== ")
        print(f"Saldo a Pagar: $ {self.saldo_pagar:.2f} pesos")
        print(f"Límite de Crédito: $ {self.limite_credito:.2f} pesos")
        print(f"Interés: {self.intereses * 100:.1f} %")
        print(f"Disponible: $ {(self.limite_credito - self.saldo_pagar):.2f} pesos")
        print("=" * 40)
        return self

    #método cobrar_interes para la clase TarjetaCredito
    def cobrar_interes(self):
        interes_a_pagar = (self.saldo_pagar * self.intereses)
        self.saldo_pagar += interes_a_pagar
        print(f"Interés aplicado ({self.intereses*100:.1f} % ): = $ {interes_a_pagar:.2f} pesos")
        return self
       
#bonus
    @classmethod
    def mostrar_todas(cls):
        print(f"\n======= Listado de {len(cls.tarjetas)} tarjetas(s) =======")
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"\nTarjeta {i}: Disponible ==> ${tarjeta.limite_credito:.2f} pesos /  "
                f"Deuda Actual ==> ${tarjeta.saldo_pagar:.2f} pesos / "
                f"Interés  {tarjeta.intereses * 100:.1f}%,==> {tarjeta.saldo_pagar * tarjeta.intereses:.2f} pesos /  "
                f"Disponible: $ {(tarjeta.limite_credito - tarjeta.saldo_pagar):.2f} pesos")
            '''print(f"\nTarjeta {i}:")
            print(f" • Límite: $ {tarjeta.limite_credito:.2f} pesos")
            print(f" • Deuda actual: $ {tarjeta.saldo_pagar:.2f} pesos")
            print(f" • Interés: {tarjeta.intereses * 100:.1f} %")
            print(f" • Disponible: $ {(tarjeta.limite_credito - tarjeta.saldo_pagar):.2f} pesos")'''
            #print(\n"-" * 40)


    @staticmethod
    def validar_monto(monto):
        if(type(monto) is float, int) and monto> 0:
            print(" el monto ingresado es valido")
        else:
            print("el monto ingresado es invalido")


#Crea 3 tarjetas
#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.

tarjeta1 = TarjetaCredito(500000,0.07)
tarjeta1.compra(50000).compra(120000).pago(50000).cobrar_interes().mostrar_info_tarjeta()


#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta;
#  todo esto en una sola línea a través de la encadenación.

tarjeta2 = TarjetaCredito(200000, 0.05)
tarjeta2.compra(30000).compra(60000).compra(80000).pago(30000).pago(60000).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; 
# todo esto en una sola línea a través de la encadenación.

tarjeta3 = TarjetaCredito(300000, 0.03)
tarjeta3.compra(120000).compra(80000).compra(50000).compra(50000).compra(30000).cobrar_interes().mostrar_info_tarjeta()

#BONUS: crea un método de clase para imprimir todas las instancias de la información de las tarjetas creadas. 
# En el capítulo pasado te dimos algunas pistas de cómo realizarlo.

TarjetaCredito.mostrar_todas()