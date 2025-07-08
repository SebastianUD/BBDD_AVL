import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_carrera(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Estudiante por Carrera")
    ventana.geometry("600x500")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Buscar estudiante por carrera",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=25)

    entrada_carrera = ctk.CTkEntry(ventana, width=350)
    entrada_carrera.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=520, height=240, font=("Segoe UI", 12))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        carrera_input = entrada_carrera.get().strip().lower()
        if not carrera_input:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una carrera para buscar.")
            return

        coincidencias = []
        estudiantes = gestor.arbol.inorden_lista()

        for estudiante in estudiantes:
            if carrera_input in estudiante.carrera.lower():
                coincidencias.append(estudiante)

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if coincidencias:
            resultado.insert("end", f"[ENCONTRADOS] {len(coincidencias)} estudiante(s) con carrera = {carrera_input}:\n")
            for e in coincidencias:
                resultado.insert("end", f"- Código: {e.codigo}, Nombre: {e.nombre}, Correo: {e.correo}, Facultad: {e.facultad}, Carrera: {e.carrera}\n")
        else:
            resultado.insert("end", "No se encontraron estudiantes con esa carrera.")

        resultado.configure(state="disabled")

    def volver():
        ventana.destroy()
        from gui_estudiante_buscar import abrir_busqueda_por_campo
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

def volver(ventana):
    ventana.destroy()
    from gui_estudiante_buscar import abrir_busqueda_por_campo
    from Estudiante import Estudiante
    from GestorBDGenerico import GestorBDGenerico
    gestor = GestorBDGenerico("estudiantes.json", Estudiante, "estudiante")
    abrir_busqueda_por_campo(gestor)