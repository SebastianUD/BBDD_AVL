import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_codigo(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Estudiante por Código")
    ventana.geometry("500x420")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Buscar estudiante por código",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=25)

    entrada_codigo = ctk.CTkEntry(ventana, width=300)
    entrada_codigo.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=420, height=160, font=("Segoe UI", 12))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        codigo_str = entrada_codigo.get().strip()
        if not codigo_str.isdigit():
            messagebox.showerror("Error", "El código debe ser un número.")
            return

        codigo = int(codigo_str)
        estudiante = gestor.buscar_por_codigo(codigo)

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if estudiante:
            resultado.insert("end", f"""
Código: {estudiante.codigo}
Nombre: {estudiante.nombre}
Correo: {estudiante.correo}
Facultad: {estudiante.facultad}
Carrera: {estudiante.carrera}
""")
        else:
            resultado.insert("end", "No se encontró ningún estudiante con ese código.")

        resultado.configure(state="disabled")

    def volver():
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar import abrir_busqueda_por_campo
        abrir_busqueda_por_campo(gestor)

    # Botones
    ctk.CTkButton(
        ventana,
        text="Buscar",
        command=buscar,
        font=("Segoe UI", 13),
        width=150,
        height=35,
        corner_radius=8
    ).pack(pady=5)

    ctk.CTkButton(
        ventana,
        text="Volver",
        command=volver,
        font=("Segoe UI", 13),
        fg_color="#e67e22",
        hover_color="#d35400",
        width=150,
        height=35,
        corner_radius=8
    ).pack(pady=10)