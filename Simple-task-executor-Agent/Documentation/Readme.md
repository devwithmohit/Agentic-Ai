# 🤖 Simple Task Executor Agent

A powerful AI agent built with Google's Gemini API that performs intelligent text processing tasks including summarization, Hindi translation, and sentiment analysis. The project features both a command-line interface and a user-friendly Streamlit web application.

## ✨ Features

- **Text Summarization**: Condense long texts into concise summaries
- **Hindi Translation**: Translate any text to Hindi using Gemini's language capabilities
- **Sentiment Analysis**: Analyze emotional tone (Positive, Negative, Neutral)
- **Dual Interface**: Command-line and web-based Streamlit UI
- **Smart Task Detection**: Automatically determines task based on user input keywords
- **Gemini-Powered**: Leverages Google's advanced Gemini 1.5 Flash model

## 🏗️ Project Structure

```
Simple-task-executor-Agent/
├── main.py                 # Command-line entry point
├── app.py                  # Streamlit web application
├── .env                    # Environment variables (API keys)
├── .env.example            # Environment template
├── agent/
│   ├── __init__.py
│   ├── llm.py             # Gemini API wrapper
│   ├── decision.py        # Task decision logic
│   ├── tasks.py           # Task definitions and execution
│   ├── executor.py        # Main agent loop
│   └── concept.txt        # Project flow documentation
└── Documentation/
    ├── Readme.md          # This file
    └── requirements.txt   # Python dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key for Gemini
- Git (optional)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Simple-task-executor-Agent
```

2. **Install dependencies**
```bash
pip install -r Documentation/requirements.txt
```

3. **Set up environment variables**
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Google API key
GOOGLE_API_KEY="your-actual-api-key-here"
```

4. **Get Google API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/)
   - Create a new API key
   - Copy the key to your `.env` file

## 💻 Usage

### Command Line Interface

Run the agent in terminal mode:

```bash
python main.py
```

**Example interactions:**
```
You: Please summarize this long article about AI...
Agent: [AI-generated summary]

You: Translate "Hello, how are you?" to Hindi
Agent: नमस्ते, आप कैसे हैं?

You: What's the sentiment of "I love this product!"
Agent: Positive
```

### Streamlit Web Interface

Launch the web application:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and interact with the intuitive web interface.

## 🔧 How It Works

### Task Detection Logic

The agent automatically detects tasks based on keywords in your input:

- **Summarization**: Keywords like "summarize", "summary"
- **Translation**: Keywords like "translate", "hindi"
- **Sentiment Analysis**: Keywords like "sentiment", "feeling", "mood"
- **Echo**: Default fallback (simply repeats input)

### Architecture Flow

1. **User Input** → [`decide_task()`](agent/decision.py) analyzes keywords
2. **Task Decision** → [`execute_task()`](agent/tasks.py) prepares prompt
3. **LLM Call** → [`llm_call()`](agent/llm.py) sends request to Gemini
4. **Response** → Formatted result returned to user

## 📋 Dependencies

- `google-generativeai` - Google's Gemini API client
- `python-dotenv` - Environment variable management
- `streamlit` - Web application framework
- `rich` - Enhanced terminal output (optional)

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

## 🛠️ Configuration

### Model Settings

The default configuration uses:
- **Model**: `gemini-1.5-flash`
- **Temperature**: `0.5` (balanced creativity)

You can modify these in [`llm.py`](agent/llm.py):

```python
def llm_call(prompt, model="gemini-1.5-flash", temperature=0.5):
```

### Adding New Tasks

To add new tasks, update the `TASKS` dictionary in [`tasks.py`](agent/tasks.py):

```python
TASKS = {
    "summarize": "Summarize the following text in a concise way:",
    "translate": "Translate the following text to Hindi:",
    "sentiment": "Analyze the sentiment of the following text (Positive, Negative, Neutral):",
    "your_new_task": "Your custom prompt here:",
}
```

And add detection logic in [`decision.py`](agent/decision.py):

```python
def decide_task(user_input: str) -> str:
    text = user_input.lower()
    if "your_keyword" in text:
        return "your_new_task"
    # ... existing conditions
```

## 🚧 Error Handling

The agent includes robust error handling:
- API connection failures
- Invalid API keys
- Empty responses
- Network timeouts

All errors are gracefully caught and user-friendly messages are displayed.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Google Gemini AI for providing the language model
- Streamlit for the excellent web framework
- The open-source community for inspiration

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) section
2. Create a new issue with detailed description
3. Include error messages and system information

---

**Made with ❤️ using Google Gemini AI**