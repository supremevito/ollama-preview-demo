# Ollama Python 调用示例

这是一个最简单的 Python 调用本地 Ollama 接口的示例项目。

## 📋 前置要求

1. **安装 Ollama**
   ```bash
   # macOS
   brew install ollama
   
   # 或从官网下载
   # https://ollama.ai/download
   ```

2. **启动 Ollama 服务**
   ```bash
   ollama serve
   ```

3. **下载模型**
   ```bash
   # 下载 llama2 模型（推荐）
   ollama pull llama2
   
   # 或其他模型
   ollama pull mistral
   ollama pull codellama
   ollama pull qwen
   ```

4. **安装 Python 依赖**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 使用方法

### 方式 1: 简单示例（ollama_demo.py）

包含两种调用方式：
- 普通调用：一次性返回完整结果
- 流式调用：逐字输出（类似 ChatGPT 效果）

```bash
python ollama_demo.py
```

### 方式 2: 交互式聊天（ollama_chat.py）

支持连续对话，保留上下文：

```bash
python ollama_chat.py
```

**功能：**
- 输入问题进行对话
- 输入 `clear` 清空对话历史
- 输入 `exit` 或 `quit` 退出

## 📡 API 说明

### 1. Generate API（生成接口）

**端点：** `http://localhost:11434/api/generate`

**请求示例：**
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama2",
        "prompt": "什么是人工智能？",
        "stream": False
    }
)

result = response.json()
print(result["response"])
```

### 2. Chat API（对话接口）

**端点：** `http://localhost:11434/api/chat`

**请求示例：**
```python
import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama2",
        "messages": [
            {"role": "user", "content": "你好"}
        ],
        "stream": False
    }
)

result = response.json()
print(result["message"]["content"])
```

## 🔧 常用命令

```bash
# 查看已安装的模型
ollama list

# 查看正在运行的模型
ollama ps

# 删除模型
ollama rm llama2

# 查看模型信息
ollama show llama2
```

## 📝 代码说明

### ollama_demo.py
- `chat_with_ollama()`: 普通调用，返回完整结果
- `chat_with_ollama_stream()`: 流式调用，逐字输出

### ollama_chat.py
- 交互式聊天程序
- 支持上下文对话
- 可清空历史记录

## 🎯 快速测试

```python
import requests

# 最简单的调用
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama2",
        "prompt": "Hello!",
        "stream": False
    }
)

print(response.json()["response"])
```

## ⚠️ 注意事项

1. 确保 Ollama 服务已启动（`ollama serve`）
2. 确保已下载对应的模型（`ollama pull llama2`）
3. 默认端口是 `11434`，如果修改了端口需要相应调整代码
4. 首次运行模型会比较慢，后续会快很多

## 🌟 推荐模型

| 模型 | 大小 | 用途 |
|------|------|------|
| llama2 | 3.8GB | 通用对话 |
| mistral | 4.1GB | 高质量对话 |
| codellama | 3.8GB | 代码生成 |
| qwen | 4.7GB | 中文对话 |
| llama2-chinese | 3.8GB | 中文优化 |

## 📚 更多资源

- [Ollama 官网](https://ollama.ai/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [API 文档](https://github.com/ollama/ollama/blob/main/docs/api.md)

