from llm.ollama_llm import OllamaLLM
from llm.model_router import ModelRouter

from agents.base_agent import BaseAgent
from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.critic_agent import CriticAgent

from orchestrator.orchestrator import Orchestrator

from tools.web_search import WebSearchTool
from tools.python_executor import PythonExecutor

from communication.message_bus import MessageBus
from communication.a2a_protocol import A2AMessage, A2AProtocol

#from llm.multimodal_llm import MultiModalLLM

gemma = OllamaLLM("gemma3")
llama = OllamaLLM("gemma3")

router = ModelRouter({

    "research": gemma,
    "planner": llama,
    "default": gemma
})

tools = [
    WebSearchTool(),
    PythonExecutor()
]

planner = PlannerAgent(
    name="planner",
    role="Break tasks into steps",
    model_router=router,
    tools=tools
)

research = ResearchAgent(
    name="research",
    role="Find information using tools",
    model_router=router,
    tools=tools
)

critic = CriticAgent(
    name="critic",
    role="Evaluate quality of responses and improve them",
    model_router=router,
    tools=tools
)

orchestrator = Orchestrator(
    planner,
    research,
    critic
)

result = orchestrator.handle(
    "Who is Prime Minister of Canada? Just give me the name without any explanation."
)

print("\n[FINAL OUTPUT]\n", result)



# DEMO: MESSAGE BUS and A2A PROTOCOL
'''
print("\n===== MESSAGE BUS DEMO =====")

bus = MessageBus()

bus.register(planner)
bus.register(research)

bus.send(
    "planner",
    "research",
    "Find the latest FastAPI documentation"
)


print("\n===== A2A PROTOCOL DEMO =====")

agents = {
    "planner": planner,
    "research": research
}

a2a = A2AProtocol(agents)

msg = A2AMessage(
    sender="planner",
    receiver="research",
    intent="information_request",
    payload="Latest Python features"
)

a2a.send(msg)
'''

#DEMO: TOOL USE
'''
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
    "Who is the Prime Minister of Canada? Just give me the name without any explanation."
    #"Find the current Python version installed on my system and explain how to print Hello World."
    #"Search the web for the latest Python version and print it using Python code."
)
'''

#DEMO: MULTIMODAL
'''
print("\n--- MULTIMODAL TEST (IMAGE UNDERSTANDING) ---\n")

vision_model = MultiModalLLM("llava")

result = vision_model.describe_image(
    "sample.jpg",
    "Describe what can you see in the image."
)

print(result)
'''