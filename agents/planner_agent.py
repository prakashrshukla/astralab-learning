from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):

    def plan(self, task):

        plan = f"""
Break this task into smaller steps:

{task}
"""

        return self.router.get_model(self.name).generate(plan)