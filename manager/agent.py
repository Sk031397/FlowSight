from google.adk.agents import Agent
from dotenv import load_dotenv
from .subagents.configure import configure
from .subagents.bottleneck import bottleneck
load_dotenv()

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="Manager agent",
    instruction="""
    You are a manager agent that is responsible for overseeing the work of the other agents. 

    Always delegate the task to the appropriate agent. use your best judgement
    to determine which agent to delegate to. 

    You are responsible for delegating tasks to the following agent:
    - configure
    - bottleneck
    """,
    sub_agents=[configure,bottleneck]
) 