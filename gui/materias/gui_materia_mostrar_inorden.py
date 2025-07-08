import customtkinter as ctk

def mostrar_materias_inorden(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Listado de Materias")
    ventana.geometry("600x480")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Materias registradas (orden por código)",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    output = ctk.CTkTextbox(ventana, width=560, height=320, font=("Courier", 11))
    output.pack(pady=10)
    output.configure(state="normal")

    materias = gestor.arbol.inorden_lista()
    if materias:
        texto = "\n".join([f"{m.codigo} - {m.nombre} ({m.creditos} créditos, {m.horas_semana} h/sem)" for m in materias])
        output.insert("end", texto)
    else:
        output.insert("end", "No hay materias registradas.")
    output.configure(state="disabled")

    def volver():
        ventana.destroy()
        from gui.core.GUI_Materia import mostrar_interfaz_materias
        mostrar_interfaz_materias()

    ctk.CTkButton(
        ventana, text="Volver", command=volver,
        font=("Segoe UI", 13), width=180, height=35,
        fg_color="#e67e22", hover_color="#d35400", corner_radius=8
    ).pack(pady=10)