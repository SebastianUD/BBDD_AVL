import customtkinter as ctk

def abrir_busqueda_por_campo_materia(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Materia por Campo")
    ventana.geometry("480x420")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar Materia por Campo",
        font=("Segoe UI", 18, "bold"), text_color="white"
    ).pack(pady=20)

    opciones = [
        ("Código", lambda: abrir_sub_busqueda("codigo", gestor, ventana)),
        ("Nombre", lambda: abrir_sub_busqueda("nombre", gestor, ventana)),
        ("Créditos", lambda: abrir_sub_busqueda("creditos", gestor, ventana)),
        ("Horas semanales", lambda: abrir_sub_busqueda("horas_semanales", gestor, ventana)),
    ]

    for texto, accion in opciones:
        ctk.CTkButton(
            ventana, text=texto, command=accion,
            font=("Segoe UI", 13), width=300, height=40, corner_radius=8
        ).pack(pady=6)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver_al_menu_materias(ventana),
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack(pady=20)

def abrir_sub_busqueda(campo, gestor, ventana_actual):
    ventana_actual.destroy()
    if campo == "codigo":
        from gui.materias.gui_materia_buscar_codigo import mostrar_busqueda_codigo_materia
        mostrar_busqueda_codigo_materia(gestor)
    elif campo == "nombre":
        from gui.materias.gui_materia_buscar_nombre import mostrar_busqueda_nombre_materia
        mostrar_busqueda_nombre_materia(gestor)
    elif campo == "creditos":
        from gui.materias.gui_materia_buscar_creditos import mostrar_busqueda_creditos_materia
        mostrar_busqueda_creditos_materia(gestor)
    elif campo == "horas_semanales":
        from gui.materias.gui_materia_buscar_horas import mostrar_busqueda_horas_materia
        mostrar_busqueda_horas_materia(gestor)

def volver_al_menu_materias(ventana):
    ventana.destroy()
    from gui.core.GUI_Materia import mostrar_interfaz_materias
    mostrar_interfaz_materias()