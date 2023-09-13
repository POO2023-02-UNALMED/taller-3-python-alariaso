class Marca:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre
