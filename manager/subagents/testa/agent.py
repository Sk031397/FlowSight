from google.adks.agents import Agent
testa = Agent(
    name="testa",
    model="gemini-2.0-flash",
    description="An agent that prioritizes and manages tests",
    instructions="""
        You are a smart testing agent that determines which tests need to be run based on code changes.
        Prioritize critical tests, detect flaky tests, and optimize test execution using historical data.
    """
)