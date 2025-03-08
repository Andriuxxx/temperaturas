# Realizado por Andres Delgado
import numpy as np

# Definimos los parámetros de la matriz 3D
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

num_ciudades = len(ciudades)
num_dias = len(dias_semana)
num_semanas = semanas

# Creamos una matriz 3D de temperaturas aleatorias entre 10 y 35 grados
temperaturas = np.random.randint(10, 35, (num_ciudades, num_dias, num_semanas))

# Mostrar las temperaturas registradas
print("\n--- Registro de Temperaturas ---")
for ciudad in range(num_ciudades):
    print(f"\nCiudad: {ciudades[ciudad]}")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}: ", end="")
        for dia in range(num_dias):
            print(f"{dias_semana[dia]}: {temperaturas[ciudad, dia, semana]}°C", end=", ")
        print()

# Calcular y mostrar promedios de temperatura por ciudad y semana
print("\n--- Promedio de Temperaturas ---")
for ciudad in range(num_ciudades):
    print(f"\nCiudad: {ciudades[ciudad]}")
    for semana in range(num_semanas):
        promedio = np.mean(temperaturas[ciudad, :, semana])
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
