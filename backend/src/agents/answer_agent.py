from datetime import datetime
from src.utils import get_scratchpad
from src.prompts import PromptEngine
from src.agents import Agent, agent

engine = PromptEngine()


@agent(
    name="AnswerAgent",
    description="This agent is responsible for generating an answer for the user, based on results in the scratchpad",
    tools=[],
)
class AnswerAgent(Agent):
    async def invoke(self, utterance: str) -> str:
        final_scratchpad = get_scratchpad()
        create_answer = engine.load_prompt("create-answer", final_scratchpad=final_scratchpad, datetime=datetime.now())

        return await self.llm.chat(self.model, create_answer, user_prompt=utterance)
