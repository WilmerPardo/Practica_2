from controls.dao.daoAdapter import DaoAdapter
from models.factura import Factura
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#class FacturaDaoControl(DaoAdapter, metaclass=Singleton):
class FacturaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

    @property
    def _factura(self):
        if self.__factura == None:
            self.__factura = Factura()
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value

    @property
    def _lista(self):
        return self._list
    
    @property
    def save(self):
        self._factura._id = self.lista._length + 1
        self._save(self._factura)
    
    def merge(self, pos):
        self._merge(self._factura, pos)
    
    def delete(self, pos):
        self._delete(self._factura, pos)

    
    def load_facturas(self):
            with open('data/factura.json', 'r') as f:
                data = json.load(f)
            for factura_data in data:
                factura = Factura()  
                factura._usuario = factura_data['usuario']
                factura._fecha = factura_data['fecha']
                factura._monto = factura_data['monto']
                factura._tipoRUC = factura_data['tipoRUC']
                factura._RUC = factura_data['RUC']
                
                self.lista.__addLast__(factura)
