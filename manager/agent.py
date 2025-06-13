from google.adk.agents import Agent
from dotenv import load_dotenv

# multi-agents 
from .sub_agents.bottleneck.agent import bottleneck
from .sub_agents.intellient.agent import intellient
from .sub_agents.loop.agent import loop
from .sub_agents.packrat.agent import packrat
from .sub_agents.plugsy.agent import plugsy
from .sub_agents.testa.agent import testa
from .sub_agents.vizor.agent import vizor

load_dotenv()

root_agent = Agent(
    name="flow",
    model="gemini-2.0-flash",
    description="Main orchestrator agent for FlowSight",
    instructions="""
        You are the main orchestrator agent responsible for coordinating other agents,
        making intelligent routing decisions, and ensuring optimal CI/CD pipeline flow.
        Monitor the overall pipeline health, detect risks early, and guide sub-agents as needed.
    """,
    
)