from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientesForm
from .forms import ProveedoresForm
from .models import Clientes
from django.forms import ModelForm
from django.views.generic import ListView
from django.http import HttpResponse
import json
import datetime

# Create your views here.

def inicio(request):
    return render(request, "../templates/index.html")

def buscar(listClientes, busqueda):
	for c in listClientes:
		if busqueda in c[0].nombre.lower():
			c.idcliente
		else:
			print("No existe")
	return c.idcliente

def nueva_venta(request):
	template = "../templates/nueva_venta.html"

	search_term = ''
	search_term_1 = ''
	productos = ''
	cliente = ''

#	clientes2 = list()
#	cliente = Clientes.objects.all()
#
#	for cl in cliente:
#		clientes2.append(cl.nombre)

	#productos = Productos.objects.all()
	if 'search' in request.GET:
		search_term = request.GET['search']
		productos = Productos.objects.filter(nombre__icontains=search_term)

	if 'search_client' in request.GET:
		search_term = request.GET['search_client']
		cliente = Clientes.objects.filter(nombre__icontains=search_term_1)

	if request.method == 'POST':
		fecha = request.POST.get("fecha")
		codigo = request.POST.get("codigo")
		concepto = request.POST.get("concepto")
		vencimiento = request.POST.get("vencimiento")
		total = request.POST.get("total")
		exenta = request.POST.get("exenta")
		descuento = request.POST.get("descuento")
		anulado = request.POST.get("anulado")
		impreso = request.POST.get("impreso")
		cantidad = request.POST.get("cantidad")
		precio = request.POST.get("precio")
		descripcion = request.POST.get("descripcionproducto")
		#buscando = request.POST.get("cliente_info")
		#search = buscando.lower()
		#idcliente = buscar(clientes2, search)
		'''
		cf = True if request.POST.get("credito_fiscal") else False
		if cf:
			idfactncred = idfactura
			# idtdoc = 1
		else:
			idfactncred = idfactura
			# idtdoc = 2
		'''
		# detallefactura = Detallefacturas(cantidad=cantidad, precio=precio, subtotal=subtotal, descuento=descuento,
		#	idfactura=idfactura, idproducto=idproducto, idbodega=idbodega)

		'''
		fatura = Facturas(codigo=codigo, fecha=fecha, concepto=concepto, vencimiento=vencimiento,
				total=total, exenta=exenta, descuento=descuento, anulado=anulado, impreso=impreso,
				idtdoc=idtdoc, idcliente=idcliente, idfactncred=idfactncred)
		factura.save()

		movimiento = Movimiento(fecha=fecha, costomovimiento=costomovimiento, costopromedio=costopromedio,
			concepto=concepto, responsable=responsable, cantidad=cantidad, bodega1=bodega1, bodega2=bodega2,
			codproducto=codproducto, tmov=tmov, idfactura=idfactura, idtdoctransferencia=idtdoctransferencia,
			idlibcom=idlibcom)
		movimiento.save()

		producto = Producto(codigoprod=codigoprod, nombre=nombre, descripcion=descripcion, marca=marca,
			existenciamax=existenciamax, existenciamin=existenciamin, existenciaactual=existenciaactual,
			idcategoria=idcategoria, idbodega=idbodega)
		producto.save()
		'''

	'''

	movimiento = Movimientos(fecha=fecha, costomovimiento=costomovimiento, costopromedio=costopromedio,
		concepto=concepto, responsable=responsable, cantidad=cantidad, bodega1=bodega1, bodega2=bodega2,
		codproducto=codproducto, tmov=tmov, idfactura=idfactura, idtdoctransferencia=idtdoctransferencia,
		idlibcom=idlibcom)
	movimiento.save()

	producto = Prodcutos(codigoprod=codigoprod, nombre=nombre, descripcion=descripcionproducto, marca=marcaproducto,
		existenciamax=existenciamax, existenciamin=existenciamin, idcategoria=idcategoria, idbodega=idbodega)
	producto.save()
	'''

	context = {
		'search_term':search_term, 'productos':productos, 'cliente': cliente,
	}

	return render(request, template, context)

def buscar_prod(listProductos, busqueda):
	for p in listProductos:
		if busqueda in p.codigoprod.lower():
			p.codigoprod
		else:
			p.codigoprod = 0
	return p.codigoprod

def listarproductos(listp, busqueda):
	seleccionados = list()
	for p in listp:
		if p.codigoprod == busqueda:
			seleccionados.append(p)
	return seleccionados

def prueba(request):
	template = "../templates/busqueda.html"
	'''
	products = list()
	productos = Productos.objects.all()
	for p in productos:
		products.append(p)
	if request.method == 'POST':
		cprod = request.POST.get("codprod")
		search = cprod.lower()
		cod = buscar_prod(products, search)
		print (cod)


	if request.method == 'POST':
		buscar = request.POST.get("codprod")
		prods = Productos.objects.filter(codigoprod=buscar)
		print (prods)

	prods = list()
	productos = Productos.objects.all()
	for pr in productos:
		prods.append(pr)
	if request.method == 'POST':
		nameprod = request.POST.get("codprod")
		search = nameprod.lower()
		idprodname = buscar_prod(prods, search)
		print(idprodname)
	'''

	return render(request, template)

def nueva_compra(request):
	return render(request, "../templates/nueva_compra.html")

