#Ejercicio 4: Función de conteo de caracteres: Crea una función llamada `count_chars` que reciba una cadena de texto y retorne un diccionario con la frecuencia de cada carácter en la cadena.

def count_chars(text):
    """
    esta función recibe una cadena de texto y retorna un diccionario con la frecuencia de cada carácter en la cadena.
    
    :param text: Cadena de texto para contar los caracteres.
    :return: Diccionario con los caracteres como claves y sus frecuencias como valores.
    """
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def main():
    print("Bienvenido al programa de conteo de caracteres.")
    
    # solicitar al usuario que ingrese una cadena de texto
    text = input("Ingrese una cadena de texto: ")
    
    # contar los caracteres
    result = count_chars(text)
    
    # mostrar el resultado
    print("Frecuencia de cada carácter en la cadena:")
    for char, count in result.items():
        print(f"'{char}': {count}")

# ejecutar la función principal
if __name__ == "__main__":
    main()
