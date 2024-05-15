from src.agents.tool import tool_metadata
from src.agents.types import Parameter
from src.agents import Agent, agent_metadata

name_a = "Mock Tool A"
name_b = "Mock Tool B"
description = "A test tool"
param_description = "A string"


@tool_metadata(
    name=name_a,
    description=description,
    parameters={
        "input": Parameter(type="string", description=param_description, required=True),
        "optional": Parameter(type="string", description=param_description, required=False),
        "another_optional": Parameter(type="string", description=param_description, required=False),
    },
)
def mock_tool_a(input: str):
    return input


@tool_metadata(
    name=name_b,
    description=description,
    parameters={
        "input": Parameter(type="string", description=param_description, required=True),
        "optional": Parameter(type="string", description=param_description, required=False),
    },
)
def mock_tool_b(input: str):
    return input

mock_agent_description = "A test agent"
mock_agent_name = "Mock Agent"
mock_prompt = "You are a bot!"
mock_tools = [mock_tool_a, mock_tool_b]


@agent_metadata(name=mock_agent_name, description=mock_agent_description, tools=mock_tools)
class MockAgent(Agent):
    pass


__all__ = ["MockAgent", "mock_agent_description", "mock_agent_name", "mock_tools"]
