class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        return self._tv.turnOn()

    def turnOff(self):
        return self._tv.turnOff()

    def canalUp(self):
        return self._tv.canalUp()

    def canalDown(self):
        return self._tv.canalDown()

    def volumenUp(self):
        return self._tv.volumenUp()

    def volumenDown(self):
        return self._tv.volumenDown()

    def setCanal(self, canal):
        return self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        return self._tv.setVolumen(volumen)

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv
