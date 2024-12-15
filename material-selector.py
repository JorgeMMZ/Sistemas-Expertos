import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np

class MaterialSelector:
    def __init__(self):
        # Descripciones de materiales (igual que antes)
        self.descripciones_materiales = {
            "Madera de Pino": "Material versátil y económico. Ligero, fácil de trabajar y con un aspecto cálido natural. Ideal para muebles rústicos o de estilo tradicional, pero requiere más mantenimiento.",
            "Madera de Roble": "Madera noble de alta durabilidad. Reconocida por su gran resistencia y belleza estética. Perfecta para muebles de alta calidad que buscan un aspecto elegante y duradero.",
            "MDF": "Material compuesto de fibras de madera prensadas. Económico y fácil de trabajar. Ideal para muebles modernos y para pintar, pero menos resistente a la humedad.",
            "Aluminio": "Metal ligero y resistente a la corrosión. Perfecto para muebles modernos, exteriores e industriales. Ofrece un aspecto contemporáneo y requiere poco mantenimiento.",
            "Acero Inoxidable": "Material ultra resistente y de alta durabilidad. Muy utilizado en cocinas y ambientes industriales. Excelente para muebles que requieren máxima resistencia y limpieza.",
            "Plástico": "Material versátil, ligero y económico. Disponible en múltiples colores y formas. Ideal para muebles juveniles, exteriores y con alto requerimiento de movilidad.",
            "Vidrio": "Material elegante y sofisticado. Perfecto para crear sensación de espacios amplios. Requiere cuidado por su fragilidad, pero ofrece un aspecto moderno y refinado.",
            "Bambú": "Material sostenible y ecológico. Ligero pero resistente. Ideal para muebles con diseño natural y para espacios zen o contemporáneos.",
            "Piedra": "Material noble y duradero. Ofrece una estética única y resistencia extrema. Perfecto para muebles decorativos y de exterior con un toque elegante y atemporal.",
            "Fibra de Carbono": "Material de alta tecnología. Extremadamente ligero y resistente. Utilizado en diseños de vanguardia y muebles de alto rendimiento.",
            "Resina Epóxica": "Material versátil que permite crear diseños únicos. Permite encapsular objetos y crear superficies con texturas increíbles. Popular en diseños modernos y artísticos.",
            "Hormigón": "Material industrial y moderno. Ofrece una estética cruda y contemporánea. Ideal para muebles minimalistas y espacios con diseño industrial.",
            "Corcho": "Material sostenible y ligero. Ofrece aislamiento térmico y acústico. Perfecto para espacios modernos y ecológicos.",
            "Titanio": "Metal de alta tecnología. Extremadamente resistente y ligero. Utilizado en diseños de vanguardia y muebles de lujo.",
            "Cartón Prensado": "Material ligero y económico. Ideal para diseños temporales o modulares. Muy utilizado en diseño experimental y muebles temporales."
        }

        # Materiales (igual que antes)
        self.materiales = {
            "Madera de Roble": {
                "resistencia": 5, 
                "impermeabilidad": 3,
                "resistencia_temperatura": 2,
                "precio": 1,
                "variedad_diseno": 5,
                "mantenimiento": 2,
                "peso": 3,
                "durabilidad": 5,
                "estetica": 5,
                "trabajabilidad": 4
            },
            "MDF": {
                "resistencia": 2, 
                "impermeabilidad": 1,
                "resistencia_temperatura": 1,
                "precio": 3,
                "variedad_diseno": 3,
                "mantenimiento": 4,
                "peso": 1,
                "durabilidad": 2,
                "estetica": 2,
                "trabajabilidad": 5
            },
            "Aluminio": {
                "resistencia": 5, 
                "impermeabilidad": 5,
                "resistencia_temperatura": 4,
                "precio": 2,
                "variedad_diseno": 3,
                "mantenimiento": 5,
                "peso": 5,
                "durabilidad": 4,
                "estetica": 3,
                "trabajabilidad": 2
            },
            "Madera de Pino": {
                "resistencia": 3, 
                "impermeabilidad": 2,
                "resistencia_temperatura": 2,
                "precio": 2,
                "variedad_diseno": 4,
                "mantenimiento": 3,
                "peso": 2,
                "durabilidad": 3,
                "estetica": 4,
                "trabajabilidad": 5
            },
            "Acero Inoxidable": {
                "resistencia": 5, 
                "impermeabilidad": 5,
                "resistencia_temperatura": 5,
                "precio": 1,
                "variedad_diseno": 2,
                "mantenimiento": 5,
                "peso": 4,
                "durabilidad": 5,
                "estetica": 3,
                "trabajabilidad": 1
            },
            "Plástico": {
                "resistencia": 2, 
                "impermeabilidad": 4,
                "resistencia_temperatura": 2,
                "precio": 4,
                "variedad_diseno": 5,
                "mantenimiento": 5,
                "peso": 1,
                "durabilidad": 2,
                "estetica": 2,
                "trabajabilidad": 3
            },
            "Vidrio": {
                "resistencia": 1, 
                "impermeabilidad": 5,
                "resistencia_temperatura": 3,
                "precio": 2,
                "variedad_diseno": 5,
                "mantenimiento": 2,
                "peso": 3,
                "durabilidad": 1,
                "estetica": 5,
                "trabajabilidad": 1
            },
            "Bambú": {
                "resistencia": 3, 
                "impermeabilidad": 2,
                "resistencia_temperatura": 2,
                "precio": 3,
                "variedad_diseno": 4,
                "mantenimiento": 3,
                "peso": 2,
                "durabilidad": 3,
                "estetica": 4,
                "trabajabilidad": 4
            },
            "Piedra": {
                "resistencia": 5, 
                "impermeabilidad": 5,
                "resistencia_temperatura": 5,
                "precio": 1,
                "variedad_diseno": 2,
                "mantenimiento": 4,
                "peso": 5,
                "durabilidad": 5,
                "estetica": 4,
                "trabajabilidad": 1
            },
            "Fibra de Carbono": {
                "resistencia": 5, 
                "impermeabilidad": 4,
                "resistencia_temperatura": 4,
                "precio": 1,
                "variedad_diseno": 3,
                "mantenimiento": 5,
                "peso": 1,
                "durabilidad": 4,
                "estetica": 3,
                "trabajabilidad": 2
            },
            "Resina Epóxica": {
                "resistencia": 4, 
                "impermeabilidad": 5,
                "resistencia_temperatura": 3,
                "precio": 2,
                "variedad_diseno": 5,
                "mantenimiento": 3,
                "peso": 2,
                "durabilidad": 3,
                "estetica": 4,
                "trabajabilidad": 4
            },
            "Hormigón": {
                "resistencia": 5, 
                "impermeabilidad": 4,
                "resistencia_temperatura": 5,
                "precio": 3,
                "variedad_diseno": 1,
                "mantenimiento": 2,
                "peso": 5,
                "durabilidad": 5,
                "estetica": 2,
                "trabajabilidad": 1
            },
            "Corcho": {
                "resistencia": 2, 
                "impermeabilidad": 3,
                "resistencia_temperatura": 2,
                "precio": 3,
                "variedad_diseno": 4,
                "mantenimiento": 4,
                "peso": 1,
                "durabilidad": 3,
                "estetica": 3,
                "trabajabilidad": 4
            },
            "Titanio": {
                "resistencia": 5, 
                "impermeabilidad": 4,
                "resistencia_temperatura": 5,
                "precio": 1,
                "variedad_diseno": 2,
                "mantenimiento": 5,
                "peso": 3,
                "durabilidad": 5,
                "estetica": 3,
                "trabajabilidad": 2
            },
            "Cartón Prensado": {
                "resistencia": 1, 
                "impermeabilidad": 1,
                "resistencia_temperatura": 1,
                "precio": 5,
                "variedad_diseno": 4,
                "mantenimiento": 3,
                "peso": 1,
                "durabilidad": 1,
                "estetica": 2,
                "trabajabilidad": 5
            }
        }

        # Ponderación de características (priorizar funcionalidad)
        self.ponderaciones = {
            "resistencia": 3.0,  # Mayor peso
            "durabilidad": 2.5,  # Alta prioridad
            "impermeabilidad": 2.0,
            "resistencia_temperatura": 2.0,
            "trabajabilidad": 1.5,
            "peso": 1.0,
            "mantenimiento": 1.0,
            "estetica": 0.5,  # Menor peso
            "variedad_diseno": 0.5,
            "precio": 0.5  # Menor impacto en la selección
        }

        # Preguntas más detalladas y nuevas
        self.preguntas = [
            # Preguntas de funcionalidad
            {
               "tipo": "opciones",
               "pregunta": "¿Qué nivel de resistencia necesitas?",
               "opciones": [
                   {"texto": "Baja resistencia", "valores": {"resistencia": 1}},
                   {"texto": "Resistencia moderada", "valores": {"resistencia": 2}},
                   {"texto": "Buena resistencia", "valores": {"resistencia": 3}},
                   {"texto": "Alta resistencia", "valores": {"resistencia": 4}},
                   {"texto": "Resistencia extrema", "valores": {"resistencia": 5}}
               ]
           },
           {
               "tipo": "opciones",
               "pregunta": "¿Cuál es la durabilidad esperada?",
               "opciones": [
                   {"texto": "Uso temporal", "valores": {"durabilidad": 1}},
                   {"texto": "Uso a corto plazo", "valores": {"durabilidad": 2}},
                   {"texto": "Uso moderado", "valores": {"durabilidad": 3}},
                   {"texto": "Uso prolongado", "valores": {"durabilidad": 4}},
                   {"texto": "Uso permanente", "valores": {"durabilidad": 5}}
               ]
           },
           {
               "tipo": "check",
               "pregunta": "¿Necesitas protección contra la humedad?",
               "caracteristicas_modificadas": {
                   "impermeabilidad": 5
               }
           },
           {
               "tipo": "opciones",
               "pregunta": "¿En qué ambiente se utilizará el mueble?",
               "opciones": [
                   {"texto": "Interior", "valores": {"resistencia_temperatura": 1, "impermeabilidad": 2}},
                   {"texto": "Semi-exterior", "valores": {"resistencia_temperatura": 3, "impermeabilidad": 4}},
                   {"texto": "Exterior", "valores": {"resistencia_temperatura": 5, "impermeabilidad": 5}}
               ]
           },
            {
                "tipo": "check",
                "pregunta": "¿Requieres exposición a altas temperaturas?",
                "caracteristicas_modificadas": {
                    "resistencia_temperatura": 4
                }
            },

            # Preguntas de manejo y trabajo
            {
                "tipo": "opciones",
                "pregunta": "¿Qué tan complejo será trabajar con el material?",
                "opciones": [
                    {"texto": "Muy fácil de trabajar", "valores": {"trabajabilidad": 5}},
                    {"texto": "Moderadamente complejo", "valores": {"trabajabilidad": 3}},
                    {"texto": "Difícil de trabajar", "valores": {"trabajabilidad": 1}}
                ]
            },
            {
                "tipo": "opciones",
                "pregunta": "¿Requieres movilidad o ligereza?",
                "opciones": [
                    {"texto": "Debe ser muy ligero", "valores": {"peso": 5}},
                    {"texto": "Peso moderado", "valores": {"peso": 3}},
                    {"texto": "Peso no es importante", "valores": {"peso": 1}}
                ]
            },

            # Preguntas de mantenimiento
            {
                "tipo": "opciones",
                "pregunta": "¿Qué nivel de mantenimiento puedes dar?",
                "opciones": [
                    {"texto": "Muy alto mantenimiento", "valores": {"mantenimiento": 1}},
                    {"texto": "Mantenimiento moderado", "valores": {"mantenimiento": 3}},
                    {"texto": "Bajo mantenimiento", "valores": {"mantenimiento": 5}}
                ]
            },

            # Preguntas de estética y diseño
            {
                "tipo": "opciones",
                "pregunta": "¿Qué importancia le das al diseño?",
                "opciones": [
                    {"texto": "Muy importante", "valores": {"estetica": 4, "variedad_diseno": 4}},
                    {"texto": "Moderadamente importante", "valores": {"estetica": 2, "variedad_diseno": 2}},
                    {"texto": "Poco importante", "valores": {"estetica": 1, "variedad_diseno": 1}}
                ]
            },

            # Preguntas de presupuesto
            {
                "tipo": "opciones",
                "pregunta": "¿Cuál es tu restricción presupuestaria?",
                "opciones": [
                    {"texto": "Presupuesto muy limitado", "valores": {"precio": 5}},
                    {"texto": "Presupuesto moderado", "valores": {"precio": 3}},
                    {"texto": "Sin restricción presupuestaria", "valores": {"precio": 1}}
                ]
            }
        ]

        # Resto del código de inicialización (similar al anterior)
        self.root = tk.Tk()
        self.root.title("Selector Avanzado de Materiales para Muebles")
        self.root.geometry("800x800")

        self.caracteristicas_usuario = {
            "resistencia": 0,
            "impermeabilidad": 0,
            "resistencia_temperatura": 0,
            "precio": 0,
            "variedad_diseno": 0,
            "mantenimiento": 0,
            "peso": 0,
            "durabilidad": 0,
            "estetica": 0,
            "trabajabilidad": 0
        }

    def crear_interfaz(self):
        # Título
        tk.Label(self.root, text="Selector de Materiales", font=("Arial", 16, "bold")).pack(pady=10)
    
        # Canvas con scrollbar para manejar muchas preguntas
        canvas = tk.Canvas(self.root)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
    
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
    
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
    
        # Título de sección
        tk.Label(scrollable_frame, text="Cuestionario de Necesidades", font=("Arial", 12)).pack(pady=10)
    
        self.variables_respuestas = []
    
        # Generar preguntas con un estilo más ordenado
        for i, pregunta in enumerate(self.preguntas, 1):
            # Frame para cada pregunta
            frame_pregunta = tk.Frame(scrollable_frame, relief=tk.RIDGE, borderwidth=1)
            frame_pregunta.pack(fill="x", padx=10, pady=5, ipady=5)
    
            # Numeración y texto de la pregunta
            tk.Label(
                frame_pregunta, 
                text=f"{i}. {pregunta['pregunta']}", 
                font=("Arial", 10, "bold"), 
                anchor="w"
            ).pack(anchor="w", padx=10)
            
            if pregunta["tipo"] == "check":
                var = tk.BooleanVar()
                self.variables_respuestas.append((var, pregunta))
                cb = tk.Checkbutton(
                    frame_pregunta, 
                    text="Sí", 
                    variable=var,
                    font=("Arial", 10)
                )
                cb.pack(anchor="w", padx=20)
    
            elif pregunta["tipo"] == "opciones":
                var = tk.StringVar()
                self.variables_respuestas.append((var, pregunta))
                
                # Crear un frame interno para los radio buttons
                frame_opciones = tk.Frame(frame_pregunta)
                frame_opciones.pack(anchor="w", padx=20)
                
                for opcion in pregunta["opciones"]:
                    rb = tk.Radiobutton(
                        frame_opciones, 
                        text=opcion["texto"], 
                        variable=var, 
                        value=opcion["texto"],
                        font=("Arial", 10)
                    )
                    rb.pack(anchor="w")
    
        # Añadir scrollbars
        canvas.pack(side="left", fill="both", expand=True, padx=10)
        scrollbar.pack(side="right", fill="y")
    
        # Botón de selección con un estilo más llamativo
        tk.Button(
            self.root, 
            text="Encontrar Materiales", 
            command=self.encontrar_materiales,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",  # Color verde
            fg="white"     # Texto blanco
        ).pack(pady=20)

    def encontrar_materiales(self):
        # Resetear características de usuario
        for key in self.caracteristicas_usuario:
            self.caracteristicas_usuario[key] = 0

        # Modificar características según respuestas
        for var, pregunta in self.variables_respuestas:
            if pregunta["tipo"] == "check":
                if var.get():
                    for caract, valor in pregunta["caracteristicas_modificadas"].items():
                        self.caracteristicas_usuario[caract] += valor
            
            elif pregunta["tipo"] == "opciones":
                for opcion in pregunta["opciones"]:
                    if var.get() == opcion["texto"]:
                        for caract, valor in opcion["valores"].items():
                            self.caracteristicas_usuario[caract] += valor

        # Asegurar que los valores no sean negativos
        for key in self.caracteristicas_usuario:
            self.caracteristicas_usuario[key] = max(0, self.caracteristicas_usuario[key])

        # Calcular similitud
        similitudes = {}
        for nombre, caracteristicas in self.materiales.items():
            distancia = self.calcular_similitud(caracteristicas)
            similitudes[nombre] = distancia

        # Ordenar materiales por similitud
        materiales_ordenados = sorted(
            similitudes.items(), 
            key=lambda x: x[1], 
            reverse=True
        )

        # Mostrar top 3 materiales con descripción
        resultado = "Materiales Recomendados:\n\n"
        for nombre, similitud in materiales_ordenados[:3]:
            resultado += f"{nombre} (Similitud: {similitud:.2f})\n"
            resultado += f"Descripción: {self.descripciones_materiales[nombre]}\n\n"

        messagebox.showinfo("Resultados", resultado)

    def calcular_similitud(self, caracteristicas_material):
        # Calcular similitud usando distancia euclidiana ponderada
        distancia = np.sqrt(
            sum(
                self.ponderaciones[key] * 
                ((self.caracteristicas_usuario[key] - caracteristicas_material[key])**2)
                for key in self.caracteristicas_usuario
            )
        )
        
        # Convertir a métrica de similitud con rango de 0-5
        similitud = 5 / (1 + distancia)
        return similitud
    def run(self):
        self.root.mainloop()

# Iniciar aplicación
if __name__ == "__main__":
    selector = MaterialSelector()
    selector.crear_interfaz()  # Añadir esta línea
    selector.run()