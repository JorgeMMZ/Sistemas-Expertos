import json
import os

class Nodo:
    def __init__(self, valor, es_pregunta=True):
        self.valor = valor  # Valor del nodo (puede ser una pregunta o una comida)
        self.es_pregunta = es_pregunta  # True si es pregunta, False si es comida
        self.si = None  # Rama para respuesta "sí"
        self.no = None  # Rama para respuesta "no"

    def a_dict(self):
        # Convierte el nodo a un diccionario para guardarlo en JSON
        nodo_dict = {
            "valor": self.valor,
            "es_pregunta": self.es_pregunta,
            "si": self.si.a_dict() if self.si else None,
            "no": self.no.a_dict() if self.no else None,
        }
        return nodo_dict

    @classmethod
    def desde_dict(cls, data):
        # Convierte un diccionario a un nodo
        nodo = cls(data["valor"], data["es_pregunta"])
        nodo.si = cls.desde_dict(data["si"]) if data["si"] else None
        nodo.no = cls.desde_dict(data["no"]) if data["no"] else None
        return nodo

class AdivinaComida:
    def __init__(self, archivo_json="conocimientocomida.json"):
        self.archivo_json = archivo_json
        # Cargar el árbol desde el archivo o crear un árbol nuevo si el archivo no existe
        self.raiz = self.cargar_conocimiento()

    def cargar_conocimiento(self):
        # Intenta cargar el árbol desde el archivo JSON
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, "r") as archivo:
                data = json.load(archivo)
                return Nodo.desde_dict(data)
        # Si no existe el archivo, crea un árbol inicial
        nodo_raiz = Nodo("¿Es un plato principal?", es_pregunta=True)
        nodo_raiz.si = Nodo("pizza", es_pregunta=False)
        return nodo_raiz

    def guardar_conocimiento(self):
        # Guarda el árbol en el archivo JSON
        with open(self.archivo_json, "w") as archivo:
            json.dump(self.raiz.a_dict(), archivo, indent=4)

    def jugar(self):
        nodo_actual = self.raiz
        while nodo_actual.es_pregunta:
            respuesta = input(f"{nodo_actual.valor} (sí/no): ").strip().lower()
            if respuesta == "si":
                if nodo_actual.si:
                    nodo_actual = nodo_actual.si
                else:
                    print("No tengo más información. Agreguemos nueva comida.")
                    self.agregar_comida(nodo_actual, respuesta=True)
                    return
            elif respuesta == "no":
                if nodo_actual.no:
                    nodo_actual = nodo_actual.no
                else:
                    print("No tengo más información. Agreguemos nueva comida.")
                    self.agregar_comida(nodo_actual, respuesta=False)
                    return
            else:
                print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

        # Llegamos a una comida, intentamos adivinar
        respuesta_final = input(f"¿Es {nodo_actual.valor}? (si/no): ").strip().lower()
        if respuesta_final == "si":
            print("¡He adivinado!")
        else:
            print("No adiviné. Vamos a agregar esta comida a mi base de conocimientos.")
            self.agregar_comida(nodo_actual, respuesta=False)

    def agregar_comida(self, nodo, respuesta):
        nueva_comida = input("¿En qué comida estabas pensando?: ").strip()
        nueva_pregunta = input(f"Dame una pregunta para diferenciar '{nueva_comida}' de '{nodo.valor}': ").strip()

        # Crear nuevos nodos para la nueva comida y la pregunta
        nodo_nueva_comida = Nodo(nueva_comida, es_pregunta=False)
        nodo_pregunta = Nodo(nueva_pregunta, es_pregunta=True)

        # Configurar las ramas según la respuesta
        if respuesta:
            nodo_pregunta.si = nodo_nueva_comida
            nodo_pregunta.no = Nodo(nodo.valor, es_pregunta=False)
        else:
            nodo_pregunta.si = Nodo(nodo.valor, es_pregunta=False)
            nodo_pregunta.no = nodo_nueva_comida

        # Reemplazar el nodo actual con la nueva pregunta
        nodo.valor = nodo_pregunta.valor
        nodo.es_pregunta = True
        nodo.si = nodo_pregunta.si
        nodo.no = nodo_pregunta.no

        # Guardar el nuevo conocimiento en el archivo JSON
        self.guardar_conocimiento()

# Ejecución del juego
juego = AdivinaComida()
while True:
    print("\n--- Nuevo Juego de Adivina la Comida ---")
    juego.jugar()
    continuar = input("¿Quieres jugar otra vez? (si/no): ").strip().lower()
    if continuar != "si":
        print("¡Gracias por jugar!")
        break
