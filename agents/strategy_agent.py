from langchain_google_genai import ChatGoogleGenerativeAI
from graph.state import StartupState

def strategy_agent(state: StartupState) -> StartupState:
    print("\n Strategy Agent working...")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    

    prompt = f"""
    You are a Business Strategy Expert.
    Based on the research and validation below, create a go-to-market strategy:

    Startup Idea: {state['startup_idea']}
    Research: {state['research_output']}
    Validation: {state['validation_output']}

    Provide:
    1. Target Audience (specific)
    2. Go-To-Market Strategy (step by step)
    3. Top 3 Marketing Channels
    4. Revenue Model suggestion

    Be practical and actionable.
    """

    response = llm.invoke(prompt)
    state["strategy_output"] = response.content
    print(" Strategy Agent done!")
    return state
