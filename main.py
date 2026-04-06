import os
from dotenv import load_dotenv
from graph.workflow import build_workflow

load_dotenv()

def main():
    print(" Startup Idea Validator — Multi-Agent System")
    print("=" * 50)

    startup_idea = input("\nEnter your startup idea: ")

    initial_state = {
        "startup_idea": startup_idea,
        "research_output": None,
        "validation_output": None,
        "strategy_output": None,
        "final_report": None,
    }

    print("\nOrchestrator delegating tasks to agents...\n")

    app = build_workflow()
    result = app.invoke(initial_state)

    print("\n" + "=" * 50)
    print(" FINAL STARTUP VALIDATION REPORT")
    print("=" * 50)
    print(result["final_report"])

if __name__ == "__main__":
    main()
