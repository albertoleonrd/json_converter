"""Tests para el módulo de conversión."""

import json
import unittest
from io import StringIO

from json_converter.converter import jsonl_to_json, json_to_jsonl


class TestConverter(unittest.TestCase):
    """Pruebas para las funciones de conversión."""
    
    def test_jsonl_to_json(self):
        """Prueba la conversión de JSONL a JSON."""
        # Preparar datos de prueba
        jsonl_input = [
            '{"id": 1, "nombre": "Juan"}',
            '{"id": 2, "nombre": "María"}',
            '{"id": 3, "nombre": "Pedro"}'
        ]
        
        # Ejecutar la función
        result = jsonl_to_json(jsonl_input)
        
        # Verificar resultado
        expected = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "María"},
            {"id": 3, "nombre": "Pedro"}
        ]
        self.assertEqual(result, expected)
    
    def test_jsonl_to_json_empty_lines(self):
        """Prueba la conversión de JSONL a JSON con líneas vacías."""
        # Preparar datos de prueba con líneas vacías
        jsonl_input = [
            '{"id": 1, "nombre": "Juan"}',
            '',  # Línea vacía
            '{"id": 2, "nombre": "María"}',
            '   ',  # Línea con espacios
            '{"id": 3, "nombre": "Pedro"}'
        ]
        
        # Ejecutar la función
        result = jsonl_to_json(jsonl_input)
        
        # Verificar resultado
        expected = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "María"},
            {"id": 3, "nombre": "Pedro"}
        ]
        self.assertEqual(result, expected)
    
    def test_jsonl_to_json_invalid_json(self):
        """Prueba la conversión de JSONL a JSON con JSON inválido."""
        # Preparar datos de prueba con JSON inválido
        jsonl_input = [
            '{"id": 1, "nombre": "Juan"}',
            '{"id": 2, "nombre": "María"',  # JSON inválido (falta llave de cierre)
            '{"id": 3, "nombre": "Pedro"}'
        ]
        
        # Verificar que se lance la excepción
        with self.assertRaises(json.JSONDecodeError):
            jsonl_to_json(jsonl_input)
    
    def test_json_to_jsonl(self):
        """Prueba la conversión de JSON a JSONL."""
        # Preparar datos de prueba
        json_input = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "María"},
            {"id": 3, "nombre": "Pedro"}
        ]
        
        # Ejecutar la función
        result = list(json_to_jsonl(json_input))
        
        # Verificar resultado
        expected = [
            '{"id": 1, "nombre": "Juan"}',
            '{"id": 2, "nombre": "María"}',
            '{"id": 3, "nombre": "Pedro"}'
        ]
        self.assertEqual(result, expected)
    
    def test_json_to_jsonl_not_list(self):
        """Prueba la conversión de JSON a JSONL con entrada que no es lista."""
        # Preparar datos de prueba que no es una lista
        json_input = {"id": 1, "nombre": "Juan"}
        
        # Verificar que se lance la excepción
        with self.assertRaises(TypeError):
            list(json_to_jsonl(json_input))


if __name__ == "__main__":
    unittest.main()