def modificar_factura(request):
	return render(request, "../templates/nueva_venta.html")

def modificar_compra(request):
	return render(request, "../templates/nueva_compra.html")

def listar_facturas(request):
	return render(request, "../templates/listar_facturas.html")

def new_product(request):
    template = "../templates/Cproducts.html"

    categorias = list()
    cates = Categorias.objects.all()
    for c in cates:
        categorias.append(c)

    bodegas = list()
    cellars = Bodegas.objects.all()
    for b in cellars:
        bodegas.append(b)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        bodega = Bodegas.objects.get(idbodega=request.POST.get('bodega'))
        categoria = Categorias.objects.get(idcategoria=request.POST.get('categoria'))
        maxima = request.POST.get('maxima')
        minima = request.POST.get('minima')
        actual = request.POST.get('actual')
        product = Productos(codigoprod=codigo, nombre=nombre, descripcion=descripcion, marca=marca,
                            existenciamax=maxima, existenciamin=minima, existenciaactual=actual,
                            idcategoria=categoria, idbodega=bodega)
        product.save()

    context = {
        'categorias': categorias,
        'bodegas': bodegas,
    }
    return render(request, template, context)

def new_categoria(request):
    template = "../templates/Ccategoria.html"

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        categoria = Categorias(nombre=nombre, codigo=codigo, descripcion=descripcion)
        categoria.save()

    context = {}
    return render(request, template, context)

def new_bodega(request):
    template = "../templates/CBodega.html"

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        bodega = Bodegas(nombre=nombre, descripcion=descripcion)
        bodega.save()

    context = {}
    return render(request, template, context)


    return render(request, "../templates/products.html")

def clientes_list(request, template_name='../templates/clientes_list.html'):
    clientes = Clientes.objects.all()
    data = {}
    data['object_list'] = clientes
    return render(request, template_name, data)

def clientes_create(request, template_name='../templates/clientes_form.html'):
    form = ClientesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes_list.html')
    return render(request, template_name, {'form': form})

def clientes_update(request, pk, template_name='../templates/clientes_form.html'):
    clientes = get_object_or_404(Clientes, pk=pk)
    form = ClientesForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
    return render(request, template_name, {'form': form})

def clientes_delete(request, pk, template_name='../templates/clientes_delete.html'):
    clientes = get_object_or_404(Clientes, pk=pk)
    if request.method=='POST':
        clientes.delete()
        return redirect('clientes_list.html')
    return render(request, template_name, {'object': clientes})

def proveedores_list(request, template_name='../templates/proveedores_list.html'):
    proveedores = Proveedores.objects.all()
    data = {}
    data['object_list'] = proveedores
    return render(request, template_name, data)

def proveedores_create(request, template_name='../templates/proveedores_form.html'):
    form = ProveedoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('proveedores_list.html')
    return render(request, template_name, {'form': form})

def proveedores_update(request, pk, template_name='../templates/proveedores_form.html'):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    form = ProveedoresForm(request.POST or None, instance=proveedores)
    if form.is_valid():
        form.save()
        return redirect('proveedores_list')
    return render(request, template_name, {'form': form})

def proveedores_delete(request, pk, template_name='../templates/proveedores_delete.html'):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    if request.method=='POST':
        proveedores.delete()
        return redirect('proveedores_list')
    return render(request, template_name, {'object': proveedores})

class BodegasList(ListView):
    model = Bodegas
    template_name = "../templates/bodegaslist.html"

class CategoriasList(ListView):
    model = Categorias
    template_name = "../templates/categorialist.html"

class ProductosList(ListView):
    model = Productos
    template_name = "../templates/productlist.html"

def busqueda(request):
  usuario = {'nombre': 'Eduardo Ismael'}
  return HttpResponse( json.dumps(usuario), content_type='application/json' )

def reporte_ventas(request):
    template = "../templates/reporte_ventas.html"
    fecha1 = DateRangeForm()
    fecha2 =DateRangeForm()
    context = {
    'form': fecha1,
    'form': fecha2,
    }
    return render(request, template, context)

def getVentas(request):
    template = "../templates/reporte_ventas.html"
    if request.method == 'POST':
		
        f1 = datetime.datetime.strptime((request.POST.get("start_date")), '%b %d, %Y')
        f2 = datetime.datetime.strptime((request.POST.get("end_date")), '%b %d, %Y')

    ventas = Libroventascf.objects.filter(fecha__range=(f1, f2))
    context = {'ventas':ventas}
    return render(request, template, context)

def reporte_facturas(request):
    template = "../templates/reporte_facturas.html"
    fecha1 = DateRangeForm()
    fecha2 =DateRangeForm()
    context = {
    'form': fecha1,
    'form': fecha2,
    }
    return render(request, template, context)

def getFacturas(request):
    template = "../templates/reporte_facturas.html"
    fecha1 = DateRangeForm()
    fecha2 =DateRangeForm()
    if request.method == 'POST':
        f1 = datetime.datetime.strptime((request.POST.get("start_date")), '%b %d, %Y')
        f2 = datetime.datetime.strptime((request.POST.get("end_date")), '%b %d, %Y')
    facturas = Facturas.objects.filter(fecha__range=(f1, f2))

    context = {'facturas':facturas,
    'form': fecha1,
    'form': fecha2,}
    return render(request, template, context)