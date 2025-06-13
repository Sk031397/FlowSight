from google.adk.agents import Agent

configure = Agent(
    name="configure",
    model="gemini-2.0-flash",
    description="An agent that tells configures data within a gitlab account",
    instructions="""
        You are a funny nerd agent that tells nerdy jokes about various topics
    """
)