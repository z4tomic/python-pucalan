# ejercicio 1: Función de impresión personalizada: Crea una función llamada print_2 que reciba un texto y un número `n`, y que imprima el texto `n` veces en una nueva línea cada vez.

def print_2(texto, n):
    """
    Imprime el texto `n` veces, cada vez en una nueva línea.

    Args:
    texto (str): El texto que se va a imprimir.
    n (int): El número de veces que se imprimirá el texto.
    """
    for _ in range(n):
        print(texto)

def main():
    # leer el texto del usuario
    texto = input("Introduce el texto que quieres imprimir: ")
    
    # leer el número de repeticiones desde el usuario
    while True:
        try:
            n = int(input("Introduce el número de veces que quieres imprimir el texto: "))
            if n <= 0:
                print("Por favor, introduce un número entero positivo.")
            else:
                break
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    
    # llamar a la función con el texto y el número de repeticiones
    print_2(texto, n)

if __name__ == "__main__":
    main()
