from crewai import Crew,Process
from textwrap import dedent
from agent import Resercher
from task import CustomTasks
from langchain_community.llms import Ollama
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import dotenv
# This is the main class that you will use to define your custom cAIrew.
dotenv.load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
class CustomCrew:
    def __init__(self, Purpuse): 
        self.input = Purpuse
        self.gemini = ChatGoogleGenerativeAI(model="gemini-1.0-pro",temperature=0.5)
        #self.mistral = Ollama(model="openhermes",temperature=0.1)
    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Resercher()
        tasks = CustomTasks()
        # Define your custom agents and tasks here
        researcher = agents.researcher()
        datasearcher = agents.data_searcher()
        writer = agents.writer()
        # Custom tasks include agent name and variables as input
        Analyze = tasks.Analyze(
            researcher,
            self.input
        )
        Content_create = tasks.Content_create(
            writer
        )
        Data_Research = tasks.Data_Research(
            agent=datasearcher,Purpose=self.input
        )
        # Define your custom crew here
        crew = Crew(
            agents=[datasearcher,researcher,writer],
            tasks=[Data_Research,Analyze,Content_create],
            verbose=2,
            process=Process.hierarchical,
            manager_llm=self.gemini,
            memory=False,
            #embedder={"provider": "google"}
        )
        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to Researcher AI")
    print("-------------------------------")
    Purpuse = input(dedent("""What is top are you interesting? : """))
    crew = CustomCrew(Purpuse)
    result = crew.run()
    print("## Researcher AI Result")
    print("-------------------------------")
    print(result)
