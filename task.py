from crewai import Task
from textwrap import dedent
class CustomTasks:
    def task1(self,agent,Purpose):
        return Task(
            description=dedent(
                f"""
            Thoroughly analyze the topic of  {Purpose}.  Gather the relevant research papers and data, prioritizing reputable sources and up-to-date.  
            Provide a comprehensive report with:
            * Key findings and insights directly related to {Purpose}
            * Actionable recommendations or implications
            * Clear citations of all research papers and datasets used 
            """
            ),
            expected_output="A detailed analysis report (at least 2 paragraphs) focused on {Purpose}. Include a reference section listing all research papers and datasets, allowing for source verification.",
            agent=agent
        )
    def task2(self,agent):
        return Task(
            description=dedent(
                f"""
            Using the report provided by the Senior Research Analyst, create an audience-friendly summary. Focus on:
            * Explaining the report's purpose in plain language
            * Highlighting the report's most important conclusions
            * Maintaining a clear and engaging writing style
            """
            ),
            expected_output="A concise summary in the following format: * 'The report is about...'  [1-2 sentences summarizing the focus] * 'The report concludes that...' [1-2 sentences on key takeaways] ",
            agent=agent
        )
    
