from langchain_google_genai import ChatGoogleGenerativeAI
from graph.state import StartupState

def validator_agent(state: StartupState) -> StartupState:
    print("\n Validator Agent working...")

    llm = ChatGoogleGenerativeAI(\
        model="gemini-2.5-flash"
        )

    prompt = f"""
    You are a Startup Validator Expert.
    Based on the research below, validate the startup idea:

    Startup Idea: {state['startup_idea']}
    Research: {state['research_output']}

    Provide:
    1. Strengths (3 points)
    2. Weaknesses (3 points)
    3. Key Risks
    4. Viability Score (1-10) with reason

    Be honest and critical.
    """

    response = llm.invoke(prompt)
    state["validation_output"] = response.content
    print(" Validator Agent done!")
    return state
