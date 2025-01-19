import unittest
from charfun import esPalindromo  # Importa la función esPalindromo del archivo charfun.py
import random
import string

class TestCharFun(unittest.TestCase):
    # Prueba para "Anita lava la tina"
    def test_frase_palindroma(self):
        self.assertTrue(esPalindromo("Anita lava la tina"), "La frase debería ser palíndroma")

    # Prueba con una frase que no es palíndroma
    def test_frase_no_palindroma(self):
        self.assertFalse(esPalindromo("Esto no es un palíndromo"), "La frase no debería ser palíndroma")

    # Prueba con una cadena vacía (que se considera palíndroma)
    def test_cadena_vacia(self):
        self.assertTrue(esPalindromo(""), "Una cadena vacía debería considerarse palíndroma")

    # Prueba con un número palíndromo
    def test_numeros_palindromos(self):
        self.assertTrue(esPalindromo("12321"), "El número debería ser palíndromo")
        self.assertFalse(esPalindromo("12345"), "El número no debería ser palíndromo")

    # Prueba con puntuación y caracteres especiales
    def test_frase_con_puntuacion(self):
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"), "La frase con puntuación debería ser palíndroma")
        self.assertTrue(esPalindromo("Dábale arroz a la zorra el abad"), "La frase con tildes debería ser palíndroma")

    # Prueba con espacios extra
    def test_frase_con_espacios(self):
        self.assertTrue(esPalindromo("     Anita    lava    la tina    "), "Los espacios adicionales no deberían afectar el resultado")

    # Prueba con parámetros no válidos
    def test_parametros_no_validos(self):
        with self.assertRaises(ValueError, msg="Se esperaba un ValueError si el parámetro no es una cadena"):
            esPalindromo(12345)  # Número entero
        with self.assertRaises(ValueError, msg="Se esperaba un ValueError si el parámetro no es una cadena"):
            esPalindromo(None)  # Valor nulo
        with self.assertRaises(ValueError, msg="Se esperaba un ValueError si el parámetro no es una cadena"):
            esPalindromo(["anita", "lava", "la", "tina"])  # Lista

    # Prueba con una lista de palabras aleatorias
    def test_lista_palabras_aleatorias(self):
        palabras = [
            ''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(100)
        ]
        for palabra in palabras:
            self.assertIsInstance(esPalindromo(palabra), bool, "La función debería devolver un booleano para cualquier entrada válida")

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
