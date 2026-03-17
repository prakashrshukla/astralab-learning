from duckduckgo_search import DDGS
from tools.base_tool import BaseTool

class WebSearchTool(BaseTool):

    name = "web_search"
    description = "Search the internet for latest information"

    def run(self, query):

        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r["title"] + " - " + r["href"])

        return "\n".join(results)