from observer.reasoning_logger import ReasoningLogger
from agents.tool_manager import ToolManager

class BaseAgent:

    def __init__(self, name, role, model_router, tools=None):
        self.name = name
        self.role = role
        self.router = model_router
        self.logger = ReasoningLogger()
        self.tool_manager = ToolManager(tools or [])

    def build_prompt(self, task):

        tool_list = "\n".join(self.tool_manager.tools.keys())

        prompt = f"""
You are an AI agent.

Agent Name: {self.name}
Role: {self.role}

Available tools:
{tool_list}

If a tool is useful, explain which tool you would use and respond in format:

TOOL: tool_name
INPUT: tool_input

Otherwise answer normally.

Your task:
{task}

Explain your reasoning briefly before answering.
"""

        return prompt

    def run(self, task):

        llm = self.router.get_model(self.name)

        prompt = self.build_prompt(task)

        response = llm.generate(prompt)

        self.logger.log(self.name, "Thinking about task...")

        if "TOOL:" in response:

            lines = response.split("\n")

            tool_name = None
            tool_input = ""

            for line in lines:

                if line.startswith("TOOL:"):
                    tool_name = line.replace("TOOL:", "").strip()

                if line.startswith("INPUT:"):
                    tool_input = line.replace("INPUT:", "").strip()

            self.logger.log(self.name, f"Executing tool: {tool_name}")

            result = self.tool_manager.execute(tool_name, tool_input)

            print("\n[TOOL RESULT]\n")
            print(result)

            final_prompt = f"""
Tool result:
{result}

Explain the result to the user clearly.
"""
            final_response = llm.generate(final_prompt)

            print("\n[FINAL RESPONSE]\n")
            print(final_response)

        else:

            print("\n[RESPONSE]\n")
            print(response)