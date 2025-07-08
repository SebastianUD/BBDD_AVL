import customtkinter as ctk
from tkinter import messagebox
from Profesor import Profesor

def mostrar_formulario_actualizar_profesor(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Actualizar Profesor")
    ventana.geometry("520x560")
    ventana.resizable(False, False)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana, text="Actualizar Datos del Profesor",
        font=("Segoe UI", 16, "bold"), text_color="white"
    ).pack(pady=20)

    entradas = {}

    def crear_entrada(label, placeholder):
        ctk.CTkLabel(ventana, text=label, font=("Segoe UI", 12), text_color="white").pack()
        entry = ctk.CTkEntry(ventana, placeholder_text=placeholder, width=340)
        entry.pack(pady=8)
        entradas[label] = entry

    crear_entrada("Código", "Código del profesor a actualizar")
    crear_entrada("Nombre", "Nuevo nombre")
    crear_entrada("Correo", "Nuevo correo")

    ctk.CTkLabel(ventana, text="Vinculación", font=("Segoe UI", 12), text_color="white").pack()
    opciones_vinculo = ["Planta", "Cátedra", "Ocasional", "Otro"]
    vinculo_var = ctk.StringVar(value=opciones_vinculo[0])
    menu_vinculo = ctk.CTkOptionMenu(
        ventana, values=opciones_vinculo, variable=vinculo_var, width=340, height=30
    )
    menu_vinculo.pack(pady=10)

    def actualizar():
        try:
            codigo = int(entradas["Código"].get())
            profesor = gestor.buscar_por_codigo(codigo)

            if not profesor:
                messagebox.showerror("No encontrado", f"No existe profesor con código {codigo}")
                return

            nuevo_nombre = entradas["Nombre"].get().strip() or profesor.nombre
            nuevo_correo = entradas["Correo"].get().strip() or profesor.correo
            nueva_vinculacion = vinculo_var.get()

            if "@" not in nuevo_correo or "." not in nuevo_correo:
                messagebox.showerror("Error", "Correo no válido.")
                return

            nuevo_profesor = Profesor(codigo, nuevo_nombre, nuevo_correo, nueva_vinculacion)
            gestor.actualizar_entidad(codigo, nuevo_profesor)
            messagebox.showinfo("Éxito", "Profesor actualizado correctamente.")
            ventana.destroy()
            from GUI_Profesor import mostrar_interfaz_profesores
            mostrar_interfaz_profesores()

        except ValueError:
            messagebox.showerror("Error", "El código debe ser un número entero.")

    ctk.CTkButton(
        ventana, text="Actualizar", command=actualizar,
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