"""Módulo para el manejo de archivos (I/O) de JSON y JSONL."""

import json
from pathlib import Path
from typing import List, Dict, Any, Iterator, Union, TextIO, Literal

from json_to_jsonl.converter import jsonl_to_json, json_to_jsonl


def read_jsonl_file(input_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Lee un archivo JSONL y lo convierte a una lista de objetos JSON.
    
    Args:
        input_path: Ruta al archivo JSONL de entrada.
        
    Returns:
        Lista de objetos JSON parseados.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        PermissionError: Si no hay permisos para leer el archivo.
        json.JSONDecodeError: Si alguna línea contiene JSON inválido.
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"El archivo {input_path} no existe")
    
    if not input_path.is_file():
        raise ValueError(f"{input_path} no es un archivo válido")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            return jsonl_to_json(f)
    except PermissionError:
        raise PermissionError(f"No hay permisos para leer el archivo {input_path}")


def write_json_file(data: List[Dict[str, Any]], output_path: Union[str, Path]) -> None:
    """
    Escribe una lista de objetos JSON a un archivo JSON.
    
    Args:
        data: Lista de objetos JSON.
        output_path: Ruta al archivo JSON de salida.
        
    Raises:
        PermissionError: Si no hay permisos para escribir el archivo.
    """
    output_path = Path(output_path)
    
    # Crear directorio padre si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except PermissionError:
        raise PermissionError(f"No hay permisos para escribir en el archivo {output_path}")


def read_json_file(input_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Lee un archivo JSON y valida que contenga un array de objetos.
    
    Args:
        input_path: Ruta al archivo JSON de entrada.
        
    Returns:
        Lista de objetos JSON parseados.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        PermissionError: Si no hay permisos para leer el archivo.
        json.JSONDecodeError: Si el archivo contiene JSON inválido.
        TypeError: Si el contenido no es una lista.
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"El archivo {input_path} no existe")
    
    if not input_path.is_file():
        raise ValueError(f"{input_path} no es un archivo válido")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if not isinstance(data, list):
                raise TypeError("El archivo JSON debe contener un array de objetos")
                
            return data
    except PermissionError:
        raise PermissionError(f"No hay permisos para leer el archivo {input_path}")


def detect_file_format(input_path: Union[str, Path]) -> Literal["json", "jsonl"]:
    """
    Detecta automáticamente si un archivo es JSON o JSONL basado en su contenido.
    
    Args:
        input_path: Ruta al archivo a analizar.
        
    Returns:
        "json" si el archivo parece ser JSON, "jsonl" si parece ser JSONL.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        PermissionError: Si no hay permisos para leer el archivo.
        ValueError: Si no se puede determinar el formato del archivo.
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"El archivo {input_path} no existe")
    
    if not input_path.is_file():
        raise ValueError(f"{input_path} no es un archivo válido")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            # Leer las primeras líneas del archivo (máximo 5)
            first_lines = []
            for _ in range(5):
                line = f.readline().strip()
                if line:  # Ignorar líneas vacías
                    first_lines.append(line)
                if not line or len(first_lines) >= 5:
                    break
            
            if not first_lines:
                raise ValueError(f"El archivo {input_path} está vacío o no contiene datos válidos")
            
            # Verificar si parece ser un archivo JSONL
            # Un archivo JSONL tiene objetos JSON válidos en cada línea
            if len(first_lines) > 1:
                try:
                    # Intentar parsear la primera línea como JSON
                    json.loads(first_lines[0])
                    # Si llegamos aquí, la primera línea es JSON válido
                    # Intentar con la segunda línea para confirmar que es JSONL
                    json.loads(first_lines[1])
                    return "jsonl"
                except json.JSONDecodeError:
                    pass
            
            # Verificar si parece ser un archivo JSON
            # Intentar leer todo el contenido como un único objeto JSON
            f.seek(0)  # Volver al inicio del archivo
            try:
                content = f.read()
                json_data = json.loads(content)
                if isinstance(json_data, list):
                    return "json"
            except json.JSONDecodeError:
                pass
            
            # Si llegamos aquí, intentar una última verificación para JSONL
            # Algunos archivos JSONL pueden tener solo una línea
            if len(first_lines) == 1:
                try:
                    json.loads(first_lines[0])
                    return "jsonl"
                except json.JSONDecodeError:
                    pass
            
            raise ValueError(f"No se pudo determinar el formato del archivo {input_path}")
    except PermissionError:
        raise PermissionError(f"No hay permisos para leer el archivo {input_path}")


def write_jsonl_file(data: List[Dict[str, Any]], output_path: Union[str, Path]) -> None:
    """
    Escribe una lista de objetos JSON a un archivo JSONL.
    
    Args:
        data: Lista de objetos JSON.
        output_path: Ruta al archivo JSONL de salida.
        
    Raises:
        PermissionError: Si no hay permisos para escribir el archivo.
        TypeError: Si el input no es una lista.
    """
    output_path = Path(output_path)
    
    # Crear directorio padre si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for line in json_to_jsonl(data):
                f.write(line + '\n')
    except PermissionError:
        raise PermissionError(f"No hay permisos para escribir en el archivo {output_path}")