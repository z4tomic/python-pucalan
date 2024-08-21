#Ejercicio 2: Función de multiplicación: Crea una función llamada `multiply` que reciba dos números y retorne el producto de los dos.

def multiply(a, b):
    """
    Esta función recibe dos números y retorna su producto.
    
    :param a: El primer número.
    :param b: El segundo número.
    :return: El producto de a y b.
    """
    return a * b

def main():
    print("Bienvenido al programa de multiplicación.")
    
    # solivita al usuario que ingrese dos números
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return
    
    # calcular el producto
    resultado = multiply(num1, num2)
    
    # Mostrar el resultado
    print(f"El producto de {num1} y {num2} es: {resultado}")

# ejecutar la función principal
if __name__ == "__main__":
    main()
