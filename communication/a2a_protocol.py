class A2AMessage:

    def __init__(self, sender, receiver, intent, payload):

        self.sender = sender
        self.receiver = receiver
        self.intent = intent
        self.payload = payload

class A2AProtocol:

    def __init__(self, agents):

        self.agents = agents

    def send(self, message):

        print(f"\n[A2A] {message.sender} → {message.receiver}")
        print(f"Intent: {message.intent}")

        receiver = self.agents.get(message.receiver)

        if not receiver:
            return "Receiver not found"

        return receiver.receive(message.sender, message.payload)
    