from iqoptionapi.stable_api import IQ_Option
from colorama import Fore, Back, Style
from tabulate import tabulate

# Inicializar la API
error_password = """{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""

#cambia El Email por tu Email de iq option y tu contraseña de iq option
iqoption = IQ_Option("Email", "Contraseña")
check, reason = iqoption.connect()

if check:
    # Obtener los activos disponibles
    activos = iqoption.get_all_open_time()  # Devuelve un diccionario con el estado de los activos

    # Crear lista para la tabla
    tabla_activos = []

    for tipo, datos in activos.items():
        for activo, info in datos.items():
            estado = "Disponible" if info["open"] else "No disponible"
            color = Back.GREEN if info["open"] else Back.RED
            tabla_activos.append([activo, tipo, f"{color}{estado}{Style.RESET_ALL}"])

    # Mostrar la tabla
    print(tabulate(tabla_activos, headers=["Activo", "Tipo", "Estado"], tablefmt="fancy_grid"))

else:
    if reason == "[Errno -2] Name or service not known":
        print("No Network")
    elif reason == error_password:
        print("Error Password")
