class Orchestrator:

    def __init__(self, planner, researcher, critic):

        self.planner = planner
        self.researcher = researcher
        self.critic = critic

    def handle(self, task):

        print("\n[ORCHESTRATOR] Step 1: Planning...\n")

        plan = self.planner.plan(task)

        print("\n[PLAN]\n", plan)

        print("\n[ORCHESTRATOR] Step 2: Research...\n")

        research_output = self.researcher.run(task)

        print("\n[ORCHESTRATOR] Step 3: Critic Review...\n")

        critique = self.critic.critique(research_output)

        print("\n[CRITIC FEEDBACK]\n", critique)

        print("\n[ORCHESTRATOR] Step 4: Final Response\n")

        return research_output
    