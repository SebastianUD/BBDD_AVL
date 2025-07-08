import customtkinter as ctk
from tkinter import messagebox
from Profesor import Profesor

def mostrar_formulario_eliminar_profesor(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Eliminar Profesor")
    ventana.geometry("460x300")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Eliminar Profesor por Código",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    ctk.CTkLabel(ventana, text="Ingrese el código del profesor a eliminar:",
                 font=("Segoe UI", 12), text_color="white").pack(pady=5)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ej: 1001", width=300)
    entrada_codigo.pack(pady=10)

    def eliminar():
        try:
            codigo = int(entrada_codigo.get())
            profesor = gestor.buscar_por_codigo(codigo)

            if not profesor:
                messagebox.showwarning("No encontrado", f"No existe profesor con código {codigo}")
                return

            confirmar = messagebox.askyesno("Confirmación", f"¿Seguro que deseas eliminar al profesor {profesor.nombre}?")
            if confirmar:
                gestor.eliminar_entidad(codigo)
                messagebox.showinfo("Éxito", "Profesor eliminado correctamente.")
                ventana.destroy()
                from GUI_Profesor import mostrar_interfaz_profesores
                mostrar_interfaz_profesores()

        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")

    ctk.CTkButton(
        ventana, text="Eliminar", command=eliminar,
        font=("Segoe UI", 13), width=220, height=35
    ).pack(pady=15)

    ctk.CTkButton(
        ventana, text="Volver",
        command=lambda: volver(ventana),
        font=("Segoe UI", 13), width=220, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack(pady=5)

def volver(ventana):
    ventana.destroy()
    from GUI_Profesor import mostrar_interfaz_profesores
    mostrar_interfaz_profesores()