class BaseTool:

    name = "base_tool"
    description = "Generic tool"

    def run(self, input_text):
        raise NotImplementedError