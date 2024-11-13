# API para E-commerce 🛒

Este proyecto es una API desarrollada en Python con FastAPI para un sistema de e-commerce. La API permite gestionar productos, categorías y usuarios, proporcionando endpoints para realizar operaciones CRUD.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **FastAPI**: Framework para la creación de APIs rápidas y eficientes.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **PostgreSQL**: Base de datos utilizada en el proyecto.

## Requisitos Previos

- Python 3.8 o superior
- Git
- PostgreSQL
- pip

## Instalación y Configuración

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

## 2. Crear y activar un entorno virtual

Windows
python -m venv venv
.\venv\Scripts\activate

Linux/MaxOS
python3 -m venv venv
source venv/bin/activate

## 3. Instalar dependencias

pip install -r requirements.txt

## 4. Configurar Variables de Entorno

Debes crear un archivo proyecto con la configuración de la base de datos:
por defecto lo que esta en el codigo:

host="localhost",
port=5432,
database="ecommerce_db",
user="postgres",
password="33pelu07",

## 5 . Ejecutar la aplicación

Inicia el servidor usando el siguiente comando:

uvicorn app.main:app --host 0.0.0.0 --port 8000

La aplicación estará disponible en: http://127.0.0.1:8000.
La documentación interactiva de la API se puede acceder en http://127.0.0.1:8000/docs (Swagger UI).

lgunos de los endpoints más importantes incluyen:

GET /products: Obtener todos los productos.
POST /products: Crear un nuevo producto.
GET /products/{id}: Obtener detalles de un producto específico.
PUT /products/{id}: Actualizar un producto.
DELETE /products/{id}: Eliminar un producto.

Contribuciones
Las contribuciones al proyecto son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

Realiza un fork del proyecto.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Agregar nueva funcionalidad').
Sube los cambios a tu fork (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto es de código abierto y está disponible bajo la licencia MIT.
