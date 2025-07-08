import customtkinter as ctk
from gui.gestor_instancias import get_gestor_materias

def mostrar_interfaz_materias():
    ventana = ctk.CTkToplevel()
    ventana.title("Módulo de Materias")
    ventana.geometry("500x520")
    ventana.resizable(False, False)
    ventana.focus()  # Dar foco a la ventana

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="GESTOR DE MATERIAS",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=20)

    # Opciones del menú
    opciones = [
        ("Agregar materia", lambda: abrir_ventana("agregar", ventana)),
        ("Buscar por campo", lambda: abrir_ventana("buscar", ventana)),
        ("Actualizar materia", lambda: abrir_ventana("actualizar", ventana)),
        ("Eliminar materia", lambda: abrir_ventana("eliminar", ventana)),
        ("Mostrar materias en orden ascendente", lambda: abrir_ventana("inorden", ventana)),
        ("Mostrar estructura del árbol AVL", lambda: abrir_ventana("arbol", ventana)),
        ("Volver al menú principal", lambda: volver_al_menu_principal(ventana))
    ]

    for texto, accion in opciones:
        ctk.CTkButton(
            ventana,
            text=texto,
            command=accion,
            font=("Segoe UI", 13, "bold"),
            width=320,
            height=40,
            corner_radius=8
        ).pack(pady=7)

def abrir_ventana(opcion, ventana_actual):
    ventana_actual.destroy()  # Cierra la ventana actual
    gestor = get_gestor_materias()

    if opcion == "agregar":
        from gui.materias.gui_materia_agregar import mostrar_formulario_agregar_materia
        mostrar_formulario_agregar_materia(gestor)
    elif opcion == "buscar":
        from gui.materias.gui_materia_buscar import abrir_busqueda_por_campo_materia
        abrir_busqueda_por_campo_materia(gestor)
    elif opcion == "actualizar":
        from gui.materias.gui_materia_actualizar import mostrar_formulario_actualizar_materia
        mostrar_formulario_actualizar_materia(gestor)
    elif opcion == "eliminar":
        from gui.materias.gui_materia_eliminar import mostrar_formulario_eliminar_materia
        mostrar_formulario_eliminar_materia(gestor)
    elif opcion == "inorden":
        from gui.materias.gui_materia_mostrar_inorden import mostrar_materias_inorden
        mostrar_materias_inorden(gestor)
    elif opcion == "arbol":
        from gui.materias.gui_materia_mostrar_arbol import mostrar_arbol_avl_materias
        mostrar_arbol_avl_materias(gestor)

def volver_al_menu_principal(ventana):
    ventana.destroy()
    from main_GUI import mostrar_menu_principal
    mostrar_menu_principal()