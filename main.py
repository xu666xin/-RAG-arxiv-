import json
import argparse
from models import init_components
from query_processor import optimize_query, search_papers, format_papers
from answer_gen import generate_answer
from iterative_search import iterative_search

def interactive_mode(llm, db):
    """交互式问答模式"""
    print("欢迎使用 arXiv 问答系统！(输入 'quit' 退出)")
    
    while True:
        query = input("\n请输入问题：").strip()
        if query.lower() == 'quit':
            break
            
        try:
            answer = iterative_search(llm, db, query)
            print("\n最终回答:", answer)
        except Exception as e:
            print(f"发生错误: {str(e)}")

def process_questions(llm, db, questions_file, output_file):
    """批处理问答模式"""
    print(f"从 {questions_file} 读取问题...")
    
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    for item in questions:
        try:
            query = item['question']
            print(f"\n处理问题: {query}")
            
            answer = iterative_search(llm, db, query)
            
            item['answer'] = answer
            print("已生成答案")
            
        except Exception as e:
            print(f"处理问题时发生错误: {str(e)}")
            item['answer'] = f"处理错误: {str(e)}"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"\n所有答案已保存到 {output_file}")

def main():
    # 解析命令行参数
    # 输入：python main.py --batch --input questions.jsonl --output answers.json   
    # 获取answer.json 文件 
    parser = argparse.ArgumentParser(description='arXiv 问答系统')
    parser.add_argument('--batch', action='store_true',
                      help='运行批处理模式处理问题文件')
    parser.add_argument('--input', default='questions.jsonl',
                      help='输入问题文件路径')
    parser.add_argument('--output', default='answers.json',
                      help='输出答案文件路径')
    args = parser.parse_args()
    
    # 初始化系统组件
    print("初始化系统组件...")
    llm, db = init_components()
    
    if args.batch:
        # 批处理模式
        process_questions(llm, db, args.input, args.output)
    else:
        # 交互式模式
        interactive_mode(llm, db)

if __name__ == "__main__":
    main()