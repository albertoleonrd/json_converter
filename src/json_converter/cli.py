"""Módulo para la interfaz de línea de comandos."""

import argparse
import sys
import json
from pathlib import Path

from json_converter import __version__
from json_converter.file_handler import (
    read_jsonl_file, write_json_file,
    read_json_file, write_jsonl_file,
    detect_file_format
)


def create_parser() -> argparse.ArgumentParser:
    """
    Crea el parser de argumentos para la interfaz de línea de comandos.
    
    Returns:
        Parser de argumentos configurado.
    """
    # Parser principal
    parser = argparse.ArgumentParser(
        prog="json_converter",
        description="Herramienta para convertir entre formatos JSON y JSONL"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    # Argumentos para el comando principal
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Ruta al archivo de entrada (JSON o JSONL)"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Ruta al archivo de salida (se convertirá al formato opuesto)"
    )
    
    # Ya no se utilizan subcomandos, ahora se usa detección automática
    
    return parser


# Las funciones to_json_command y to_jsonl_command han sido eliminadas
# ya que ahora se utiliza únicamente la detección automática


def convert_auto(args: argparse.Namespace) -> int:
    """
    Ejecuta la conversión automática detectando el formato del archivo de entrada.
    
    Args:
        args: Argumentos de línea de comandos.
        
    Returns:
        Código de salida (0 si todo va bien, otro valor en caso de error).
    """
    try:
        input_format = detect_file_format(args.input)
        
        if input_format == "jsonl":
            # Convertir de JSONL a JSON
            data = read_jsonl_file(args.input)
            write_json_file(data, args.output)
        elif input_format == "json":
            # Convertir de JSON a JSONL
            data = read_json_file(args.input)
            write_jsonl_file(data, args.output)
        else:
            print(f"Error: No se pudo determinar el formato del archivo {args.input}", file=sys.stderr)
            return 1
            
        print(f"Conversión exitosa: {args.input} -> {args.output}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main() -> int:
    """
    Función principal de la interfaz de línea de comandos.
    
    Returns:
        Código de salida (0 si todo va bien, otro valor en caso de error).
    """
    parser = create_parser()
    args = parser.parse_args()
    
    # Ejecutar la conversión automática
    if hasattr(args, "input") and hasattr(args, "output"):
        return convert_auto(args)
    else:
        # Mostrar ayuda si no se proporcionan los argumentos necesarios
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())