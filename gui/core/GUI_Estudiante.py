import customtkinter as ctk
from tkinter import messagebox
from gui.gestor_instancias import get_gestor_estudiantes

# Configuración global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------------- INTERFAZ PRINCIPAL DE ESTUDIANTES ----------------------
def mostrar_interfaz_estudiantes():
    ventana = ctk.CTkToplevel()
    ventana.title("Módulo de Estudiantes")
    ventana.geometry("500x550")
    ventana.resizable(False, False)
    ventana.focus()  # Dar foco a la ventana

    ctk.CTkLabel(
        ventana,
        text="GESTOR DE ESTUDIANTES",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=25)

    opciones = [
        ("Agregar estudiante", lambda: mostrar_formulario_agregar(ventana)),
        ("Buscar por campo", lambda: mostrar_busqueda_por_campo(ventana)),
        ("Actualizar estudiante", lambda: mostrar_formulario_actualizar(ventana)),
        ("Eliminar estudiante", lambda: mostrar_formulario_eliminar(ventana)),
        ("Mostrar estudiantes en orden ascendente", lambda: mostrar_inorden(ventana)),
        ("Mostrar estructura del árbol AVL", lambda: mostrar_arbol(ventana)),
        ("Volver al menú principal", lambda: volver_al_menu_principal(ventana))
    ]

    for texto, accion in opciones:
        ctk.CTkButton(
            ventana,
            text=texto,
            command=accion,
            font=("Segoe UI", 14, "bold"),
            width=300,
            height=40,
            corner_radius=10
        ).pack(pady=10)

# ---------------------- FUNCIONES DE SUBMENÚ ----------------------

def mostrar_formulario_agregar(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_agregar import mostrar_formulario_agregar_estudiante
    mostrar_formulario_agregar_estudiante(get_gestor_estudiantes())

def mostrar_busqueda_por_campo(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_buscar import abrir_busqueda_por_campo
    abrir_busqueda_por_campo(get_gestor_estudiantes())

def mostrar_formulario_actualizar(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_actualizar import abrir_formulario_actualizar
    abrir_formulario_actualizar(get_gestor_estudiantes())

def mostrar_formulario_eliminar(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_eliminar import abrir_formulario_eliminar
    abrir_formulario_eliminar(get_gestor_estudiantes())

def mostrar_inorden(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_mostrarLista import mostrar_estudiantes_inorden
    mostrar_estudiantes_inorden(get_gestor_estudiantes())

def mostrar_arbol(ventana_actual):
    ventana_actual.destroy()
    from gui.estudiantes.gui_estudiante_mostrarArbol import mostrar_arbol_avl
    mostrar_arbol_avl(get_gestor_estudiantes())

def volver_al_menu_principal(ventana_actual):
    ventana_actual.destroy()
    from main_GUI import mostrar_menu_principal
    mostrar_menu_principal()