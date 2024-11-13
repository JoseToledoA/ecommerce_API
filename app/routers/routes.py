from fastapi import APIRouter, HTTPException, Query
from app.database.db import POSTGRESSQL_DB
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Crear el enrutador de FastAPI
router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Endpoint para obtener productos filtrados por categoría
@router.get("/all_products", tags=["Products"])
async def get_all_products(category: str = None):
    """
    Retrieve all products from the database, optionally filtered by category.
    """
    db_client = POSTGRESSQL_DB()  # Aquí debes inicializar tu cliente DB
    query = """
        SELECT * FROM products
    """
    # Ejecutar la consulta
    results = db_client.fetch_all_data(query)

    # Verificar si se obtuvieron resultados
    if results is None or len(results) == 0:
        raise HTTPException(status_code=404, detail="No products found.")

    return results


# Endpoint para obtener productos filtrados por categoría
@router.get("/all_products/by_category", tags=["Products"])
async def get_all_products(category: str = None):
    """
    Retrieve all products from the database, optionally filtered by category.
    """
    db_client = POSTGRESSQL_DB()  # Aquí debes inicializar tu cliente DB
    query = """
        SELECT * FROM products
    """

    # Si se proporciona una categoría, agregamos el filtro al query
    if category:
        query += f" WHERE category_id = '{category}'"

    # Ejecutar la consulta
    results = db_client.fetch_all_data(query)

    # Verificar si se obtuvieron resultados
    if results is None or len(results) == 0:
        raise HTTPException(status_code=404, detail="No products found.")

    return results


# Endpoint para obtener productos ordenados por precio
@router.get("/products/sorted_by_price", tags=["Products"])
async def get_products_sorted_by_price(
    order: str = Query(
        "asc",
        regex="^(asc|desc)$",
        description="Orden 'asc' para ascendente o 'desc' para descendente",
    ),
    category_id: Optional[int] = None,
):
    """
    Retrieve products sorted by price. Optionally filter by category.

    - **order**: "asc" para orden ascendente o "desc" para orden descendente.
    - **category_id**: ID de la categoría para filtrar los productos (opcional).
    """
    db_client = POSTGRESSQL_DB()  # Inicializa tu cliente de base de datos

    # Crear la consulta base
    query = "SELECT * FROM products"

    # Agregar filtro por categoría si se proporciona
    if category_id:
        query += f" WHERE category_id = {category_id}"

    # Agregar ordenamiento por precio
    query += f" ORDER BY price {'ASC' if order == 'asc' else 'DESC'}"

    # Ejecutar la consulta
    results = db_client.fetch_all_data(query)

    # Verificar si se obtuvieron resultados
    if not results:
        raise HTTPException(status_code=404, detail="No products found.")

    return results


@router.post("/create_user", tags=["Users"])
async def create_user(user: UserCreate):
    """
    Crea un nuevo usuario en el sistema.
    """
    db_client = POSTGRESSQL_DB()

    # Verificar si el usuario ya existe
    query_check_user = f"SELECT * FROM users WHERE email = '{user.email}'"
    existing_user = db_client.fetch_one_data(query_check_user)

    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")

    # Insertar el nuevo usuario con la contraseña sin modificar
    query_insert_user = f"""
        INSERT INTO users (username, email, password_hash)
        VALUES ('{user.username}', '{user.email}', '{user.password}')
    """
    db_client.execute_query(query_insert_user)

    return {"message": "Usuario creado exitosamente"}
