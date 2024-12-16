import requests
import json
from getpass import getpass  # Para ocultar la entrada del token

# URL base de la API
BASE_URL = 'http://127.0.0.1:8000/api/productos/'

# Función para obtener el token de acceso
def obtener_token():
    print("\nPara acceder al sistema, ingrese su token:")
    token = getpass("Token de acceso: ")  # Esto oculta la entrada del token
    return token  # Retorna el token para ser usado en las solicitudes

# Función para ver todos los productos
def ver_productos():
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(BASE_URL, headers=headers)

    if response.status_code == 200:
        productos = response.json()
        print("\n----- Lista de Productos -----")
        for producto in productos:
            print(f"ID: {producto['id']} - Nombre: {producto['nombre']}")
    else:
        print("Error al obtener los productos:", response.text)

# Función para ver un producto por su ID
def ver_producto_por_id():
    try:
        id_producto = int(input("Ingrese el ID del producto que desea ver: "))
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f'{BASE_URL}{id_producto}/', headers=headers)

        if response.status_code == 200:
            producto = response.json()
            print("\n----- Detalles del Producto -----")
            print(f"ID: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Marca: {producto['marca']}")
            print(f"Cantidad: {producto['cantidad_min']} - {producto['cantidad_max']}")
            print(f"Precio: ${producto['precio']}")
        else:
            print(f"Error al obtener el producto: {response.text}")
    except ValueError:
        print("El ID debe ser un número entero.")

# Función para crear un nuevo producto
def crear_producto():
    token = obtener_token()  # Solicitar el token antes de crear un producto
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    marca = input("Marca del producto: ")
    cantidad_min = int(input("Cantidad mínima: "))
    cantidad_max = int(input("Cantidad máxima: "))
    precio = float(input("Precio del producto: "))

    # Crear un diccionario con los datos del producto
    producto_data = {
        'nombre': nombre,
        'descripcion': descripcion,
        'marca': marca,
        'cantidad_min': cantidad_min,
        'cantidad_max': cantidad_max,
        'precio': precio
    }

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(producto_data))

    if response.status_code == 201:
        print("\nProducto creado con éxito.")
    else:
        print(f"Error al crear el producto: {response.text}")

# Función para actualizar un producto
def actualizar_producto():
    token = obtener_token()  # Solicitar el token antes de actualizar un producto
    try:
        id_producto = int(input("Ingrese el ID del producto que desea actualizar: "))
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

        # Solicitar nuevos datos para el producto
        nombre = input("Nuevo nombre del producto: ")
        descripcion = input("Nueva descripción del producto: ")
        marca = input("Nueva marca del producto: ")
        cantidad_min = int(input("Nueva cantidad mínima: "))
        cantidad_max = int(input("Nueva cantidad máxima: "))
        precio = float(input("Nuevo precio del producto: "))

        producto_data = {
            'nombre': nombre,
            'descripcion': descripcion,
            'marca': marca,
            'cantidad_min': cantidad_min,
            'cantidad_max': cantidad_max,
            'precio': precio
        }

        response = requests.put(f'{BASE_URL}{id_producto}/', headers=headers, data=json.dumps(producto_data))

        if response.status_code == 200:
            print("\nProducto actualizado con éxito.")
        else:
            print(f"Error al actualizar el producto: {response.text}")
    except ValueError:
        print("El ID debe ser un número entero.")

# Función para eliminar un producto
def eliminar_producto():
    token = obtener_token()  # Solicitar el token antes de eliminar un producto
    try:
        id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.delete(f'{BASE_URL}{id_producto}/', headers=headers)

        if response.status_code == 204:
            print("\nProducto eliminado con éxito.")
        else:
            print(f"Error al eliminar el producto: {response.text}")
    except ValueError:
        print("El ID debe ser un número entero.")

# Menú interactivo
def mostrar_menu():
    global token  # Declarar la variable token como global
    token = obtener_token()  # Solicitar el token al inicio para acceder al menú

    while True:
        print("\n----- Menú de Productos -----")
        print("1. Ver todos los productos")
        print("2. Ver un producto por ID")
        print("3. Crear un nuevo producto")
        print("4. Actualizar un producto")
        print("5. Eliminar un producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_productos()
        elif opcion == '2':
            ver_producto_por_id()
        elif opcion == '3':
            crear_producto()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == '__main__':
    mostrar_menu()