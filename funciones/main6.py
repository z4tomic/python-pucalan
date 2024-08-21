#Ejercicio 5: Función de suma con retorno:  Crea una función `suma recursiva` para que retorne la suma del número elegido como parámetro y sus números anteriores. 
def sum_with_step(min_val, max_val, step):
    """
    Esta función suma los números desde min hasta max con un incremento de step.
    
    :param min_val: El valor mínimo desde donde empezar la suma.
    :param max_val: El valor máximo hasta donde sumar.
    :param step: El incremento entre cada número sumado.
    :return: La suma de los números desde min hasta max con un incremento de step.
    """
    if step <= 0:
        raise ValueError("El incremento (step) debe ser mayor que 0.")
    
    total_sum = 0
    current = min_val
    
    while current <= max_val:
        total_sum += current
        current += step
    
    return total_sum

# Ejemplo de uso
if __name__ == "__main__":
    try:
        # Solicitar al usuario que ingrese los valores
        min_val = float(input("Ingrese el valor mínimo: "))
        max_val = float(input("Ingrese el valor máximo: "))
        step = float(input("Ingrese el incremento (step): "))
        
        # Calcular la suma
        result = sum_with_step(min_val, max_val, step)
        
        # Mostrar el resultado
        print(f"La suma de los números desde {min_val} hasta {max_val} con un incremento de {step} es: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")
