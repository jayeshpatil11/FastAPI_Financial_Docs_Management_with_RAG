Financial Document Management System with Semantic AnalysisAn AI-powered document management platform designed for the financial sector. This system enables organizations to store, manage, and analyze financial documents (invoices, reports, agreements) using Retrieval-Augmented Generation (RAG) and Semantic Search.

🚀 Key Features
Document Management: Secure upload and metadata tracking for financial files.RBAC (Role-Based Access Control): Granular permissions for Admin, Analyst, Auditor, and Client roles using JWT authentication.
Advanced RAG Pipeline:
  Text Extraction & Chunking: Semantic splitting of complex financial text.
  Vector Search: High-performance retrieval using Qdrant/FAISS.
  Financial Re-ranking: A two-stage retrieval process (Vector Search + Cross-Encoder Re-ranking) to ensure the highest relevance for financial queries.
Semantic Search: Context-aware search that understands financial terminology (e.g., "liquidity risk" or "debt-to-equity ratios").


🏗️ Architecture Overview
The system follows a modern AI microservice architecture:
  FastAPI: High-performance web framework for the API layer.
  PostgreSQL/MySQL: Relational database for metadata and user RBAC.
  Vector DB (Qdrant): Stores high-dimensional embeddings of document chunks.
  LangChain: Orchestrates the document processing and embedding pipeline.
  Sentence-Transformers: Powering the specialized financial embeddings and re-ranking.
  
  
🚦 Getting Started

Prerequisites
Python 3.9+
Qdrant (via Docker or Cloud)
Relational Database (PostgreSQL/SQLite)

Installation
1.Clone the repository:
Bashgit clone https://github.com/yourusername/financial-doc-mgmt.git
cd financial-doc-mgmt

2.Install dependencies:
Bashpip install -r requirements.txt

3.Set up Environment Variables:
Create a .env file:
Code snippet:
DATABASE_URL=postgresql://user:pass@localhost/dbname
VECTOR_DB_URL=http://localhost:6333
JWT_SECRET=your_super_secret_key

4.Run the application:
Bash
uvicorn main:app --reload


RAG Implementation Logic

The system uses a Bi-Encoder for the initial retrieval (top 20 results) followed by a Cross-Encoder (Re-ranker) to narrow down to the top 5 most relevant financial insights. This compensates for the nuance required in financial auditing where keyword matching often fails.
