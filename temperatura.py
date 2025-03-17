# Se cambio el antiguo codigo por el siguiente:
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad en base a datos semanales.
    
    :param temperaturas: Diccionario con ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con ciudades como claves y sus respectivas temperaturas promedio como valores.
    """
    promedios = {}  # Diccionario para almacenar los promedios de cada ciudad
    
    for ciudad, temps in temperaturas.items():  # Iterar sobre cada ciudad y sus temperaturas
        promedio = sum(temps) / len(temps)  # Calcular el promedio sumando y dividiendo por la cantidad de valores
        promedios[ciudad] = round(promedio, 2)  # Redondear el resultado a dos decimales y almacenarlo en el diccionario
    
    return promedios  # Devolver el diccionario con los promedios

# Datos de prueba (3 ciudades, 4 semanas de temperaturas en grados Celsius)
temperaturas_ciudades = {
    "Quito": [18, 20, 19, 17],  # Temperaturas registradas en Quito durante 4 semanas
    "Guayaquil": [29, 30, 31, 28],  # Temperaturas registradas en Guayaquil durante 4 semanas
    "Cuenca": [16, 17, 15, 14]  # Temperaturas registradas en Cuenca durante 4 semanas
}

# Prueba de la función
promedios = calcular_temperatura_promedio(temperaturas_ciudades)  # Llamar a la función con los datos de prueba
print("Temperaturas promedio por ciudad:", promedios)  # Imprimir los resultados
