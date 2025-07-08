import customtkinter as ctk

def mostrar_arbol_avl_profesores(gestor):
    ventana = ctk.CTkToplevel()
    ventana.title("Árbol AVL de Profesores")
    ventana.geometry("960x540")
    ventana.resizable(True, True)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.CTkLabel(
        ventana,
        text="Visualización del Árbol AVL (Profesores)",
        font=("Segoe UI", 16, "bold"),
        text_color="white"
    ).pack(pady=15)

    output_box = ctk.CTkTextbox(ventana, width=880, height=380, font=("Courier", 12))
    output_box.pack(pady=10)

    output_box.configure(state="normal")
    if gestor.arbol.raiz:
        arbol = gestor.arbol.convertir_a_binarytree(gestor.arbol.raiz)
        output_box.insert("end", str(arbol))
        output_box.insert("end", f"\n\nAltura del árbol: {1 + arbol.height}")
        output_box.insert("end", f"\nNodos totales: {arbol.size}")
        output_box.insert("end", f"\nHojas: {arbol.leaf_count}")
    else:
        output_box.insert("end", "El árbol está vacío.")
    output_box.configure(state="disabled")

    # Botón volver
    def volver():
        ventana.destroy()
        from gui.core.GUI_Profesor import mostrar_interfaz_profesores
        mostrar_interfaz_profesores()

    ctk.CTkButton(
        ventana, text="Volver",
        command=volver,
        font=("Segoe UI", 13), width=200, height=35,
        fg_color="#e67e22", hover_color="#d35400"
    ).pack(pady=15)