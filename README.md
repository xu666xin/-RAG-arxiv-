# arXiv 问答系统

基于 RAG (Retrieval-Augmented Generation) 的学术论文问答系统。

纯靠cursor生成，milvus数据库是学校的地址

## 功能特点

- 支持交互式问答和批处理模式
- 使用迭代式搜索优化答案质量
- 集成向量数据库进行相似度检索
- 支持答案质量评估

## 安装

1. 克隆仓库：

```bash
git clone [repository-url]
```

2.创建虚拟环境

```bash
python -m venv rag_env
source rag_env/bin/activate
```

3.安装依赖

```bash
pip install -r requirements.txt
```

## 使用

1. 交互式问答

```bash
python main.py
```

2. 批处理模式

```bash
python main.py --batch --input questions.jsonl --output answers.json
```

## 配置

修改 `config.py` 配置文件：
- OpenAI API 设置
- Milvus 数据库连接信息

## 项目结构

- `main.py`: 主程序入口
- `models.py`: 模型初始化
- `query_processor.py`: 查询处理
- `answer_gen.py`: 答案生成
- `iterative_search.py`: 迭代搜索

