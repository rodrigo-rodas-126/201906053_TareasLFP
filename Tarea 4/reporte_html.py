import json
import webbrowser

nombres = []
edades = []
estados = []
saldos = []

lista = [
        {'nombre': 'Maldini', 'edad': 23, 'activo': True, 'saldo': 61.9}, 
        {'nombre': 'Sambueza', 'edad': 24, 'activo': False, 'saldo': 41.1}, 
        {'nombre': 'Juancho', 'edad': 21, 'activo': False, 'saldo': 91.2}, 
        {'nombre': 'Messi', 'edad': 29, 'activo': True, 'saldo': 123.0}, 
        {'nombre': 'Cristiano', 'edad': 28, 'activo': False, 'saldo': 89.1}, 
        {'nombre': 'Kante', 'edad': 24, 'activo': True, 'saldo': 12.1}, 
        {'nombre': 'Manolo', 'edad': 22, 'activo': False, 'saldo': 9.0}, 
        {'nombre': 'Ramos', 'edad': 19, 'activo': False, 'saldo': 45.23}, 
        {'nombre': 'Luis', 'edad': 26, 'activo': False, 'saldo': 100.23}, 
        {'nombre': 'Pedro', 'edad': 25, 'activo': True, 'saldo': 76.0}
        ]

N = 0
N = lista.__len__()

def datos_edades():
    for e in lista:
        ename = e["edad"]
        edades.append(ename)
    

def datos_saldos():
    for e in lista:
        ename = e["saldo"]
        saldos.append(ename)
    

def datos_nombres():
    for e in lista:
        ename = e["nombre"]
        nombres.append(ename)
    

def datos_estados():
    for e in lista:
        ename = e["activo"]
        estados.append(ename)


datos_edades()
datos_estados()
datos_nombres()
datos_saldos()

with open('reporte.html', 'w') as reporte:
    reporte.write('<html>')
    reporte.write('<head>')
    reporte.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
    reporte.write('<body>')
    reporte.write('<center>')

    reporte.write('<table class="table table-hover">')

    reporte.write('<thead>')
    reporte.write('<tr>')
    reporte.write('<th scope="col">No.</th>')
    reporte.write('<th scope="col">Nombre</th>')
    reporte.write('<th scope="col">Edad</th>')
    reporte.write('<th scope="col">Activo</th>')
    reporte.write('<th scope="col">Saldo</th>')
    reporte.write('</tr>')
    reporte.write('</thead>')

    reporte.write('<tbody>')

    for ie in range(N):
        valor = str(ie)
        reporte.write('<tr>')
        reporte.write('<th>' + str(ie + 1) + '</th>')
        reporte.write('<td class="active">' + str(nombres[ie]) + '</td>')
        reporte.write('<td class="success">' + str(edades[ie]) + '</td>')
        reporte.write('<td class="warning">' + str(estados[ie]) + '</td>')
        reporte.write('<td class="danger">' + str(saldos[ie]) + '</td>')
        reporte.write('</tr>')

    reporte.write('</tbody>')

    reporte.write('</table>')
    reporte.write('</center>')
    reporte.write('</body>')
    reporte.write('</html>')

    webbrowser.open('reporte.html')

