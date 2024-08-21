#Ejercicio 5: Función de suma con retorno:  Crea una función `suma recursiva` para que retorne la suma del número elegido como parámetro y sus números anteriores. 
def suma_recursiva(n):
    """
    Esta función recibe un número entero n y retorna la suma de n y todos sus números anteriores hasta 0 usando recursión.
    
    :param n: El número hasta el cual se sumarán todos los números anteriores.
    :return: La suma de n y todos sus números anteriores.
    """
    # caso base: si n es menor o igual a 0, la suma es 0
    if n <= 0:
        return 0
    else:
        # llamada recursiva: suma el número actual con la suma de los números anteriores
        return n + suma_recursiva(n - 1)

# ejemplo de uso
if __name__ == "__main__":
    try:
        # solicitar al usuario que ingrese un número entero
        number = int(input("Ingrese un número entero: "))
        
        # calcular la suma recursiva
        result = suma_recursiva(number)
        
        # mostrar el resultado
        print(f"La suma de {number} y todos sus números anteriores es: {result}")
    
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
