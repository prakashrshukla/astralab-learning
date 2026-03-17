class ToolManager:

    def __init__(self, tools):

        self.tools = {tool.name: tool for tool in tools}

    def execute(self, tool_name, input_data):

        if tool_name not in self.tools:
            return f"Tool {tool_name} not found."

        tool = self.tools[tool_name]

        return tool.run(input_data)