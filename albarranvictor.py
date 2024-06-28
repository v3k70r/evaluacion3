import pandas as pd
import numpy as np
import statistics

#Método que genera una lista de clientes con nombres y saldo aleatorios
def generar_clientes():
    nombres = pd.read_csv("nombres.csv", header=None, names=["nombre"])
    clientes = []
    i = 9
    while i >= 0:
        nombre_azar = np.random.choice(nombres['nombre'])
        saldo_azar = np.random.randint(1000, 10000000)
        cliente_actual = {"nombre": nombre_azar, "saldo": saldo_azar}
        clientes.append(cliente_actual)
        i -= 1
    return clientes

def mostrar_clientes(clientes):
    i = 0
    while(i < len(clientes)):
        print(f"cliente {i+1}. Nombre: {clientes[i]['nombre']}. Saldo: ${clientes[i]['saldo']}")
        i += 1

def mostrar_tramos(clientes):
    print("Acontinuación se le muestra la lista de clientes segmentada en tres tramos. Tramo 1, donde aparecen clientes con saldo menor que 3 millones, tramo 2 de clientes con saldo entre 3 millones y 7 millones y tramo 3 con clientes con saldo mayor a 7 millones.")
    i = 0
    print("TRAMO 1:")
    while(i < len(clientes)):
        if(clientes[i]['saldo'] < 3000000):
            print(f"cliente {i+1}. Nombre: {clientes[i]['nombre']}. Saldo: ${clientes[i]['saldo']}")
        i += 1
    print("TRAMO 2:")
    i = 0
    while(i < len(clientes)):
        if(clientes[i]['saldo'] >= 3000000 and clientes[i]['saldo'] <= 7000000):
            print(f"cliente {i+1}. Nombre: {clientes[i]['nombre']}. Saldo: ${clientes[i]['saldo']}")
        i += 1
    print("TRAMO 3:")
    i = 0
    while(i < len(clientes)):
        if(clientes[i]['saldo'] > 7000000):
            print(f"cliente {i+1}. Nombre: {clientes[i]['nombre']}. Saldo: ${clientes[i]['saldo']}")
        i += 1
def estadisticas(clientes):
    cliente_con_mayor_saldo = max(clientes, key=lambda x: x['saldo'])
    cliente_con_menor_saldo = min(clientes, key=lambda x: x['saldo'])
    print(f"El cliente con el mayor saldo es: {cliente_con_mayor_saldo['nombre']} con un saldo de ${cliente_con_mayor_saldo['saldo']}")
    print(f"El cliente con el menor saldo es: {cliente_con_menor_saldo['nombre']} con un saldo de ${cliente_con_menor_saldo['saldo']}")
    saldos = [cliente['saldo'] for cliente in clientes]
    promedio_saldos = statistics.mean(saldos)
    media_geometrica_saldos = statistics.geometric_mean(saldos)
    print(f"El saldo promedio es:{promedio_saldos:.3f}")
    print(f"La media geométrica de los saldos es: {media_geometrica_saldos:.3f}")

def variacion(clientes, variacion):
    clientes2 = []
    i = 0
    clientes2.append({"nombre": "--Saldos netos--", "saldo": 0})
    while(i < len(clientes)):
        cliente_actual = {"nombre": clientes[i]['nombre'], "saldo": (clientes[i]['saldo'] + clientes[i]['saldo'] * (variacion/100))}
        clientes2.append(cliente_actual)
        i += 1
    return clientes2

def generar_csv(clientes):
    df_clientes = pd.DataFrame(clientes)
    df_clientes2 = pd.DataFrame(variacion(clientes, 3))
    saldos = [cliente['saldo'] for cliente in clientes]
    cliente_con_mayor_saldo = max(clientes, key=lambda x: x['saldo'])
    cliente_con_menor_saldo = min(clientes, key=lambda x: x['saldo'])
    promedio_saldos = statistics.mean(saldos)
    media_geometrica_saldos = statistics.geometric_mean(saldos)
    media_geometrica_redondeada = round(media_geometrica_saldos, 2)
    data = {
        "1": ["Mayor Saldo", "Menor Saldo", "Promedio Saldo", "Media Geométrica"],
        "2": [cliente_con_mayor_saldo['nombre'], cliente_con_menor_saldo['nombre'], "", ""],
        "3": [cliente_con_mayor_saldo['saldo'], cliente_con_menor_saldo['saldo'], promedio_saldos, media_geometrica_redondeada]
    }
    df_estadisticas = pd.DataFrame(data)

    df_combinado = pd.concat([df_clientes, df_clientes2, df_estadisticas], ignore_index=True, sort=False)
    df_combinado.to_csv("clientes_y_estadisticas.csv", index=False)
    print("La información ha sido guardada en 'clientes_y_estadisticas.csv'.")
def menu():
    clientes = generar_clientes()
    opcion = -1
    while opcion != 5:
        print("Las opciones a operar son: \n1)Ver lista de clientes. \n2)Ver clientes clasificados según tramo. \n3)Ver estadísticas generales. \n4)Generar Reporte csv. \n5)Salir.")
        opcion = int(input("Ingrese opción: "))
        if(opcion == 1):
            mostrar_clientes(clientes)
            print("Los saldos este mes como en un deposito a plazo han tenido una variación de +3%. A continuación se muestra la lista con los SALDOS NETOS finales.")
            mostrar_clientes(variacion(clientes, 3))
        elif(opcion == 2):
            mostrar_tramos(clientes)
        elif(opcion == 3):
            estadisticas(clientes)
        elif(opcion == 4):
            generar_csv(clientes)
        elif(opcion == 5):
            print("Programa finalizado, adiós.")
        else:
            print("Opción no válida. Intente nuevamente.")
        print("\n------------------------------------------------------\n")
def main():
    menu()
main()
