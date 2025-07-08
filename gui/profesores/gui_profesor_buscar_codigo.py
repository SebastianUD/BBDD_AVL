import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_codigo(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Profesor por Código")
    ventana.geometry("500x420")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar profesor por código exacto",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ingrese el código del profesor", width=320)
    entrada_codigo.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=440, height=150, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        codigo = entrada_codigo.get().strip()
        if not codigo.isdigit():
            messagebox.showerror("Error", "El código debe ser un número.")
            return

        profesor = gestor.arbol.buscar_por_codigo(int(codigo))
        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if profesor:
            resultado.insert("end", f"[ENCONTRADO] Profesor con código = {codigo}:\n")
            resultado.insert("end", f"- Código: {profesor.codigo}, Nombre: {profesor.nombre}, Correo: {profesor.correo}, Vinculación: {profesor.vinculacion}")
        else:
            resultado.insert("end", f"[NO ENCONTRADO] No existe profesor con código = {codigo}")

        resultado.configure(state="disabled")

    ctk.CTkButton(
        ventana, text="Buscar", command=buscar,
        font=("Segoe UI", 13), width=200, height=35
    ).pack(pady=5)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana, gestor),
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack(pady=5)

def volver(ventana, gestor):
    ventana.destroy()
    from gui.profesores.gui_profesor_buscar import abrir_busqueda_por_campo_profesor
    abrir_busqueda_por_campo_profesor(gestor)
