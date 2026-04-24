from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import Document
from ..deps import get_db, get_current_user
from ..rbac import check_permission
from ..rag import index_document

router = APIRouter(prefix="/documents")
'''
# ✅ SINGLE CLEAN UPLOAD API
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Permission check
    check_permission(user.role, "upload")

    # Save in DB
    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    # 🔥 Store in vector DB (RAG)
    index_document(doc.id, content)

    return {"msg": "Uploaded & Indexed successfully"}

'''
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    # 🔥 Index into RAG
    index_document(doc.id, content)

    return {"msg": "Uploaded + Indexed"}


# ✅ Get Documents
@router.get("/")
def get_docs(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "view")
    return db.query(Document).all()


# ✅ Metadata Search
@router.get("/search")
def search_docs(
    company_name: str = "",
    document_type: str = "",
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    query = db.query(Document)

    if company_name:
        query = query.filter(Document.company_name == company_name)

    if document_type:
        query = query.filter(Document.document_type == document_type)

    return query.all()


'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import Document
from ..deps import get_db, get_current_user
from ..rbac import check_permission
from ..rag import index_document

router = APIRouter(prefix="/documents")


# ✅ Upload Document (ONLY ONE FUNCTION)
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    # 🔥 Index in vector DB
    index_document(doc.id, content)

    return {"msg": "Uploaded successfully"}


# ✅ Get Documents
@router.get("/")
def get_docs(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "view")
    return db.query(Document).all()


# ✅ Metadata Search
@router.get("/search")
def search_docs(
    company_name: str = "",
    document_type: str = "",
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "search")

    query = db.query(Document)

    if company_name:
        query = query.filter(Document.company_name == company_name)

    if document_type:
        query = query.filter(Document.document_type == document_type)

    return query.all()
'''



'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import Document
from ..deps import get_db, get_current_user
from ..rbac import check_permission

router = APIRouter(prefix="/documents")

#Upload Document (FIXED)
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # ✅ FIXED HERE
):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    check_permission(user.role, "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {"msg": "Uploaded successfully"}


#Get Documents
@router.get("/")
def get_docs(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "view")
    return db.query(Document).all()


#Metadata Search
@router.get("/search")
def search_docs(
    company_name: str = "",
    document_type: str = "",
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # optional but better
):
    query = db.query(Document)

    if company_name:
        query = query.filter(Document.company_name == company_name)

    if document_type:
        query = query.filter(Document.document_type == document_type)

    return query.all()


from ..rag import index_document

@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    # 🔥 Add this line
    index_document(doc.id, content)

    return {"msg": "Uploaded"}

'''














'''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Document
from ..deps import get_db, get_current_user
from ..rbac import check_permission

router = APIRouter(prefix="/documents")


#Upload Document
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user["role"], "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user["user_id"]
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {"msg": "Document uploaded", "id": doc.id}


'''
'''
@router.post("/upload")
def upload(
    title: str,
    company_name: str,
    document_type: str,
    content: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # 🔥 FIXED (not oauth2_scheme)
):
    check_permission(user.role, "upload")

    doc = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        content=content,
        uploaded_by=user.id
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {"msg": "Document uploaded", "id": doc.id}
'''
'''

#Get All Documents
@router.get("/")
def get_docs(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    check_permission(user.role, "view")
    return db.query(Document).all()


#Metadata Search
@router.get("/search")
def search_docs(
    company_name: str = "",
    document_type: str = "",
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   # 🔥 ADD THIS (secure route)
):
    check_permission(user.role, "view")

    query = db.query(Document)

    if company_name:
        query = query.filter(Document.company_name == company_name)

    if document_type:
        query = query.filter(Document.document_type == document_type)

    return query.all()
'''