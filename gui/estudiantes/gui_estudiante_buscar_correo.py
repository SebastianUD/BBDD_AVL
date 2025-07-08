import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_correo(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Estudiante por Correo")
    ventana.geometry("600x500")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Buscar estudiante por correo",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=25)

    entrada_correo = ctk.CTkEntry(ventana, width=350)
    entrada_correo.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=520, height=240, font=("Segoe UI", 12))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        correo_input = entrada_correo.get().strip().lower()
        if not correo_input:
            messagebox.showwarning("Campo vacío", "Por favor ingresa un correo para buscar.")
            return

        coincidencias = []
        estudiantes = gestor.arbol.inorden_lista()

        for estudiante in estudiantes:
            if correo_input in estudiante.correo.lower():
                coincidencias.append(estudiante)

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if coincidencias:
            resultado.insert("end", f"[ENCONTRADOS] {len(coincidencias)} estudiante(s) con correo = {correo_input}:\n")
            for e in coincidencias:
                resultado.insert("end", f"- Código: {e.codigo}, Nombre: {e.nombre}, Correo: {e.correo}, Facultad: {e.facultad}, Carrera: {e.carrera}\n")
        else:
            resultado.insert("end", "No se encontraron estudiantes con ese correo.")

        resultado.configure(state="disabled")

    def volver():
        ventana.destroy()
        from gui.estudiantes.gui_estudiante_buscar import abrir_busqueda_por_campo
        abrir_busqueda_por_campo(gestor)

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