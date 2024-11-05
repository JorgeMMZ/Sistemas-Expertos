# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:49:20 2024

@author: Ghost
"""

import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    def __init__(self, valor, es_pregunta=True):
        self.valor = valor
        self.es_pregunta = es_pregunta
        self.si = None
        self.no = None

    def a_dict(self):
        nodo_dict = {
            "valor": self.valor,
            "es_pregunta": self.es_pregunta,
            "si": self.si.a_dict() if self.si else None,
            "no": self.no.a_dict() if self.no else None,
        }
        return nodo_dict

    @classmethod
    def desde_dict(cls, data):
        nodo = cls(data["valor"], data["es_pregunta"])
        nodo.si = cls.desde_dict(data["si"]) if data["si"] else None
        nodo.no = cls.desde_dict(data["no"]) if data["no"] else None
        return nodo

class AdivinaComida:
    def __init__(self, archivo_json="conocimientocomida.json"):
        self.archivo_json = archivo_json
        self.raiz = self.cargar_conocimiento()
        self.nodo_actual = self.raiz

    def cargar_conocimiento(self):
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, "r") as archivo:
                data = json.load(archivo)
                return Nodo.desde_dict(data)
        nodo_raiz = Nodo("¿Es un plato principal?", es_pregunta=True)
        nodo_raiz.si = Nodo("pizza", es_pregunta=False)
        nodo_raiz.no = Nodo("Arroz con leche", es_pregunta=False)
        
        return nodo_raiz

    def guardar_conocimiento(self):
        with open(self.archivo_json, "w") as archivo:
            json.dump(self.raiz.a_dict(), archivo, indent=4)

    def jugar(self, root):
        self.nodo_actual = self.raiz
        self.mostrar_pregunta(root)

    def mostrar_pregunta(self, root):
        if self.nodo_actual.es_pregunta:
            pregunta_label.config(text=self.nodo_actual.valor)
            respuesta_si_btn.config(command=lambda: self.procesar_respuesta(True, root))
            respuesta_no_btn.config(command=lambda: self.procesar_respuesta(False, root))
        else:
            pregunta_label.config(text=f"¿Es {self.nodo_actual.valor}?")
            respuesta_si_btn.config(command=lambda: self.adivinado(root))
            respuesta_no_btn.config(command=lambda: self.agregar_nueva_comida(root))

    def procesar_respuesta(self, respuesta, root):
        if respuesta:
            if self.nodo_actual.si:
                self.nodo_actual = self.nodo_actual.si
            else:
                self.agregar_nueva_comida(root)
                return
        else:
            if self.nodo_actual.no:
                self.nodo_actual = self.nodo_actual.no
            else:
                self.agregar_nueva_comida(root)
                return
        self.mostrar_pregunta(root)

    def adivinado(self, root):
        messagebox.showinfo("¡Adiviné!", "¡He adivinado!")
        if messagebox.askyesno("Nuevo Juego", "¿Quieres jugar otra vez?"):
            self.jugar(root)
        else:
            root.destroy()

    def agregar_nueva_comida(self, root):
        nueva_comida = simpledialog.askstring("Nueva Comida", "¿En qué comida estabas pensando?")
        if not nueva_comida:
            return
        nueva_pregunta = simpledialog.askstring("Nueva Pregunta", f"Dame una pregunta para diferenciar '{nueva_comida}' de '{self.nodo_actual.valor}'")
        if not nueva_pregunta:
            return

        nodo_nueva_comida = Nodo(nueva_comida, es_pregunta=False)
        nodo_pregunta = Nodo(nueva_pregunta, es_pregunta=True)

        if messagebox.askyesno("Confirmación", f"¿La respuesta a la pregunta para '{nueva_comida}' sería 'sí'?"):
            nodo_pregunta.si = nodo_nueva_comida
            nodo_pregunta.no = Nodo(self.nodo_actual.valor, es_pregunta=False)
        else:
            nodo_pregunta.si = Nodo(self.nodo_actual.valor, es_pregunta=False)
            nodo_pregunta.no = nodo_nueva_comida

        self.nodo_actual.valor = nodo_pregunta.valor
        self.nodo_actual.es_pregunta = True
        self.nodo_actual.si = nodo_pregunta.si
        self.nodo_actual.no = nodo_pregunta.no

        self.guardar_conocimiento()
        messagebox.showinfo("Nuevo Conocimiento", f"{nueva_comida} ha sido agregado a la base de conocimientos.")
        self.jugar(root)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Adivina la Comida")
root.geometry("400x300")


juego = AdivinaComida()
pregunta_label = tk.Label(root, text="Piensa en una comida y responde las preguntas", font=("Arial", 12), wraplength=300)
pregunta_label.pack(pady=20)

respuesta_si_btn = tk.Button(root, text="Sí", width=10)
respuesta_si_btn.pack(side=tk.LEFT, padx=20, pady=10)

respuesta_no_btn = tk.Button(root, text="No", width=10)
respuesta_no_btn.pack(side=tk.RIGHT, padx=20, pady=10)

juego.jugar(root)

root.mainloop()
