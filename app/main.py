from fastapi import FastAPI
from .database import Base, engine
from .routes import auth_routes, document_routes, rag_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(document_routes.router)
app.include_router(rag_routes.router)

@app.get("/")
def root():
    return {"msg": "Financial RAG API Running"}


#python  -m venv envname
#source venv/scripts/activate
#pip install -r requirements.txt
#python -m uvicorn app.main:app --reload