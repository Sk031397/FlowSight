from google.adks.agents import Agent

packrat = Agent(
    name="packrat",
    model="gemini-2.0-flash",
    description="An agent that manages builds and artifacts",
    instructions="""
        You are a build management agent. Handle artifact caching, build versioning,
        and reuse strategies. Suggest incremental builds and detect redundant steps.
    """
)
