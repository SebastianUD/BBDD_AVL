# gui_profesor_buscar.py
import customtkinter as ctk

def abrir_busqueda_por_campo_profesor(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Profesor por Campo")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar profesor por campo",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    opciones = [
        ("Código", lambda: abrir("codigo", ventana, gestor)),
        ("Nombre", lambda: abrir("nombre", ventana, gestor)),
        ("Correo", lambda: abrir("correo", ventana, gestor)),
        ("Vinculación", lambda: abrir("vinculacion", ventana, gestor)),
        ("Volver", lambda: volver(ventana))
    ]

    for texto, accion in opciones:
        ctk.CTkButton(
            ventana, text=texto, command=accion,
            font=("Segoe UI", 13), width=300, height=40, corner_radius=10
        ).pack(pady=6)

def abrir(tipo, ventana, gestor):
    ventana.destroy()
    if tipo == "codigo":
        from gui_profesor_buscar_codigo import mostrar_busqueda_por_codigo
        mostrar_busqueda_por_codigo(gestor)
    elif tipo == "nombre":
        from gui_profesor_buscar_nombre import mostrar_busqueda_por_nombre
        mostrar_busqueda_por_nombre(gestor)
    elif tipo == "correo":
        from gui_profesor_buscar_correo import mostrar_busqueda_por_correo
        mostrar_busqueda_por_correo(gestor)
    elif tipo == "vinculacion":
        from gui_profesor_buscar_vinculacion import mostrar_busqueda_por_vinculacion
        mostrar_busqueda_por_vinculacion(gestor)

def volver(ventana):
    ventana.destroy()
    from GUI_Profesor import mostrar_interfaz_profesores
    mostrar_interfaz_profesores()