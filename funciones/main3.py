#Ejercicio 3: Función de promedio: Crea una función llamada `average` que reciba una lista de números y retorne el promedio de estos.

def average(numbers):
    """
    Esta función recibe una lista de números y retorna el promedio de estos.
    
    :param numbers: Lista de números.
    :return: El promedio de los números en la lista.
    """
    if not numbers:
        raise ValueError("La lista no puede estar vacía.")
    
    return sum(numbers) / len(numbers)

def main():
    print("Bienvenido al programa de cálculo de promedio.")
    
    # solitica al usuario que ingrese números separados por comas
    input_str = input("Ingrese una lista de números separados por comas (por ejemplo: 10,20,30): ")
    
    # convertir la entrada en una lista de números
    try:
        # convertir la cadena de entrada en una lista de flotantes
        numbers = [float(num) for num in input_str.split(',')]
    except ValueError:
        print("Por favor, ingrese números válidos separados por comas.")
        return
    
    # calcular el promedio
    try:
        result = average(numbers)
        print(f"El promedio de los números {numbers} es: {result:.2f}")
    except ValueError as e:
        print(e)

# ejecutar la función principal
if __name__ == "__main__":
    main()
