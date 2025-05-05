"""Módulo para la lógica de conversión entre formatos JSON y JSONL."""

import json
from typing import List, Dict, Any, Iterator, Union, TextIO


def jsonl_to_json(jsonl_lines: Iterator[str]) -> List[Dict[str, Any]]:
    """
    Convierte líneas de formato JSONL a una lista de objetos JSON.
    
    Args:
        jsonl_lines: Iterador de líneas en formato JSONL.
        
    Returns:
        Lista de objetos JSON parseados.
        
    Raises:
        json.JSONDecodeError: Si alguna línea contiene JSON inválido.
    """
    result = []
    
    for line_number, line in enumerate(jsonl_lines, 1):
        line = line.strip()
        if not line:  # Ignorar líneas vacías
            continue
            
        try:
            obj = json.loads(line)
            result.append(obj)
        except json.JSONDecodeError as e:
            # Mejorar el mensaje de error con el número de línea
            raise json.JSONDecodeError(
                f"Error en línea {line_number}: {e.msg}", 
                e.doc, 
                e.pos
            ) from e
            
    return result


def json_to_jsonl(json_array: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Convierte una lista de objetos JSON a formato JSONL.
    
    Args:
        json_array: Lista de objetos JSON.
        
    Returns:
        Iterador de líneas en formato JSONL.
        
    Raises:
        TypeError: Si el input no es una lista.
    """
    if not isinstance(json_array, list):
        raise TypeError("El contenido JSON debe ser una lista de objetos")
        
    for item in json_array:
        yield json.dumps(item, ensure_ascii=False)