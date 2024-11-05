import unittest
from charfun import esPalindromo  # Importa la función esPalindromo del archivo charfun.py

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
        self.assertTrue(esPalindromo("No 'lemon', no melon"), "La frase con apóstrofes debería ser palíndroma")

    # Prueba con espacios extra
    def test_frase_con_espacios(self):
        self.assertTrue(esPalindromo("     Anita    lava    la tina    "), "Los espacios adicionales no deberían afectar el resultado")

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
