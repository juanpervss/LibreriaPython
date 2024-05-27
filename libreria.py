import json

class Libreria:
    """
    Representa una librería que contiene una colección de libros.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Libreria.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la librería.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título en la librería.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Una lista de libros que coinciden con el título especificado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por un autor específico en la librería.

        Args:
            autor (str): El autor cuyos libros se desean buscar.

        Returns:
            list: Una lista de libros escritos por el autor especificado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la librería por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro ha sido eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda los libros de la librería en un archivo JSON.

        Args:
            archivo (str): La ruta del archivo donde se guardarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga los libros desde un archivo JSON a la librería.

        Args:
            archivo (str): La ruta del archivo desde donde se cargarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido cargados, o que el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Ejemplo de uso:
mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))


# Unit Test
import unittest

class TestLibreria(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.libros[0]['titulo'], "Cien años de soledad")
        self.assertEqual(self.libreria.libros[0]['autor'], "Gabriel García Márquez")
        self.assertEqual(self.libreria.libros[0]['genero'], "Novela")
        self.assertEqual(self.libreria.libros[0]['anio'], 1967)

    def test_buscar_libro(self):
        libros_encontrados = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(len(libros_encontrados), 1)
        self.assertEqual(libros_encontrados[0]['titulo'], "Cien años de soledad")

    def test_buscar_por_autor(self):
        libros_autor = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(len(libros_autor), 1)
        self.assertEqual(libros_autor[0]['autor'], "Gabriel García Márquez")

    def test_eliminar_libro(self):
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)

    def test_guardar_cargar_libros(self):
        self.libreria.guardar_libros('test_libreria.json')
        self.libreria_cargada = Libreria()
        self.libreria_cargada.cargar_libros('test_libreria.json')
        self.assertEqual(len(self.libreria_cargada.libros), 1)
        self.assertEqual(self.libreria_cargada.libros[0]['titulo'], "Cien años de soledad")

if __name__ == '__main__':
    unittest.main()

# Github: git commit -m "a"