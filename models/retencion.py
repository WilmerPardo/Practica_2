from models.factura import Factura

class Retencion():
    def __init__(self):#, factura = Factura()):
        self.__id = 0
        self.__fecha = "" #factura._fecha
        self.__cliente = " " #factura._usuario
        self.__porcentajeRetencion = '' #0.8 if factura._tipoRUC == "EDUCATIVO" else 0.1
        self.__valorInicial = 0.0 #factura._monto
        self.__retencion = 0.0
        self.__valorFinal = 0.0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _cliente(self):
        return self.__cliente

    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value

    @property
    def _porcentajeRetencion(self):
        return self.__porcentajeRetencion

    @_porcentajeRetencion.setter
    def _porcentajeRetencion(self, value):
        self.__porcentajeRetencion = value

    @property
    def _valorInicial(self):
        return self.__valorInicial

    @_valorInicial.setter
    def _valorInicial(self, value):
        self.__valorInicial = value

    @property
    def _retencion(self):
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _valorFinal(self):
        return self.__valorFinal

    @_valorFinal.setter
    def _valorFinal(self, value):
        self.__valorFinal = value 

    

    @property
    def serialize(self):
        return {
            "id": self._id,
            "fecha": self._fecha,
            "cliente": self._cliente,
            "porcentajeRetencion": self._porcentajeRetencion,
            "valorInicial": self._valorInicial,
            "retencion": self._retencion,
            "valorFinal": self._valorFinal
        }
    
    def deserializar(self, data):
        retencion = Retencion()
        retencion._id = data["id"]
        retencion._fecha = data["fecha"]
        retencion._cliente = data["cliente"]
        retencion._porcentajeRetencion = data["porcentajeRetencion"]
        retencion._valorInicial = data["valorInicial"]
        retencion._retencion = data["retencion"]
        retencion._valorFinal = data["valorFinal"]
        return retencion