#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ollama 交互式聊天程序
支持连续对话
"""

import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/chat"

def chat(messages, model="llama2"):
    """
    使用 chat API 进行对话（支持上下文）
    
    Args:
        messages: 消息列表
        model: 模型名称
    """
    payload = {
        "model": model,
        "messages": messages,
        "stream": True
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()
        
        full_response = ""
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                if "message" in data:
                    content = data["message"].get("content", "")
                    print(content, end="", flush=True)
                    full_response += content
        
        print()
        return full_response
    
    except requests.exceptions.RequestException as e:
        print(f"\n错误: {e}")
        return None


def main():
    """交互式聊天主程序"""
    print("=" * 60)
    print("Ollama 交互式聊天")
    print("=" * 60)
    print("输入 'exit' 或 'quit' 退出")
    print("输入 'clear' 清空对话历史")
    print("-" * 60)
    
    # 对话历史
    messages = []
    
    # 可以修改为你已下载的模型
    model = "llama2"  # 或 "mistral", "codellama", "qwen" 等
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["exit", "quit"]:
                print("再见！")
                break
            
            if user_input.lower() == "clear":
                messages = []
                print("对话历史已清空")
                continue
            
            # 添加用户消息
            messages.append({
                "role": "user",
                "content": user_input
            })
            
            # 获取 AI 回复
            print("AI: ", end="", flush=True)
            response = chat(messages, model=model)
            
            if response:
                # 添加 AI 回复到历史
                messages.append({
                    "role": "assistant",
                    "content": response
                })
        
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n发生错误: {e}")


if __name__ == "__main__":
    main()

