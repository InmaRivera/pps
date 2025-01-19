import unicodedata

def esPalindromo(palabra):
    try:
        # Asegurarse de que el parámetro sea una cadena
        if not isinstance(palabra, str):
            raise ValueError("El parámetro debe ser una cadena.")  # Lanzar ValueError explícito

        # Normalizar la cadena para eliminar tildes y otros caracteres especiales
        palabra_normalizada = unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('utf-8')
        
        # Limpiar la cadena: eliminar espacios, convertir a minúsculas y quitar caracteres no alfanuméricos
        palabra_limpia = ''.join(char.lower() for char in palabra_normalizada if char.isalnum())
        
        # Comprobar si es un palíndromo
        return palabra_limpia == palabra_limpia[::-1]  # Compara la cadena limpia con su reverso

    except ValueError:
        raise  # Re-lanzar el error para que los tests lo detecten
    except Exception as e:
        print(f"Error en la función esPalindromo: {e}")
        return False


if __name__ == "__main__":
    while True:
        # Solicitar entrada del usuario
        palabra = input('Escriba una palabra o frase (o escriba "salir" para terminar): ')
        
        # Salir del bucle si el usuario lo indica
        if palabra.lower() == "salir":
            print("Programa finalizado. ¡Hasta luego!")
            break
        
        # Evaluar y mostrar el mensaje adecuado
        if esPalindromo(palabra):
            print(f'"{palabra}" : Sí es palíndroma.')
        else:
            print(f'"{palabra}" : No es palíndroma.')
