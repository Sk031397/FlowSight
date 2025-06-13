from google.adk.agents import Agent

plugsy = Agent(
    name="plugsy",
    model="gemini-2.0-flash",
    description="A toolchain integration agent",
    instructions="""
        You are a plugin and third-party integration agent.
        Connect FlowSight to external tools like Jira, Sentry, SonarQube, or Slack,
        and manage data flow and status updates across platforms.
    """
)