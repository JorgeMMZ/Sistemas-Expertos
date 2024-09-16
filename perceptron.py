# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:11:51 2024

@author: Ghost
"""

import numpy as np

# Hábitos iniciales de la persona [horas de ejercicio, consumo de azúcar, consumo de vegetales]
# Convertimos los hábitos a float para evitar problemas de casting
habitos = np.array([1, -1, 1], dtype=float)  # Supongamos: 1 hora de ejercicio, alto consumo de azúcar, alto consumo de vegetales
ajuste_habitos = habitos.copy()

# Datos de 4 días de hábitos reales de la persona [ejercicio, azúcar, vegetales]
datos_diarios = np.array([
    [1, -1, -1],  # Día 1: 1 hora de ejercicio, alto consumo de azúcar, bajo consumo de vegetales
    [1, 1, -1],   # Día 2: 1 hora de ejercicio, bajo consumo de azúcar, bajo consumo de vegetales
    [1, -1, 1],   # Día 3: 1 hora de ejercicio, alto consumo de azúcar, alto consumo de vegetales
    [1, 1, 1]     # Día 4: 1 hora de ejercicio, bajo consumo de azúcar, alto consumo de vegetales
], dtype=float)

# Evaluación diaria de si cumplió o no con su objetivo (1 si cumplió, -1 si no cumplió)
evaluacion = np.array([-1, -1, -1, 1], dtype=float)  # Objetivo: más vegetales, menos azúcar

# Ajuste de hábitos basado en los días anteriores
for dia in range(4):
    # Predicción basada en hábitos actuales (dot product entre hábitos actuales y hábitos diarios)
    prediccion = np.sign(np.dot(ajuste_habitos, datos_diarios[dia, :]))
    
    # Ajuste los hábitos si la predicción no coincide con la evaluación real
    ajuste_habitos += (evaluacion[dia] - prediccion) * (datos_diarios[dia, :] / 2)

# Revisión de los hábitos ajustados después de 4 días
for dia in range(4):
    evaluacion_predicha = np.sign(np.dot(ajuste_habitos, datos_diarios[dia, :]))
    print(f"Día {dia + 1}: Predicción después del ajuste = {evaluacion_predicha}")

print(f"Hábitos ajustados después de 4 días: {ajuste_habitos}")
