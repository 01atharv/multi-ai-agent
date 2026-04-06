import streamlit as st
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.dirname(__file__))

st.set_page_config(
    page_title="Startup Idea Validator",
    layout="centered"
)

st.markdown("""
<style>
    .main { padding-top: 2rem; }
    .agent-box {
        padding: 16px 20px;
        border-radius: 12px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 15px;
        font-weight: 500;
    }
    .idle    { background: #1e1e2e; border: 1px solid #2d2d44; color: #888; }
    .working { background: #1a1a3e; border: 1px solid #4a4aff; color: #aaaaff; }
    .done    { background: #0f2e1a; border: 1px solid #2ecc71; color: #2ecc71; }
    .report-box {
        background: #0f1f0f;
        border: 1px solid #2ecc71;
        border-radius: 14px;
        padding: 28px;
        margin-top: 20px;
    }
    .stTextArea textarea { font-size: 15px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("Startup Idea Validator")
st.markdown("##### Multi-Agent AI System ")
st.divider()

idea = st.text_area(
    "Enter your startup idea",
    placeholder="e.g. I want to build a food delivery app for tier 2 cities in India...",
    height=120
)

AGENTS = [
    {"key": "research",  "icon": "🔍", "label": "Research Agent",  "desc": "Live web search for market data"},
    {"key": "validator", "icon": "✅", "label": "Validator Agent",  "desc": "Strengths, weaknesses & viability score"},
    {"key": "strategy",  "icon": "📊", "label": "Strategy Agent",  "desc": "Go-to-market plan & revenue model"},
    {"key": "report",    "icon": "📝", "label": "Report Agent",    "desc": "Compiles final validation report"},
]

def render_agent(agent, status):
    css = {"idle": "idle", "working": "working", "done": "done"}.get(status, "idle")
    status_text = {
        "idle":    agent["desc"],
        "working": "Working...",
        "done":    "Completed"
    }.get(status, agent["desc"])
    st.markdown(f"""
    <div class="agent-box {css}">
        <span style="font-size:22px">{agent["icon"]}</span>
        <div>
            <div>{agent["label"]}</div>
            <div style="font-size:12px;opacity:0.7;margin-top:2px">{status_text}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if st.button("Validate My Idea", type="primary", use_container_width=True, disabled=not idea.strip()):

    from agents.research_agent import research_agent
    from agents.validator_agent import validator_agent
    from agents.strategy_agent import strategy_agent
    from agents.report_agent import report_agent

    st.divider()
    st.markdown("###  Agents Working...")

    placeholders = {a["key"]: st.empty() for a in AGENTS}

    for agent in AGENTS:
        with placeholders[agent["key"]]:
            render_agent(agent, "idle")

    state = {
        "startup_idea": idea.strip(),
        "research_output": None,
        "validation_output": None,
        "strategy_output": None,
        "final_report": None,
    }

    steps = [
        ("research",  research_agent),
        ("validator", validator_agent),
        ("strategy",  strategy_agent),
        ("report",    report_agent),
    ]

    completed = set()

    for key, fn in steps:
        with placeholders[key]:
            render_agent(next(a for a in AGENTS if a["key"] == key), "working")

        state = fn(state)
        completed.add(key)

        with placeholders[key]:
            render_agent(next(a for a in AGENTS if a["key"] == key), "done")

    st.divider()
    st.markdown("###  Final Startup Validation Report")
    st.markdown(state["final_report"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.success(" Validation complete!")

    st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)