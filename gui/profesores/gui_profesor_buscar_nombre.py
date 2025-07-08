import customtkinter as ctk
from tkinter import messagebox

def mostrar_busqueda_por_nombre(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Buscar Profesor por Nombre")
    ventana.geometry("520x460")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Buscar profesor por nombre (coincidencia parcial)",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entrada_nombre = ctk.CTkEntry(ventana, placeholder_text="Ej: Ana", width=360)
    entrada_nombre.pack(pady=10)

    resultado = ctk.CTkTextbox(ventana, width=470, height=200, font=("Courier", 11))
    resultado.pack(pady=10)
    resultado.configure(state="disabled")

    def buscar():
        nombre_buscado = entrada_nombre.get().strip().lower()
        if not nombre_buscado:
            messagebox.showerror("Error", "Por favor, ingrese un nombre.")
            return

        profesores = gestor.arbol.inorden_lista()
        encontrados = [
            p for p in profesores if nombre_buscado in p.nombre.lower()
        ]

        resultado.configure(state="normal")
        resultado.delete("1.0", "end")

        if encontrados:
            resultado.insert("end", f"[ENCONTRADOS] {len(encontrados)} profesor(es) con nombre = {nombre_buscado}:\n")
            for p in encontrados:
                resultado.insert(
                    "end",
                    f"- Código: {p.codigo}, Nombre: {p.nombre}, Correo: {p.correo}, Vinculación: {p.vinculacion}\n"
                )
        else:
            resultado.insert("end", f"[NO ENCONTRADO] No hay profesores con nombre = {nombre_buscado}")
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