from langchain_google_genai import ChatGoogleGenerativeAI
from graph.state import StartupState
from datetime import datetime


def report_agent(state: StartupState) -> StartupState:
    print("\n Report Agent working...")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        max_output_tokens=500
    )
    today = datetime.now().strftime("%B %d, %Y")

    prompt = f"""
    You are a Professional Business Report Writer.
    Compile all the information below into a clean, structured startup validation report.

    Startup Idea: {state['startup_idea']}
    Research: {state['research_output']}
    Validation: {state['validation_output']}
    Strategy: {state['strategy_output']}

    Do NOT include any specific date in the report.

   Format the report with:
    - Report Date: {today}
    - Executive Summary
    - Market Research Findings
    - Validation Results
    - Recommended Strategy
    - Final Verdict (Go / No-Go / Pivot)

    Make it professional and easy to read.
    """

    response = llm.invoke(prompt)
    state["final_report"] = response.content
    print(" Report Agent done!")
    return state
