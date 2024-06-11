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