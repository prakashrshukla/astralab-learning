class ReasoningLogger:

    def log(self, agent_name, message):

        print(f"\n[{agent_name} LOG]")
        print(message)
        print("-" * 40)