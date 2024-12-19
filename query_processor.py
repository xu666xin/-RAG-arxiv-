from langchain.prompts import PromptTemplate

def optimize_query(llm, query):
    """优化用户查询"""
    template = """
    你是一个专业的学术论文检索专家。请将用户的问题转化为更适合在学术论文数据库中检索的形式。
    要求：
    1. 使用学术化的表达
    2. 包含关键概念和术语
    3. 避免过于口语化的表达
    4. 必须是一个简短的查询语句，不要解释
    
    用户问题：{query}
    优化后的查询：
    """
    
    prompt = PromptTemplate(
        input_variables=["query"],
        template=template
    )
    
    try:
        optimized = llm.predict(prompt.format(query=query))
        # 清理多余的换行和说明文字
        optimized = optimized.split('\n')[0].strip()
        return optimized
    except Exception as e:
        print(f"查询优化失败: {str(e)}")
        return query

def search_papers(db, query, k=3):
    """从向量数据库检索相关论文"""
    return db.similarity_search(query, k=k)

def format_papers(papers):
    """格式化论文信息"""
    return "\n".join([
        f"标题：{paper.metadata['title']}\n"
        f"作者：{paper.metadata['authors']}\n"
        f"分类：{paper.metadata['categories']}\n"
        f"摘要：{paper.page_content}\n"
        f"ID：{paper.metadata['id']}\n"
        "---"
        for paper in papers
    ])