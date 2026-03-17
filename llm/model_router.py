class ModelRouter:

    def __init__(self, models):
        self.models = models

    def get_model(self, agent_name):

        if agent_name in self.models:
            return self.models[agent_name]

        return self.models["default"]