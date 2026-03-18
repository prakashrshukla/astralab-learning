from agents.base_agent import BaseAgent

class CriticAgent(BaseAgent):

    def critique(self, content):

        prompt = f"""
You are a critic AI.

Evaluate the following response:

{content}

Check for:
- correctness
- completeness
- clarity

If needed, suggest improvements.
"""

        return self.router.get_model(self.name).generate(prompt)