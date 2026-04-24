

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize Qdrant
qdrant = QdrantClient(":memory:")

COLLECTION_NAME = "docs"

# Create collection
qdrant.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=768, distance=Distance.COSINE)
)

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)


# Index Documents
def index_document(doc_id: int, content: str):
    vector = embedding_model.embed_query(content)

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=doc_id,
                vector=vector,
                payload={"content": content}
            )
        ]
    )


#Search Function
def search(query: str):
    q_vector = embedding_model.embed_query(query)

    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=q_vector,
        limit=5
    )

    return [r.payload for r in results.points]