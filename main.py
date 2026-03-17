from llm.ollama_llm import OllamaLLM
from llm.model_router import ModelRouter
from agents.base_agent import BaseAgent
from tools.web_search import WebSearchTool
from tools.python_executor import PythonExecutor
#from llm.multimodal_llm import MultiModalLLM

gemma = OllamaLLM("gemma3")
llama = OllamaLLM("llama3")

router = ModelRouter({

    "LearningAgent": gemma,
    "ResearchAgent": llama,
    "default": gemma
})

tools = [
    WebSearchTool(),
    PythonExecutor()
]

agent = BaseAgent(
    name="LearningAgent",
    role="AI tutor explaining AI systems",
    model_router=router,
    tools=tools
)

agent.run(
    #"Who is the PM of Canada?"
    "Find the current Python version installed on my system and explain how to print Hello World."
    #"Search the web for the latest Python version and print it using Python code."
)

'''
print("\n--- MULTIMODAL TEST (IMAGE UNDERSTANDING) ---\n")

vision_model = MultiModalLLM("llava")

result = vision_model.describe_image(
    "sample.jpg",
    "Describe what can you see in the image."
)

print(result)
'''