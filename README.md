# JSON Converter

Herramienta de línea de comandos para convertir eficientemente entre formatos JSON Lines (JSONL) y JSON estándar.

## Características

- Conversión de JSONL a JSON: Transforma archivos donde cada línea es un objeto JSON a un único archivo JSON con un array de objetos.
- Conversión de JSON a JSONL: Convierte un archivo JSON con un array de objetos a un archivo de texto donde cada línea es un objeto JSON.
- Manejo eficiente de archivos grandes mediante procesamiento por streaming.
- Validación robusta y mensajes de error claros.

## Requisitos

- Python 3.8 o superior

## Instalación

### 1. Verificar la instalación de Python

Antes de comenzar, asegúrate de tener Python 3.8 o superior instalado correctamente:

1. Abre una terminal (PowerShell o Símbolo del sistema) y verifica si Python está instalado:

```bash
python --version
```

Si ves un mensaje como "Python 3.x.x", Python está instalado correctamente. Si recibes un error, sigue estos pasos:

#### Si Python no está instalado:

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, **ASEGÚRATE DE MARCAR LA OPCIÓN "Add Python to PATH"**
3. Reinicia tu terminal después de la instalación

#### Si Python está instalado pero no se reconoce el comando:

Puede que Python esté instalado pero no esté en tu PATH. Puedes:

- Usar la ruta completa al ejecutable de Python. Busca dónde está instalado (normalmente en `C:\Python3x\` o `C:\Users\[usuario]\AppData\Local\Programs\Python\Python3x\`)
- Agregar Python al PATH manualmente:
  1. Busca "Variables de entorno" en el menú de inicio
  2. Haz clic en "Variables de entorno..."
  3. En la sección "Variables del sistema", selecciona "Path" y haz clic en "Editar"
  4. Haz clic en "Nuevo" y agrega la ruta a la carpeta de Python y también a la subcarpeta Scripts
  5. Haz clic en "Aceptar" en todas las ventanas
  6. Reinicia tu terminal

### 2. Clonar o descargar este repositorio:

```bash
git clone https://github.com/albertoleonrd/json_converter.git
cd json_converter
```

### 3. Instalar el paquete en modo desarrollo:

```bash
# Instalar usando pip
pip install -e .
```

**Nota**: Si el comando pip no funciona, asegúrate de que Python esté correctamente instalado y agregado al PATH del sistema.

## Uso Básico

### Modo Automático (Recomendado)

La herramienta detecta automáticamente el formato del archivo de entrada y realiza la conversión apropiada:

```bash
json_converter --input archivo.jsonl --output archivo.json
```

o

```bash
json_converter --input archivo.json --output archivo.jsonl
```

### Ver la ayuda

```bash
json_converter --help
```

## Ejemplos

En el directorio `examples/` encontrarás archivos de ejemplo en ambos formatos:

- `ejemplo.jsonl`: Archivo en formato JSONL (cada línea es un objeto JSON)
- `ejemplo.json`: Archivo en formato JSON (array de objetos)

Puedes probar la herramienta con estos archivos:

```bash
# Usando el modo automático
json_converter --input examples/ejemplo.jsonl --output resultado.json
json_converter --input examples/ejemplo.json --output resultado.jsonl
```

### Ejemplo de contenido JSONL (ejemplo.jsonl)

```
{"id": 1, "nombre": "Juan", "edad": 30}
{"id": 2, "nombre": "María", "edad": 25}
{"id": 3, "nombre": "Pedro", "edad": 35}
```

### Ejemplo de contenido JSON (ejemplo.json)

```json
[
  {"id": 1, "nombre": "Juan", "edad": 30},
  {"id": 2, "nombre": "María", "edad": 25},
  {"id": 3, "nombre": "Pedro", "edad": 35}
]
```

## Ejecución de Tests

Para ejecutar las pruebas unitarias:

```bash
python -m unittest discover tests
```

## Manejo de Errores

La herramienta proporciona mensajes de error claros para situaciones comunes:

- Archivo de entrada no encontrado
- Permisos insuficientes
- JSON inválido
- Formato incorrecto (por ejemplo, si el archivo JSON no contiene un array como elemento principal)

Si encuentras algún problema, asegúrate de verificar:

1. Que los archivos existan y tengan los permisos correctos
2. Que el formato de los archivos sea el esperado
3. Que tengas suficiente espacio en disco para la operación

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un nuevo Pull Request