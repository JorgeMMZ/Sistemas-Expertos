import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Listas de elementos del juego
personajes = ["Sr blanco", "Sra azul", "Prof ciruela", "Srta amapola", "Coronel mostaza"]
habitaciones = ["Sala", "Cocina", "Comedor", "Biblioteca", "Estudio"]
armas = ["Cuchillo", "Pistola", "Cuerda", "Llave inglesa", "Candelabro"]

# Función para crear combinaciones únicas de persona, habitación y arma
def crear_grupos(personajes, habitaciones, armas):
    elementos = list(zip(personajes, habitaciones, armas))
    random.shuffle(elementos)
    return elementos[:5]  # Retornamos cinco grupos aleatorios

# Crear grupos para la partida
grupos = crear_grupos(personajes, habitaciones, armas)

# Escena del crimen (aleatoria y diferente a los grupos generados)
while True:
    escena_crimen = (
        random.choice(personajes),
        random.choice(habitaciones),
        random.choice(armas)
    )
    if escena_crimen not in grupos:
        break

# Función para responder a la consulta del usuario
def responder_consulta(elemento):
    encontrado = False
    for personaje, habitacion, arma in grupos:
        if personaje == elemento or habitacion == elemento or arma == elemento:
            encontrado = True
            info = ""
            es_persona_correcta = personaje == escena_crimen[0]
            es_habitacion_correcta = habitacion == escena_crimen[1]
            es_arma_correcta = arma == escena_crimen[2]
            a = 1
            b = 1
            c = 1
            d = 1
            for objeto in escena_crimen:
                if elemento == objeto:
                    d = 0
            if personaje == elemento:
                info += f"{personaje} está en {habitacion} y tiene el {arma}.\n"
                a = 0
            if habitacion == elemento:
                info += f"En la habitación {habitacion} está {personaje} y tiene el {arma}.\n"
                b = 0
            if arma == elemento:
                info += f"El {arma} lo tiene {personaje} y está en {habitacion}.\n"
                c = 0
                
            if a: info += f"- {personaje} es {'verdadero' if (d^es_persona_correcta) else 'falso'}.\n"
            if b: info += f"- La ubicación ({habitacion}) es {'verdadera' if (d^es_habitacion_correcta) else 'falsa'}.\n"
            if c: info += f"- El arma ({arma}) es {'verdadera' if (d^es_arma_correcta) else 'falsa'}.\n"
            messagebox.showinfo("Resultado de la Consulta", info)
            return True
    if not encontrado:
        messagebox.showinfo("Elemento Desconocido", "Elemento desconocido, intenta nuevamente.")
        return False

# Función para manejar la consulta de un elemento desde el botón
def realizar_consulta(elemento):
    global inspecciones_restantes
    if responder_consulta(elemento):
        inspecciones_restantes -= 1
        lbl_inspecciones.config(text=f"Inspecciones restantes: {inspecciones_restantes}")
    if inspecciones_restantes == 0:
        adivinar_escena()

# Función para permitir al usuario adivinar la escena del crimen
def adivinar_escena():
    # Ventana de selección de escena del crimen
    ventana_adivinanza = tk.Toplevel(root)
    ventana_adivinanza.title("Adivina la Escena del Crimen")
    
    # Menús desplegables para elegir sospechoso, habitación y arma
    tk.Label(ventana_adivinanza, text="Selecciona el sospechoso:").pack(pady=5)
    sospechoso_var = tk.StringVar(value=personajes[0])
    tk.OptionMenu(ventana_adivinanza, sospechoso_var, *personajes).pack()
    
    tk.Label(ventana_adivinanza, text="Selecciona la habitación:").pack(pady=5)
    habitacion_var = tk.StringVar(value=habitaciones[0])
    tk.OptionMenu(ventana_adivinanza, habitacion_var, *habitaciones).pack()
    
    tk.Label(ventana_adivinanza, text="Selecciona el arma:").pack(pady=5)
    arma_var = tk.StringVar(value=armas[0])
    tk.OptionMenu(ventana_adivinanza, arma_var, *armas).pack()
    
    # Botón para confirmar la adivinanza
    def confirmar_adivinanza():
        sospechoso = sospechoso_var.get()
        lugar = habitacion_var.get()
        arma = arma_var.get()
        if (sospechoso, lugar, arma) == escena_crimen:
            messagebox.showinfo("Resultado", "¡Felicidades! Has acertado en todos los elementos de la escena del crimen.")
        else:
            mensaje = (f"Buen intento, pero no acertaste en todos los elementos.\n"
                       f"La escena correcta era: {escena_crimen[0]}, en {escena_crimen[1]} con {escena_crimen[2]}.")
            messagebox.showinfo("Resultado", mensaje)
        root.destroy()
    
    tk.Button(ventana_adivinanza, text="Confirmar Adivinanza", command=confirmar_adivinanza).pack(pady=10)

# Configuración de la ventana principal de tkinter
root = tk.Tk()
root.title("Juego de Clue")
root.geometry("600x400")

# Etiqueta de instrucciones
lbl_instrucciones = tk.Label(root, text="Selecciona un elemento para consultar:", font=("Arial", 12))
lbl_instrucciones.pack(pady=10)

# Contador de inspecciones restantes
inspecciones_restantes = 5
lbl_inspecciones = tk.Label(root, text=f"Inspecciones restantes: {inspecciones_restantes}", font=("Arial", 10))
lbl_inspecciones.pack(pady=5)

# Crear botones para cada personaje, habitación y arma
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Crear y organizar los botones para personajes
for personaje in personajes:
    btn_personaje = tk.Button(frame_botones, text=personaje, command=lambda p=personaje: realizar_consulta(p))
    btn_personaje.grid(row=0, column=personajes.index(personaje), padx=5, pady=5)

# Crear y organizar los botones para habitaciones
for habitacion in habitaciones:
    btn_habitacion = tk.Button(frame_botones, text=habitacion, command=lambda h=habitacion: realizar_consulta(h))
    btn_habitacion.grid(row=1, column=habitaciones.index(habitacion), padx=5, pady=5)

# Crear y organizar los botones para armas
for arma in armas:
    btn_arma = tk.Button(frame_botones, text=arma, command=lambda a=arma: realizar_consulta(a))
    btn_arma.grid(row=2, column=armas.index(arma), padx=5, pady=5)

# Iniciar la aplicación tkinter
root.mainloop()
