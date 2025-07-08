import customtkinter as ctk
from tkinter import messagebox
from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
from gui.core.GUI_Materia import mostrar_interfaz_materias
from gui.core.GUI_Profesor import mostrar_interfaz_profesores

# --------------------- CONFIGURACIÓN DE TEMA Y APARIENCIA ---------------------
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul

# Variable global para la ventana principal
ventana_principal_global = None

# --------------------- FUNCIÓN PARA ABRIR MÓDULOS ---------------------
def abrir_modulo(nombre, ventana_principal):
    global ventana_principal_global
    ventana_principal_global = ventana_principal
    ventana_principal.withdraw()  # Ocultar en lugar de destruir

    if nombre == "Estudiantes":
        mostrar_interfaz_estudiantes()
    elif nombre == "Profesores":
        mostrar_interfaz_profesores()
    elif nombre == "Materias":
        mostrar_interfaz_materias() 

def mostrar_menu_principal():
    """Función para mostrar el menú principal desde cualquier ventana"""
    global ventana_principal_global
    if ventana_principal_global:
        ventana_principal_global.deiconify()  # Mostrar la ventana oculta
    else:
        iniciar_menu_principal()

def salir_aplicacion():
    """Función para cerrar completamente la aplicación"""
    global ventana_principal_global
    
    try:
        # Cerrar todas las ventanas toplevel abiertas
        import tkinter as tk
        if hasattr(tk, '_default_root') and tk._default_root:
            for child in tk._default_root.winfo_children():
                try:
                    if hasattr(child, 'destroy'):
                        child.destroy()
                except:
                    pass
        
        # Cerrar la ventana principal
        if ventana_principal_global:
            try:
                ventana_principal_global.quit()  # Termina el mainloop
                ventana_principal_global.destroy()  # Destruye la ventana
            except:
                pass
        
        # Destruir la ventana raíz de tkinter si existe
        if hasattr(tk, '_default_root') and tk._default_root:
            try:
                tk._default_root.quit()
                tk._default_root.destroy()
            except:
                pass
                
    except Exception as e:
        print(f"Error al cerrar la aplicación: {e}")
    
    # Forzar salida del programa
    import sys
    sys.exit(0)

# --------------------- CONFIGURACIÓN INICIAL DE LA VENTANA ---------------------
def iniciar_menu_principal():
    global ventana_principal_global
    ventana_principal = ctk.CTk()
    ventana_principal_global = ventana_principal
    ventana_principal.title("Gestor de Base de Datos AVL")
    ventana_principal.geometry("500x480")
    ventana_principal.resizable(False, False)
    
    # Manejar el cierre de ventana con la X
    ventana_principal.protocol("WM_DELETE_WINDOW", salir_aplicacion)

    # --------------------- MENSAJE DE BIENVENIDA ---------------------
    mensaje = ctk.CTkLabel(
        ventana_principal,
        text="\n¡Bienvenido/a al Gestor de Base de Datos AVL!\nSelecciona una entidad para comenzar",
        font=("Segoe UI", 18, "bold"),
        text_color="white",
        justify="center"
    )
    mensaje.pack(pady=40)

    # --------------------- BOTONES DE MÓDULOS ---------------------
    botones = [
        ("Estudiantes", lambda: abrir_modulo("Estudiantes", ventana_principal)),
        ("Profesores", lambda: abrir_modulo("Profesores", ventana_principal)),
        ("Materias", lambda: abrir_modulo("Materias", ventana_principal)),
    ]

    for texto, accion in botones:
        b = ctk.CTkButton(
            ventana_principal,
            text=texto,
            command=accion,
            font=("Segoe UI", 14, "bold"),
            width=200,
            height=40,
            corner_radius=10
        )
        b.pack(pady=10)

    # --------------------- BOTÓN SALIR ---------------------
    boton_salir = ctk.CTkButton(
        ventana_principal,
        text="Salir",
        command=salir_aplicacion,
        font=("Segoe UI", 14, "bold"),
        width=200,
        height=40,
        fg_color="#D9534F",
        hover_color="#C9302C",
        corner_radius=10
    )
    boton_salir.pack(pady=30)

    ventana_principal.mainloop()

# --------------------- EJECUCIÓN PRINCIPAL ---------------------
if __name__ == "__main__":
    iniciar_menu_principal()
