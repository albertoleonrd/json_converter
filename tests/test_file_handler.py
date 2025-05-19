"""Tests para el módulo de manejo de archivos."""

import json
import os
import tempfile
import unittest
from pathlib import Path

from json_to_jsonl.file_handler import (
    read_jsonl_file, write_json_file,
    read_json_file, write_jsonl_file
)


class TestFileHandler(unittest.TestCase):
    """Pruebas para las funciones de manejo de archivos."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Crear directorio temporal para los archivos de prueba
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)
    
    def tearDown(self):
        """Limpieza después de las pruebas."""
        # Eliminar directorio temporal
        self.temp_dir.cleanup()
    
    def test_read_write_jsonl_file(self):
        """Prueba la lectura y escritura de archivos JSONL."""
        # Datos de prueba
        test_data = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "María"},
            {"id": 3, "nombre": "Pedro"}
        ]
        
        # Ruta del archivo de prueba
        test_file = self.test_dir / "test.jsonl"
        
        # Escribir datos en formato JSONL
        write_jsonl_file(test_data, test_file)
        
        # Verificar que el archivo existe
        self.assertTrue(test_file.exists())
        
        # Leer el archivo JSONL
        result = read_jsonl_file(test_file)
        
        # Verificar que los datos leídos son iguales a los escritos
        self.assertEqual(result, test_data)
    
    def test_read_write_json_file(self):
        """Prueba la lectura y escritura de archivos JSON."""
        # Datos de prueba
        test_data = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "María"},
            {"id": 3, "nombre": "Pedro"}
        ]
        
        # Ruta del archivo de prueba
        test_file = self.test_dir / "test.json"
        
        # Escribir datos en formato JSON
        write_json_file(test_data, test_file)
        
        # Verificar que el archivo existe
        self.assertTrue(test_file.exists())
        
        # Leer el archivo JSON
        result = read_json_file(test_file)
        
        # Verificar que los datos leídos son iguales a los escritos
        self.assertEqual(result, test_data)
    
    def test_read_nonexistent_file(self):
        """Prueba la lectura de un archivo que no existe."""
        # Ruta de un archivo que no existe
        nonexistent_file = self.test_dir / "nonexistent.json"
        
        # Verificar que se lance la excepción
        with self.assertRaises(FileNotFoundError):
            read_json_file(nonexistent_file)
        
        with self.assertRaises(FileNotFoundError):
            read_jsonl_file(nonexistent_file)
    
    def test_read_invalid_json_file(self):
        """Prueba la lectura de un archivo JSON inválido."""
        # Ruta del archivo de prueba
        test_file = self.test_dir / "invalid.json"
        
        # Escribir JSON inválido
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write('{"id": 1, "nombre": "Juan"')  # JSON inválido
        
        # Verificar que se lance la excepción
        with self.assertRaises(json.JSONDecodeError):
            read_json_file(test_file)
    
    def test_read_json_not_array(self):
        """Prueba la lectura de un archivo JSON que no contiene un array."""
        # Ruta del archivo de prueba
        test_file = self.test_dir / "not_array.json"
        
        # Escribir JSON que no es un array
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write('{"id": 1, "nombre": "Juan"}')  # Objeto JSON, no array
        
        # Verificar que se lance la excepción
        with self.assertRaises(TypeError):
            read_json_file(test_file)


if __name__ == "__main__":
    unittest.main()