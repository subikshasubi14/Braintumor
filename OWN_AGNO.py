from typing import List
from agno.models.ollama import Ollama
from agno.agent import Agent
from agno.tools import Toolkit
from agno.utils.log import logger

class MathTools(Toolkit):
    def __init__(self):
        super().__init__(name="math_tools")
        self.register(self.add_numbers)

    def add_numbers(self, numbers: List[int]) -> int:
        """
        Adds a list of numbers and returns the sum.

        Args:
            numbers (List[int]): A list of integers to add.
        Returns:
            int: The sum of the numbers.
        """
        logger.info(f"Adding numbers: {numbers}")
        try:
            return sum(numbers)
        except Exception as e:
            logger.warning(f"Failed to add numbers: {e}")
            return f"Error: {e}"
            
# model="openrouter/gpt-4o",
agent = Agent(tools=[MathTools()], show_tool_calls=True, markdown=True,model=Ollama(id="llama3.2"))

agent.print_response("Add 5 and 10.")