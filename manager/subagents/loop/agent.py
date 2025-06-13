from google.adks.agents import Agent

loop = Agent(
    name="loop",
    model="gemini-2.0-flash",
    description="A deployment and feedback agent",
    instructions="""
        You are a deployment manager agent that coordinates staging and production rollouts.
        Handle canary deployments, blue-green setups, and progressive delivery.
        Collect post-deployment feedback to validate or trigger rollback.
    """
)