import tkinter as tk
from tkinter import messagebox


def calcular(operacion):
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        if operacion == "sumar":
            resultado = num1 + num2
            simbolo = "+"
        elif operacion == "restar":
            resultado = num1 - num2
            simbolo = "-"
        elif operacion == "multiplicar":
            resultado = num1 * num2
            simbolo = "*"
        elif operacion == "dividir":
            if num2 == 0:
                messagebox.showerror(
                    "Error", "No se puede dividir entre cero."
                )
                return
            resultado = num1 / num2
            simbolo = "/"

        # Mostrar resultado formateado (quita decimales innecesarios si es entero)
        if resultado.is_integer():
            resultado = int(resultado)

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        messagebox.showerror(
            "Error", "Por favor ingresa números válidos en ambos campos."
        )


def limpiar():
    entrada_num1.delete(0, tk.END)
    entrada_num2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado: ")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Moderna")
ventana.geometry("320x380")
ventana.config(bg="#f0f0f0")
ventana.resizable(False, False)

# Título
titulo = tk.Label(
    ventana,
    text="Calculadora",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
titulo.pack(pady=15)

# Campo Número 1
frame_num1 = tk.Frame(ventana, bg="#f0f0f0")
frame_num1.pack(pady=5)
tk.Label(
    frame_num1, text="Primer número:", font=("Arial", 10), bg="#f0f0f0"
).pack(anchor="w")
entrada_num1 = tk.Entry(
    frame_num1, font=("Arial", 12), width=22, relief="solid", bd=1
)
entrada_num1.pack(pady=2)

# Campo Número 2
frame_num2 = tk.Frame(ventana, bg="#f0f0f0")
frame_num2.pack(pady=5)
tk.Label(
    frame_num2, text="Segundo número:", font=("Arial", 10), bg="#f0f0f0"
).pack(anchor="w")
entrada_num2 = tk.Entry(
    frame_num2, font=("Arial", 12), width=22, relief="solid", bd=1
)
entrada_num2.pack(pady=2)

# Frame para los botones de operaciones
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=10)

btn_sumar = tk.Button(
    frame_botones,
    text="+",
    font=("Arial", 14, "bold"),
    width=4,
    bg="#4CAF50",
    fg="white",
    command=lambda: calcular("sumar"),
)
btn_sumar.grid(row=0, column=0, padx=5, pady=5)

btn_restar = tk.Button(
    frame_botones,
    text="-",
    font=("Arial", 14, "bold"),
    width=4,
    bg="#2196F3",
    fg="white",
    command=lambda: calcular("restar"),
)
btn_restar.grid(row=0, column=1, padx=5, pady=5)

btn_multiplicar = tk.Button(
    frame_botones,
    text="×",
    font=("Arial", 14, "bold"),
    width=4,
    bg="#FF9800",
    fg="white",
    command=lambda: calcular("multiplicar"),
)
btn_multiplicar.grid(row=1, column=0, padx=5, pady=5)

btn_dividir = tk.Button(
    frame_botones,
    text="÷",
    font=("Arial", 14, "bold"),
    width=4,
    bg="#9C27B0",
    fg="white",
    command=lambda: calcular("dividir"),
)
btn_dividir.grid(row=1, column=1, padx=5, pady=5)

# Botón de limpiar
btn_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    font=("Arial", 10),
    width=15,
    bg="#f44336",
    fg="white",
    command=limpiar,
)
btn_limpiar.pack(pady=5)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(
    ventana,
    text="Resultado: ",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#009688",
)
etiqueta_resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
