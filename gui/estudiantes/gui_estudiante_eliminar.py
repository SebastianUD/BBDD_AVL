import customtkinter as ctk
from tkinter import messagebox

def abrir_formulario_eliminar(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Eliminar Estudiante")
    ventana.geometry("450x300")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Eliminar estudiante por código",
        font=("Segoe UI", 18, "bold"),
        text_color="white"
    ).pack(pady=30)

    entrada_codigo = ctk.CTkEntry(ventana, placeholder_text="Ingrese el código", width=300)
    entrada_codigo.pack(pady=10)

    def eliminar():
        try:
            codigo = int(entrada_codigo.get().strip())
        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")
            return

        estudiante = gestor.buscar_por_codigo(codigo)
        if not estudiante:
            messagebox.showerror("No encontrado", f"No existe estudiante con código {codigo}.")
            return

        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar al estudiante con código {codigo}?")
        if confirmacion:
            gestor.eliminar_entidad(codigo)
            messagebox.showinfo("Éxito", f"Estudiante con código {codigo} eliminado correctamente.")
            ventana.destroy()
            from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
            mostrar_interfaz_estudiantes()

    def volver():
        ventana.destroy()
        from gui.core.GUI_Estudiante import mostrar_interfaz_estudiantes
        mostrar_interfaz_estudiantes()

    ctk.CTkButton(
        ventana,
        text="Eliminar",
        command=eliminar,
        font=("Segoe UI", 13),
        width=150,
        height=35,
        corner_radius=8
    ).pack(pady=10)

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
    ).pack(pady=5)