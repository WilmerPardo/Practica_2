from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, url_for
from controls.retencionDaoControl import RetencionDaoControl
from controls.facturaDaoControl import FacturaDaoControl
#import json

router = Blueprint('api', __name__)

@router.route('/')
def home():
    return render_template('template.html')


@router.route('/historial/facturas/ver')
def ver_facturas():
    factura = FacturaDaoControl()
    return render_template('factura/listaFacturas.html', lista = factura.to_dic())


@router.route('/historial')
def lista_historial():
    retencion = RetencionDaoControl()
    return render_template('factura/lista.html', lista = retencion.to_dict())
    #factura = FacturaDaoControl()
    #return render_template('factura/lista.html', lista = factura.to_dic())

#editar facturs
@router.route('/facturas/editar/<pos>')
def ver_editar(pos):
    fd = FacturaDaoControl()
    nene = fd._list().get(int(pos)-1)
    return render_template("factura/editar.html", data=nene)


@router.route('/historial/ver')
def ver_guardad():
    return render_template('factura/guardar.html')


@router.route('/historial/guardar', methods=['POST'])
def guardar_factura():
    factura = FacturaDaoControl()
    factura._factura._usuario = request.form['usuario']
    factura._factura._fecha = request.form['fecha']
    factura._factura._monto = float(request.form['monto'])
    factura._factura._tipoRUC = request.form['tipoRUC']
    factura._factura._RUC = request.form['RUC']
    factura.save
    return redirect('/historial/facturas/ver', code = 302)


@router.route('/historial/eliminar')
def eliminar_historial():
    retencion = RetencionDaoControl()
    retencion.clear_all_retenciones()
    return redirect('/historial', code=302)


@router.route('/historial/generar')
def generar_retenciones():
    retencion = RetencionDaoControl()
    factura = FacturaDaoControl()
    factura.load_facturas()
    retencion.process_facturas(factura)
    return redirect('/historial', code=302)

@router.route('/facturas/modificar', methods=['POST'], )
def modificar_personas():
    fd = FacturaDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = fd._list().get(int(pos)-1)
    #if not "ausuar" in data.keys():
    #    abort(400)            
    #Todo..validar
    fd._factura = nene
    fd._factura._usuario = data['usuario']
    fd._factura._fecha = data['fecha']
    fd._factura._monto = data['monto']
    fd._factura._tipoRUC = data['tipoRUC']
    fd._factura._RUC = data['RUC']
    #pd._persona._tipoIdentificacion = data['tipo']
    fd.merge(int(pos))
    return redirect("/historial/facturas/ver", code=302)

#ordenar facturas
@router.route('/historial/ordenar')
def ordenar_historial():
    campo_orden = request.args.get('campo', default='_fecha', type=str)
    direccion = request.args.get('direccion', default=1, type=int)
    factura = FacturaDaoControl()
    linked_list = factura._list().sort_models(campo_orden, direccion)
    lista_ordenada = linked_list.toArray
    return render_template('factura/ordenar.html', lista = lista_ordenada)

#buscar facturas
@router.route('/historial/buscar', methods=['GET', 'POST'])
def buscar_factura():
    if request.method == 'POST':
        data = request.form
        campo = data['select-campo'] #request.form.get('select-campo')
        valor = data['input-campo']
        if campo == '_monto':
            valor = float(valor)
        fact = FacturaDaoControl()
        if campo == '_RUC':
            facturas1 = fact._list().binary_search_models(valor, campo)
        else:
            facturas1 = fact._list().binary_models(valor, campo)
        if facturas1 is not None and facturas1._length > 0:
            mensaje = f'Facturas correspondientes a "{valor}":'
        else:
            if campo == '_monto':
                mensaje = f'No se ha encontrado facturas con el monto de "{valor}"'
            elif campo == '_fecha':
                mensaje = f'No se ha encontrado facturas con la fecha de "{valor}"'
            else:
                mensaje = f'No se ha encontrado facturas con el usuario "{valor}"'
                
        return render_template('factura/buscar.html', facturas = facturas1, code=302, mensaje = mensaje)
    else:
        return render_template('factura/buscar.html')