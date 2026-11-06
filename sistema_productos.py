import csv

productos = []
archivo = "productos.csv"

def mostrar_productos(lista):
    if not lista:
        print("\n[!] No hay productos cargados.")
        return
    print("\n=== LISTA DE PRODUCTOS ===")
    for p in lista:
        estado = "Activo" if p['activo'] else "Inactivo"
        print(f"ID: {p['id']} | {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']} | Estado: {estado}")

def agregar_producto(lista):
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("[!] El nombre no puede estar vacío.")
            return
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        activo = True
        
        nuevo_id = max([p['id'] for p in lista], default=0) + 1
        
        nuevo = {
            "id": nuevo_id,
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "activo": activo
        }
        lista.append(nuevo)
        print(f"[+] Producto '{nombre}' agregado con éxito.")
    except ValueError:
        print("[!] Error: El precio debe ser un número decimal y el stock un entero.")

def modificar_stock(lista):
    print("\n--- MODIFICAR STOCK ---")
    if not lista:
        print("[!] No hay productos para modificar.")
        return
    mostrar_productos(lista)
    try:
        id_prod = int(input("Ingrese el ID del producto a modificar: "))
        for p in lista:
            if p["id"] == id_prod:
                nuevo_stock = int(input(f"Nuevo stock para '{p['nombre']}': "))
                p["stock"] = nuevo_stock
                print("[*] Stock actualizado correctamente.")
                return
        print("[!] Producto no encontrado.")
    except ValueError:
        print("[!] Error: Ingrese valores numéricos válidos.")

def eliminar_producto(lista):
    print("\n--- ELIMINAR PRODUCTO (BAJA LÓGICA) ---")
    if not lista:
        print("[!] No hay productos para dar de baja.")
        return
    mostrar_productos(lista)
    try:
        id_prod = int(input("Ingrese el ID del producto a eliminar: "))
        for p in lista:
            if p["id"] == id_prod:
                if not p["activo"]:
                    print("[!] Este producto ya se encuentra inactivo.")
                    return
                p["activo"] = False
                print(f"[-] Producto '{p['nombre']}' dado de baja correctamente.")
                return
        print("[!] Producto no encontrado.")
    except ValueError:
        print("[!] Error: ID inválido.")

def guardar_productos(lista, archivo):
    try:
        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            campos = ["id", "nombre", "precio", "stock", "activo"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(lista)
    except Exception as e:
        print(f"[!] Error al guardar el archivo: {e}")

def leer_productos(archivo):
    try:
        with open(archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            productos_leidos = list(reader)
            
            for p in productos_leidos:
                p["id"] = int(p["id"])
                p["precio"] = float(p["precio"])
                p["stock"] = int(p["stock"])
                p["activo"] = p["activo"].lower() == "true"
            return productos_leidos
    except FileNotFoundError:
        return []

def menu():
    print("\n================================")
    print("  SISTEMA DE GESTIÓN (CRUD)  ")
    print("================================")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Modificar stock")
    print("4. Eliminar producto")
    print("5. Guardar y salir")

def main():
    global productos
    productos = leer_productos(archivo)
    while True:
        menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            modificar_stock(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            guardar_productos(productos, archivo)
            print("\n[+] Datos guardados en 'productos.csv'. Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("[!] Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
