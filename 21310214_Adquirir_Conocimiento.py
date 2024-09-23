# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:17:28 2024

@author: Ghost
"""

# Base de conocimiento inicial
base_conocimiento = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿De qué te gustaría hablar?": "Podemos hablar de lo que quieras."
}

def responder(pregunta):
    # Buscar respuesta en la base de conocimiento
    if pregunta in base_conocimiento:
        return base_conocimiento[pregunta]
    else:
        # Preguntar al usuario por la nueva respuesta si no está registrada
        return "No conozco la respuesta a esa pregunta. ¿Me puedes enseñar la respuesta?"

def agregar_conocimiento(pregunta, respuesta):
    # Agregar el nuevo conocimiento a la base de datos
    base_conocimiento[pregunta] = respuesta
    print(f"Nueva pregunta '{pregunta}' agregada con su respuesta: '{respuesta}'")

def chat():
    print("Bienvenido al chat. Escribe 'salir' para tsalirerminar.")
    
    while True:
        pregunta = input("Tú: ")
        
        if pregunta.lower() == 'salir':
            print("Adiós!")
            break
        
        respuesta = responder(pregunta)
        print(f"Bot: {respuesta}")
        
        # Si el bot no conoce la respuesta, solicitar al usuario que la enseñe
        if respuesta == "No conozco la respuesta a esa pregunta. ¿Me puedes enseñar la respuesta?":
            nueva_respuesta = input("Por favor, ingresa la respuesta: ")
            agregar_conocimiento(pregunta, nueva_respuesta)

# Ejecutar el chat
chat()
