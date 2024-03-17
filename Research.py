from crewai import Crew
from textwrap import dedent
from agent import Resercher
from task import CustomTasks

# This is the main class that you will use to define your custom crew.
class CustomCrew:
    def __init__(self, Purpuse): 
        self.input = Purpuse
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Resercher()
        tasks = CustomTasks()
        # Define your custom agents and tasks here
        researcher = agents.researcher()
        writer = agents.writer()
        # Custom tasks include agent name and variables as input
        task1 = tasks.task1(
            researcher,
            self.input
        )
        task2 = tasks.task2(
            writer
        )
        # Define your custom crew here
        crew = Crew(
            agents=[researcher,writer],
            tasks=[task1,task2],
            verbose=1,
        )
        result = crew.kickoff()
        return result
# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Researcher AI")
    print("-------------------------------")
    Purpuse = input(dedent("""What is top are you interesting? : """))
    crew = CustomCrew(Purpuse)
    result = crew.run()
    print("## Researcher AI Result")
    print("-------------------------------")
    print(result)
