from google.adk.agents import Agent

bottleneck = Agent(
    name="bottleneck",
    model="gemini-2.0-flash",
    description="An agent that tells identifies bottleneck",
    instructions="""
        You are a bottleneck agent that finds inconsistencies in code
    """
)