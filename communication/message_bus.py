'''
internal structure:
{
 "planner": PlannerAgent(),
 "research": ResearchAgent()
}

When one agent sends a message:
bus.send("planner", "research", task)
'''

class MessageBus:

    def __init__(self):
        self.agents = {}

    def register(self, agent):

        self.agents[agent.name] = agent

    def send(self, sender, receiver, message):

        if receiver not in self.agents:
            return f"Agent {receiver} not found"

        print(f"\n[BUS] {sender} → {receiver}")

        return self.agents[receiver].receive(sender, message)
    