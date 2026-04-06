from typing import TypedDict, Optional

class StartupState(TypedDict):
    startup_idea: str
    research_output: Optional[str]
    validation_output: Optional[str]
    strategy_output: Optional[str]
    final_report: Optional[str]
