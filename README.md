# 通义大模型 Streamlit 应用

这是一个基于 Streamlit 框架的网页应用，集成了阿里云通义大模型，实现了类似 ChatGPT 的对话功能。

## 功能特点

- 实时对话：支持与通义大模型进行实时对话
- 系统提示语：可自定义系统提示语
- 对话历史：保存并显示完整的对话历史
- 流式响应：实时显示 AI 响应内容

## 安装说明

1. 克隆项目到本地：
```bash
git clone <repository-url>
cd <project-directory>
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
- 复制 `.env.example` 文件为 `.env`
- 在 `.env` 文件中设置你的 DASHSCOPE_API_KEY：
```
DASHSCOPE_API_KEY=your_api_key_here
```

4. 运行应用：
```bash
streamlit run app.py
```

## 使用说明

1. 启动应用后，在浏览器中打开显示的地址
2. 在侧边栏可以设置系统提示语
3. 在主界面的输入框中输入问题即可开始对话
4. 对话历史会自动保存在会话中

## 注意事项

- 请确保您有有效的通义大模型 API 密钥
- API 调用可能产生费用，请注意使用��
- 建议在生产环境中添加适当的错误处理和日志记录

## 技术栈

- Python
- Streamlit
- OpenAI API（通义大模型兼容模式）
- python-dotenv 