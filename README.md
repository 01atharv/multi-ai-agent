#  Startup Idea Validator — Multi-Agent System

A production-ready Multi-Agent system built with **LangGraph** and **Gemini API** that validates startup ideas by delegating tasks across specialized AI agents.

## Agent Architecture

```
User Input → Orchestrator → Research Agent
                         → Validator Agent
                         → Strategy Agent
                         → Report Agent → Final Report
```

Each agent specializes in one task and passes its output to the next agent via shared state.

## Tech Stack
- Python 
- LangGraph (Multi-Agent Orchestration)
- Gemini 2.5 Flash (LLM)
- LangChain Google GenAI

##  Setup

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your Gemini API key in `.env`:
```
GEMINI_API_KEY=your_key_here
```

4. Run:
```bash
python main.py
```

##  Output
The system generates a complete **Startup Validation Report** including:
- Market Research
- Strengths & Weaknesses
- Go-To-Market Strategy
- Final Verdict (Go / No-Go / Pivot)
