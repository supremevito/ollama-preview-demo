#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ollama API 调用示例
最简单的方式调用本地 Ollama 接口
"""

import requests
import json

# Ollama 默认地址
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def chat_with_ollama(prompt, model="llama2"):
    """
    调用 Ollama API 进行对话
    
    Args:
        prompt: 用户输入的问题
        model: 使用的模型名称，默认 llama2
    
    Returns:
        AI 的回复内容
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # 不使用流式输出，直接返回完整结果
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "")
    
    except requests.exceptions.RequestException as e:
        return f"请求错误: {e}"


def chat_with_ollama_stream(prompt, model="llama2"):
    """
    调用 Ollama API 进行对话（流式输出）
    
    Args:
        prompt: 用户输入的问题
        model: 使用的模型名称
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True  # 启用流式输出
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
        response.raise_for_status()
        
        print("AI 回复: ", end="", flush=True)
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                content = data.get("response", "")
                print(content, end="", flush=True)
        
        print()  # 换行
    
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("Ollama API 调用示例")
    print("=" * 50)
    
    # 示例 1: 普通调用（非流式）
    print("\n【示例 1】普通调用（一次性返回）")
    question = "什么是人工智能？用一句话回答。(中文)"
    print(f"问题: {question}")
    answer = chat_with_ollama(question, model="llama2")
    print(f"回答: {answer}")
    
    # 示例 2: 流式调用
    print("\n【示例 2】流式调用（逐字输出）")
    question2 = "介绍一下 Python 编程语言。"
    print(f"问题: {question2}")
    chat_with_ollama_stream(question2, model="llama2")
    
    print("\n" + "=" * 50)
    print("提示: 请确保 Ollama 服务已启动")
    print("启动命令: ollama serve")
    print("查看可用模型: ollama list")
    print("=" * 50)

