from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from app.models import File
from typing import List
from ydata_profiling import ProfileReport
router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile):
    # Реализация загрузки файла и сохранения информации о колонках
    return {"filename": file.filename}

@router.get("/")
async def read_files():
    # Вернуть список файлов с информацией о колонках
    return []

@router.get("/{file_id}")
async def read_file(file_id: int, filter: str = None, sort: List[str] = None):
    # Реализация возврата данных из файла с фильтрацией и сортировкой
    return {"file_id": file_id}
@router.delete("/{file_id}")
async def delete_file(file_id: int):
    """
    Удалить файл с заданным ID
    """
    
    # Поиск файла по ID
    file = session.get(File, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Удаление файла
    session.delete(file)
    session.commit()

    return {"status": "success", "message": f"File with id {file_id} has been deleted"}