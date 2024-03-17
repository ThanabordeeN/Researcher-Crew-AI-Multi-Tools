from langchain_community.tools import Tool, DuckDuckGoSearchRun, ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

class Tools:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()
        self.arxiv = ArxivQueryRun()
        self.wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    def search_tool(self):
        return Tool(
            name="Search",
            func=self.search.run,
            description="useful for when you need to answer questions about current general events."
        )

    def arxiv_tool(self):
        return Tool(
            name="Arxiv",
            func=self.arxiv.run,
            description="useful when you need an answer about encyclopedic specific knowledge"
        )

    def wikipedia_tool(self):
        return Tool(
            name="Wikipedia",
            func=self.wiki.run,
            description="useful when you need an answer about encyclopedic specific knowledge"
        )
    # Add more tools here


