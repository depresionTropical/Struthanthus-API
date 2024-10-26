# Struthanthus-API

## Descripción
Struthanthus-API es un proyecto que utiliza FastAPI para recibir una imagen, procesarla y devolver la clase a la que pertenece la imagen.

## Características
- Recepción de imágenes.
- Procesamiento de imágenes para clasificación.
- Devolución de la clase de la imagen.

## Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/tu-usuario/Struthanthus-API.git
  ```
2. Navega al directorio del proyecto:
  ```bash
  cd Struthanthus-API
  ```
3. Crea un entorno virtual:
  ```bash
  python -m venv venv
  ```
4. Activa el entorno virtual:
  - En Windows:
    ```bash
    venv\Scripts\activate
    ```
  - En Unix o MacOS:
    ```bash
    source venv/bin/activate
    ```
5. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

## Uso

1. Inicia el servidor FastAPI:
  ```bash
  uvicorn main:app --reload
  ```
2. Envía una imagen a la API para clasificación:
  ```bash
  curl -X POST "http://127.0.0.1:8000/clasificar" -F "file=@ruta/a/tu/imagen.jpg"
  ```

## Endpoints

- `POST /clasificar`: Recibe una imagen y devuelve la clase a la que pertenece.

## Ejemplo de Respuesta
```json
{
  "clase": "nombre_de_la_clase"
}
```

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.