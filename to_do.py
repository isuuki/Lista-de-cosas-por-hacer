import json
import os

FILE = "tareas.json"

def cargar_tareas():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(FILE, "w") as f:
        json.dump(tareas, f, indent=4)

def mostrar_tareas(tareas):
    if not tareas:
        print("\n✅ No tienes tareas pendientes.")
        return
    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i}. [{estado}] {tarea['nombre']}")

def agregar_tarea(tareas):
    nombre = input("\n👉 Ingresa el nombre de la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    guardar_tareas(tareas)
    print("✅ Tarea agregada.")

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("\nNúmero de tarea a completar: ")) - 1
        tareas[num]["completada"] = True
        guardar_tareas(tareas)
        print("✔ Tarea completada.")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        num = int(input("\nNúmero de tarea a eliminar: ")) - 1
        tarea = tareas.pop(num)
        guardar_tareas(tareas)
        print(f"🗑 Tarea '{tarea['nombre']}' eliminada.")
    except (ValueError, IndexError):
        print("❌ Número inválido.")

def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
