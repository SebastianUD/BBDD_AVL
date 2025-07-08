import customtkinter as ctk
from gui.gestor_instancias import get_gestor_profesores

def mostrar_interfaz_profesores():
    ventana = ctk.CTkToplevel()
    ventana.title("Gestor de Profesores")
    ventana.geometry("520x540")
    ventana.resizable(False, False)
    ventana.focus()  # Dar foco a la ventana

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    gestor = get_gestor_profesores()

    ctk.CTkLabel(
        ventana, text="GESTOR DE PROFESORES",
        font=("Segoe UI", 18, "bold"), text_color="white"
    ).pack(pady=25)

    opciones = [
        ("Agregar profesor", lambda: abrir_ventana("agregar", ventana, gestor)),
        ("Buscar por campo", lambda: abrir_ventana("buscar", ventana, gestor)),
        ("Actualizar profesor", lambda: abrir_ventana("actualizar", ventana, gestor)),
        ("Eliminar profesor", lambda: abrir_ventana("eliminar", ventana, gestor)),
        ("Mostrar profesores en orden ascendente", lambda: abrir_ventana("mostrar", ventana, gestor)),
        ("Mostrar estructura del árbol AVL", lambda: abrir_ventana("arbol", ventana, gestor)),
        ("Volver al menú principal", lambda: volver_al_menu_principal(ventana))
    ]

    for texto, accion in opciones:
        ctk.CTkButton(
            ventana, text=texto, command=accion,
            font=("Segoe UI", 13, "bold"), width=260, height=40, corner_radius=10
        ).pack(pady=6)

def abrir_ventana(tipo, ventana, gestor):
    ventana.destroy()

    if tipo == "agregar":
        from gui.profesores.gui_profesor_agregar import mostrar_formulario_agregar_profesor
        mostrar_formulario_agregar_profesor(gestor)
    elif tipo == "buscar":
        from gui.profesores.gui_profesor_buscar import abrir_busqueda_por_campo_profesor
        abrir_busqueda_por_campo_profesor(gestor)
    elif tipo == "actualizar":
        from gui.profesores.gui_profesor_actualizar import mostrar_formulario_actualizar_profesor
        mostrar_formulario_actualizar_profesor(gestor)
    elif tipo == "eliminar":
        from gui.profesores.gui_profesor_eliminar import mostrar_formulario_eliminar_profesor
        mostrar_formulario_eliminar_profesor(gestor)
    elif tipo == "mostrar":
        from gui.profesores.gui_profesor_mostrar_inorden import mostrar_profesores_inorden
        mostrar_profesores_inorden(gestor)
    elif tipo == "arbol":
        from gui.profesores.gui_profesor_mostrar_arbol import mostrar_arbol_avl_profesores
        mostrar_arbol_avl_profesores(gestor)

def volver_al_menu_principal(ventana):
    ventana.destroy()
    from main_GUI import mostrar_menu_principal
    mostrar_menu_principal()