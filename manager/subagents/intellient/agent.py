from google.adk.agents import Agent

intellilint = Agent(
    name="intellilint",
    model="gemini-2.0-flash",
    description="An agent that analyzes code quality and style",
    instructions="""
        You are a static analysis and linting agent. Review source code to detect style issues,
        syntax violations, and potential bugs. Recommend improvements and enforce coding standards.
    """
)