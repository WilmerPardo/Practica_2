class Factura:
    def __init__(self):
        self.__id = 0
        self.__usuario = ""
        self.__fecha = ""
        self.__monto = 0
        self.__tipoRUC = ""
        self.__RUC = ""

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _usuario(self):
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _monto(self):
        return self.__monto

    @_monto.setter
    def _monto(self, value):
        self.__monto = value

    @property
    def _tipoRUC(self):
        return self.__tipoRUC

    @_tipoRUC.setter
    def _tipoRUC(self, value):
        self.__tipoRUC = value

    @property
    def _RUC(self):
        return self.__RUC

    @_RUC.setter
    def _RUC(self, value):
        self.__RUC = value

    @property
    def serialize(self):
        return {
            "id": self._id,
            "usuario": self._usuario,
            "fecha": self._fecha,
            "monto": self._monto,
            "tipoRUC": self._tipoRUC,
            "RUC": self._RUC
        }
    
    def deserializar(self, data):
        factura = Factura()
        factura._id = data["id"]
        factura._usuario = data["usuario"]
        factura._fecha = data["fecha"]
        factura._monto = data["monto"]
        factura._tipoRUC = data["tipoRUC"]
        factura._RUC = data["RUC"]
        return factura
    
    def __str__(self) -> str:
        return "Usuario: " + self._usuario + " " + self._fecha + " Monto:" + str(self._monto)
    
    __repr__ = __str__