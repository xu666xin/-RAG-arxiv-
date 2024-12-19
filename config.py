import os

# OpenAI 配置
os.environ["OPENAI_API_KEY"] = "None"
os.environ["OPENAI_API_BASE"] = "http://10.58.0.2:8000/v1"

# Milvus 配置
MILVUS_CONFIG = {
    "host": "10.58.0.2",
    "port": "19530",
    "collection": "arxiv",
    "dim": 384,  # all-MiniLM-L12-v2 的向量维度是 384
}                           