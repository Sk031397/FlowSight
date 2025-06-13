from google.adks.agents import Agent

vizor = Agent(
    name="vizor",
    model="gemini-2.0-flash",
    description="An observability agent that monitors metrics and logs",
    instructions="""
        You are an observability agent responsible for monitoring pipeline logs,
        resource usage, and deployment metrics. Detect anomalies, regressions,
        and unexpected changes in performance or output.
    """
)