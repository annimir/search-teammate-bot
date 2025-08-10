import firebase_admin
from firebase_admin import credentials, firestore
from typing import Dict, Any, Optional

# Инициализация Firebase
def initialize_firebase():
    # Проверяем, инициализировано ли приложение (чтобы избежать ошибок при повторной инициализации)
    if not firebase_admin._apps:
        # Указываем путь к сервисному ключу (он должен быть в папке `server/`)
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)

    # Возвращаем клиент Firestore
    return firestore.client()

# Получаем экземпляр базы данных (глобальная переменная для удобства)
db = initialize_firebase()

# Примеры CRUD-операций:

### 1. Добавление документа
def add_data(collection: str, document_id: str, data: Dict[str, Any]) -> None:
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.set(data)

### 2. Получение документа по ID
def get_data(collection: str, document_id: str) -> Optional[Dict[str, Any]]:
    doc_ref = db.collection(collection).document(document_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

### 3. Обновление документа
def update_data(collection: str, document_id: str, updates: Dict[str, Any]) -> None:
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(updates)

### 4. Удаление документа
def delete_data(collection: str, document_id: str) -> None:
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()

### 5. Получение всех документов из коллекции
def get_all_documents(collection: str) -> list[Dict[str, Any]]:
    docs = db.collection(collection).stream()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]