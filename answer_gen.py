from langchain.prompts import PromptTemplate

def generate_answer(llm, query, context):
    """生成回答"""
    template = """
    你是一个专业的学术问答助手。请基于提供的论文信息回答用户问题。
    
    要求：
    1. 如果论文信息与问题相关，请基于论文内容给出详细回答
    2. 如果论文信息与问题无关，请说明这一点，并基于你的知识给出准确的回答
    3. 回答要有逻辑性和结构性
    4. 在回答末尾列出所有参考论文的标题和作者
    
    用户问题：{query}
    
    参考论文信息：
    {context}
    
    请按以下格式回答：
    1. 主要回答
    2. 补充说明（如果需要）
    3. 参考文献
    """
    
    prompt = PromptTemplate(
        input_variables=["query", "context"],
        template=template
    )
    
    try:
        response = llm.predict(prompt.format(query=query, context=context))
        return response
    except Exception as e:
        print(f"生成答案时出错: {str(e)}")
        return str(e)