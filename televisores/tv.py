class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if not self._permitidoCambiarCanal(canal):
            return

        self._canal = canal

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if not self._permitidoCambiarVolumen(volumen):
            return

        self._volumen = volumen

    def getControl(self):
        return self._control

    def setControl(self, control):
        self._control = control

    @staticmethod
    def getNumTV():
        return TV._numTV

    @staticmethod
    def setNumTV(numTV):
        TV._numTV = numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if not self._permitidoCambiarCanal(self._canal + 1):
            return

        self._canal += 1

    def canalDown(self):
        if not self._permitidoCambiarCanal(self._canal - 1):
            return

        self._canal -= 1

    def volumenUp(self):
        if not self._permitidoCambiarVolumen(self._volumen + 1):
            return

        self._volumen += 1

    def volumenDown(self):
        if not self._permitidoCambiarVolumen(self._volumen - 1):
            return

        self._volumen -= 1

    def _permitidoCambiarCanal(self, canal):
        if not self._estado:
            return False

        return canal >= 1 and canal <= 120

    def _permitidoCambiarVolumen(self, volumen):
        if not self._estado:
            return False

        return volumen >= 0 and volumen <= 7
