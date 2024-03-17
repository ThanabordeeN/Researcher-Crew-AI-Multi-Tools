from crewai import Agent
from langchain_community.llms import Ollama
from tools import Tools
class Resercher :
    def __init__(self) -> None:
        self.mistral = Ollama(model="openhermes",temperature=0.5)
        self.tool_list = Tools()
        self.search = self.tool_list.search_tool()
        self.arxiv = self.tool_list.arxiv_tool()
        self.wiki = self.tool_list.wikipedia_tool()
    def researcher(self) :
        return Agent(
            role='Senior Research Analyst',
            goal='Analyze and synthesize research papers and complex data sets, extracting key findings and implications. Present insights in a clear, concise format, highlighting actionable recommendations for stakeholders',
            backstory="""Thoroughly analyze the topic of [Purpose]. Gather the most relevant research papers and data, prioritizing reputable sources and recent publications. Provide a comprehensive report with:
                        * Key findings and insights directly related to [Purpose]
                        * Actionable recommendations or implications
                        * **Critical analysis of the conclusions presented in the research. Identify strengths, weaknesses, potential biases, and areas for further exploration.**
                        * Clear citations of all research papers and datasets used
                        * Cross check the information with the various tools provided
                        * You will check related information instead and analyze relation of them if there is no information available in the tools provided""",
            verbose=True,
            allow_delegation=False,
            tools=[self.search, self.arxiv, self.wiki],
            llm=self.mistral,
            max_iter=30,
            )
    def writer(self) :
        return Agent(
            role='Content Strategist',
            goal='Translate technical research summaries into engaging and digestible content for a general audience. Explain complex concepts clearly, using relatable examples and storytelling techniques.',
            backstory="""You are a skilled communicator with a deep understanding of technology and a passion for 
            making complex concepts accessible. Your experience in technical writing and 
            content strategy  enables you to transform intricate research into compelling and informative content.""",
            verbose=False,
            allow_delegation=False,
            tools=[],
            llm=self.mistral,
            max_iter=30,
            )
    #add more agents here