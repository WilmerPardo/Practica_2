import sys
sys.path.append('../')

from controls.tda.linked.linkedList import Linked_List
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
import random
import time

listaNumber = Linked_List()
listaString = Linked_List()
try:
    fact = FacturaDaoControl()
    ret = RetencionDaoControl()

    """ fact._factura._usuario = "Juan"
    fact._factura._fecha = "2021-10-10"
    fact._factura._monto = 100
    fact._factura._tipoRUC = "EDUCATIVO"
    fact._factura._RUC = "1234567890"
    fact.save

    fact._factura._usuario = "William Chamba"
    fact._factura._fecha = "2021-10-10"
    fact._factura._monto = 10000
    fact._factura._tipoRUC = "PROFESIONAL"
    fact._factura._RUC = "1234567890"
    fact.save

    fact._factura._usuario = "Andres Pardo"
    fact._factura._fecha = "2021-10-10"
    fact._factura._monto = 2000
    fact._factura._tipoRUC = "PROFESIONAL"
    fact._factura._RUC = "1234567890"
    fact.save
    
    fact._factura._usuario = "Rafael Chuquihuanca"
    fact._factura._fecha = "2021-10-10"
    fact._factura._monto = 100
    fact._factura._tipoRUC = "EDUCATIVO"
    fact._factura._RUC = "1234567890"
    fact.save

    ret.process_facturas(fact)
    ret.clear_all_retenciones() """

    for i in range(10):
        listaNumber.add(random.randint(0,100000))

    #listaNumber.add(1995.19)
    #listaNumber.add(1995.19)
    #listaNumber.print
    inicio = time.time()
    listaNumber.sort(1,0)
    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)

    listaString.add("Juan Perez")
    listaString.add("William Chamba")
    listaString.add("Andres Pardo")
    listaString.add("Rafael Chuquihuanca")
    listaString.add("David Jimenez")
    listaString.add("Carlos Andrade")
    listaString.add("Brandon Gutierrez")
    listaString.add("Estefania Cale")
    listaString.add("Ximena Yanayaco")
    listaString.add("Ximena Yanayaco")
    
    listaAuxx = listaString.binary_search_secuencial("Ximena Yanayaco", 1)
    #print(listaAuxx)
    #listaString.print
    listaString.sort(1)
    #listaAuxStr = listaString.search_equals("ez")
    #listaAuxStr.print
    #listaString.print
    #listaString.binary_search("ez", 0)

    
    
    #fact._list().print
    listaAux = fact._list().sort_models('_monto', 1, 0) 
    #listaAux.print
    #fact._list().sort_models('_usuario', 1).print

    #facturita = fact._list().binary_search_models(120.20, '_monto', 1) 
    #facturota = fact._list().binary_search_models('Rafael Chuquihuanca', '_usuario', 2) #busqueda binaria
    #facturaAux = fact._list().binary_models(200, '_monto', 1) #binaria secuencial
    #print(facturaAux)
    
except Exception as e:
    print(f"Error: {e}")