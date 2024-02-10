"""Clase para simular el pago de nómina de un empleado"""

class empleado():

    # Método constructor:
    def __init__(self, codigo, sueldoBase, pagoHoraExtra, horasExtras, estadoCivil, numeroHijos):
        self.codigo = codigo                            # entero
        self.sueldoBase = sueldoBase                    # entero
        self.pagoHoraExtra = pagoHoraExtra              # entero
        self.horasExtras = horasExtras                  # entero
        self.estadoCivil = estadoCivil                  # string
        self.numeroHijos = numeroHijos                  # entero


    # Calcular las horas extras.
    def pagoHorasExtras(self):

        totalHorasExtras = self.pagoHoraExtra * self.horasExtras    # Multiplicamos el número de horas * las horas extras trabajadas.

        return totalHorasExtras


    # Calcular el sueldo incluyendo las horas extras.
    def calcularSueldo(self):

        totalHorasExtras = self.pagoHorasExtras()

        sueldo = self.sueldoBase + totalHorasExtras

        return sueldo


    # calcular retencion estado civil.
    def retencion1(self):                                               # Retención por estado civil

        if self.estadoCivil == "casado":                                # la calculamos con base en el sueldo base.
            descuento = self.sueldoBase * .05

        return descuento


    # calcular retención por el número de hijos.
    def retencion2(self):                                               # Retención por el número de hijos.

        if self.numeroHijos > 0:
            descuento = self.sueldoBase * (self.numeroHijos * .05)      # la calculamos con base en el sueldo base.

        return descuento


    # Calcular las retenciones.
    def retenciones(self):

        retencion1 = self.retencion1()                                  # Retención por estado civil.
        retencion2 = self.retencion2()                                  # Retención por el número de hijos.

        retenciones = retencion1 + retencion2

        return retenciones


    # Calcular el sueldo neto.
    def sueldoNeto(self):

        sueldoNeto = self.calcularSueldo() - self.retenciones()

        return sueldoNeto


    # Mostrar los detalles de pago.
    def detallesDePago(self):

        retenciones = self.retenciones()
        sueldoNeto = self.sueldoNeto()

        print("Detalles de pago: código ", self.codigo ,'\n',
              "1. Sueldo base: ", self.sueldoBase, '\n',
              "2. Horas extras laboradas: ", self.horasExtras, '\n',
              "3. Valor hora extra: ", self.pagoHoraExtra, '\n',
              "4. Retenciones: ", retenciones, '\n',
              "5. Sueldo neto: ", sueldoNeto)




