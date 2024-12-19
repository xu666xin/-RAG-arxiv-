from langchain.prompts import PromptTemplate
from query_processor import optimize_query, search_papers, format_papers
from answer_gen import generate_answer

def evaluate_answer(llm, query, answer):
    """评估答案质量"""
    template = """
    评估以下答案的质量（1-10分）：
    问题：{query}
    答案：{answer}
    
    请给出：
    1. 分数（1-10）
    2. 不足之处
    3. 建议改进的方向
    """
    
    prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=template
    )
    
    try:
        evaluation = llm.predict(prompt.format(query=query, answer=answer))
        return evaluation
    except Exception as e:
        return "评估失败: " + str(e)

def get_score(evaluation):
    """从评估结果中提取分数"""
    try:
        if "分数：" in evaluation:
            score = int(evaluation.split("分数：")[1][0])
            return score
        return 0
    except Exception:
        return 0

def iterative_search(llm, db, query, max_iterations=3, min_score=7):
    """迭代式查询"""
    print(f"\n开始处理问题: {query}")
    
    # 记录最佳答案和分数
    best_answer = None
    best_score = 0
    
    for i in range(max_iterations):
        print(f"\n迭代 {i+1}:")
        
        # 优化查询
        optimized = optimize_query(llm, query)
        papers = search_papers(db, optimized)
        context = format_papers(papers)
        answer = generate_answer(llm, query, context)
        
        # 评估答案
        evaluation = evaluate_answer(llm, query, answer)
        print(f"\n答案评估:\n{evaluation}")
        
        # 获取当前答案的分数
        current_score = get_score(evaluation)
        
        # 更新最佳答案
        if current_score > best_score:
            best_score = current_score
            best_answer = answer
            print(f"发现更好的答案！分数：{best_score}")
        
        # 如果达到最低分数要求，直接返回
        if current_score >= min_score:
            return answer
    
    # 如果达到最大迭代次数，返回最佳答案
    print(f"\n达到最大迭代次数，返回最佳答案（分数：{best_score}）")
    return best_answer or answer  # 如果没有找到任何有效答案，返回最后一个答案