from langgraph.graph import StateGraph, END
from graph.state import StartupState
from agents.research_agent import research_agent
from agents.validator_agent import validator_agent
from agents.strategy_agent import strategy_agent
from agents.report_agent import report_agent

def build_workflow():
    workflow = StateGraph(StartupState)

    # Add all agent nodes
    workflow.add_node("research", research_agent)
    workflow.add_node("validator", validator_agent)
    workflow.add_node("strategy", strategy_agent)
    workflow.add_node("report", report_agent)

    # Define the flow — orchestrator delegates in sequence
    workflow.set_entry_point("research")
    workflow.add_edge("research", "validator")
    workflow.add_edge("validator", "strategy")
    workflow.add_edge("strategy", "report")
    workflow.add_edge("report", END)

    return workflow.compile()
