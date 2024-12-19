from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Milvus
from config import MILVUS_CONFIG

def init_components():
    # 初始化大模型
    llm = ChatOpenAI(
        model_name="Qwen2.5-14B",
        temperature=0.7,
        model_kwargs={"response_format": {"type": "text"}},
        streaming=False
    )
    
    # 初始化嵌入模型
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L12-v2"
    )
    
    # 连接向量数据库
    db = Milvus(
        embedding_function=embedding,
        collection_name=MILVUS_CONFIG["collection"],
        connection_args={
            "host": MILVUS_CONFIG["host"],
            "port": MILVUS_CONFIG["port"]
        }
    )
    
    return llm, db