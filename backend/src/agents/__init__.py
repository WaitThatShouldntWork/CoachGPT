from typing import List
from src.utils import Config
from .agent import Agent, agent
from .datastore_agent import DatastoreAgent
from .web_agent import WebAgent
from .intent_agent import IntentAgent
from .tool import tool, Parameter
from .validator_agent import ValidatorAgent
from .answer_agent import AnswerAgent
from .chart_generator_agent import ChartGeneratorAgent
from .goal_agent import GoalAgent
from .file_agent import FileAgent

config = Config()


def get_validator_agent() -> Agent:
    return ValidatorAgent(config.validator_agent_llm, config.validator_agent_model)


def get_intent_agent() -> Agent:
    return IntentAgent(config.intent_agent_llm, config.intent_agent_model)


def get_answer_agent() -> Agent:
    return AnswerAgent(config.answer_agent_llm, config.answer_agent_model)


def agent_details(agent) -> dict:
    return {"name": agent.name, "description": agent.description}


def get_available_agents() -> List[Agent]:
    return [DatastoreAgent(config.datastore_agent_llm, config.datastore_agent_model),
            WebAgent(config.web_agent_llm, config.web_agent_model),
            ChartGeneratorAgent(config.chart_generator_llm, config.chart_generator_model),
            FileAgent(config.file_agent_llm, config.file_agent_model),
            GoalAgent(config.goal_agent_llm, config.goal_agent_model),
            ]


def get_agent_details():
    agents = get_available_agents()
    return [agent_details(agent) for agent in agents]


__all__ = [
    "agent",
    "Agent",
    "agent_details",
    "get_agent_details",
    "get_answer_agent",
    "get_intent_agent",
    "get_available_agents",
    "get_validator_agent",
    "Parameter",
    "tool",
]
