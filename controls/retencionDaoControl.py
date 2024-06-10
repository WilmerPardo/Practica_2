from controls.dao.stackDaoAdapter import StackDaoAdapter
from controls.facturaDaoControl import FacturaDaoControl
from models.retencion import Retencion
import json

class RetencionDaoControl(StackDaoAdapter):
    def __init__(self):
        super().__init__(Retencion)
        self.__retencion = None

    @property
    def _retencion(self):
        if self.__retencion == None:
            self.__retencion = Retencion()
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value
    
    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self._retencion._id = self._lista._stack._length + 1
        self._save(self._retencion)



    def process_facturas(self, fact = FacturaDaoControl()):
        node = fact.lista._head
        while node is not None:
            factura = node._data
            self._retencion = Retencion()
            self._retencion._fecha = factura._fecha
            self._retencion._cliente = factura._usuario
            self._retencion._porcentajeRetencion = "8%" if factura._tipoRUC == "EDUCATIVO" else "10%"
            self._retencion._valorInicial = round(float(factura._monto), 2)
            self._retencion._retencion = round(self._retencion._valorInicial * 0.08, 2) if factura._tipoRUC == "EDUCATIVO" else round(self._retencion._valorInicial * 0.1, 2)
            self._retencion._valorFinal = round(self._retencion._valorInicial - self._retencion._retencion, 2)

            self.save
            node = node._next 

    
    def clear_all_retenciones(self):
            self.clear_json_data(self.URL + self.file)  # Llama a la función clear_json_data con la ruta del archivo JSON
            print("Retenciones eliminadas")
    
    def clear_json_data(self, filename):
            with open(filename, 'w') as f:
                json.dump({}, f)