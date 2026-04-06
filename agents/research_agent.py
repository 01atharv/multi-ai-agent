import os
from google import genai
from google.genai import types
from graph.state import StartupState

class FreeTierLimitError(Exception):
    pass

def research_agent(state: StartupState) -> StartupState:
    print("\n Research Agent working... (Live Web Search)")
    try:
         client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

         prompt = f"""
            You are a Market Research Expert.
            Search the internet and provide CURRENT, ACCURATE data about:
            1. Market Size & Opportunity (with real numbers and year)
            2. Top 3 Competitors (with current market share if available)
            3. Current Market Trends (2024-2025)
            4. Target Audience

            Startup Idea: {state['startup_idea']}
            

            Use real, up-to-date data from the web. Be concise and factual.
            """

         response = client.models.generate_content(
                model="gemini-2.5-flash",
                max_output_tokens=500,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())]
                )
            )

         state["research_output"] = response.text
         print(" Research Agent done! (Data fetched from live web)")
         return state
    
    except Exception as e:
        err = str(e).lower()
        if "quota" in err or "rate" in err or "429" in err or "limit" in err or "exhausted" in err:
            raise FreeTierLimitError("Gemini API free tier limit is over!")
        raise e
