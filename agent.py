from crewai import Agent
from langchain_community.llms import Ollama
from tools import Tools
class Resercher :
    def __init__(self) -> None:
        self.llm = Ollama(model="mistral",temperature=0)
        self.tool_list = Tools()
        self.search = self.tool_list.search_tool()
        self.arxiv = self.tool_list.arxiv_tool()
        self.wiki = self.tool_list.wikipedia_tool()
    def researcher(self) :
        return Agent(
            role='Senior Research Analyst',
            goal='Summarize the research papers and data to provide actionable insights of purpose',
            backstory="""You work at a leading technology research institute.
            You are a researcher with the ability to read research papers at leading universities.
            You very strict abut data so your research base on true data and research paper by using tools.
            You have a unique ability to break down complex data and present actionable insights.""",
            verbose=True,
            allow_delegation=False,
            tools=[self.search, self.arxiv, self.wiki],
            llm=self.llm
            )
    def writer(self) :
        return Agent(
            role='Tech Content Strategist',
            goal='summary content from the Senior Research Analyst for easy reading and understanding without using any tools.',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
            You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True,
            tools=[],
            llm=self.llm
            )
    #add more agents here