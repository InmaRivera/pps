
# # Usamos la palabra reservada def para crear la función
# def esPalindromo(palabra):
#     # Limpiar la cadena: eliminar espacios, convertir a minúsculas y quitar caracteres no alfanuméricos
#     palabra_limpia = ''.join(char.lower() for char in palabra if char.isalnum())
    
#     # Comprobar si es un palíndromo
#     return palabra_limpia == palabra_limpia[::-1]  # Compara la cadena limpia con su reverso

# # Solicitar entrada del usuario
# palabra = input('Escriba una palabra o frase: ')
# print(palabra, '¿es un palíndromo?', esPalindromo(palabra))#Si es palíndroma devuelve True // si no es palíndroma devuelve False

# Usamos la palabra reservada def para crear la función
def esPalindromo(palabra):
    # Limpiar la cadena: eliminar espacios, convertir a minúsculas y quitar caracteres no alfanuméricos
    palabra_limpia = ''.join(char.lower() for char in palabra if char.isalnum())
    
    # Comprobar si es un palíndromo
    return palabra_limpia == palabra_limpia[::-1]  # Compara la cadena limpia con su reverso

# Solicitar entrada del usuario
palabra = input('Escriba una palabra o frase: ')

# Evaluar y mostrar el mensaje adecuado
if esPalindromo(palabra):
    print(palabra,': Sí es palíndroma.')
else:
    print(palabra,': No es palíndroma.')
