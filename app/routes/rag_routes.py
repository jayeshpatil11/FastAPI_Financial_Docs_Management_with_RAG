from fastapi import APIRouter
from ..rag import index_document, search

router = APIRouter(prefix="/rag")

@router.post("/index-document")
def index(doc_id: int, content: str):
    index_document(doc_id, content)
    return {"msg": "Indexed"}

@router.post("/search")
def rag_search(query: str):
    return {"results": search(query)}