from crewai import Task
from textwrap import dedent
class CustomTasks:
    def Data_Research(self,agent,Purpose):
        return Task(
            description=dedent(
                f"""
            use the tools provided to conduct a comprehensive search for information related to {Purpose} ,
            Gather the relevant research papers and data, prioritizing reputable sources and up-to-date,
                """
            ),
            agent=agent,
            expected_output="A list of at least 5 paragraph of research papers and datasets related to {Purpose}.",
            )
    

    def Analyze(self,agent,Purpose):
        return Task(
            description=dedent(
                f"""
            Thoroughly analyze the topic of  {Purpose}.  
            Provide a comprehensive report with:
            * Key findings and insights directly related to {Purpose}
            * Actionable recommendations or implications
            * Clear citations of all research papers and datasets used 
            """
            ),
            expected_output="A detailed analysis report (at least 2 paragraphs) focused on {Purpose}. Include a reference section listing all research papers and datasets, allowing for source verification.",
            agent=agent,
        )
    def Content_create(self,agent):
        return Task(
            description=dedent(
                f"""
            Using the report provided by the Senior Research Analyst, create an audience-friendly summary. Focus on:
            * Explaining the report's purpose in plain language
            * Highlighting the report's most important conclusions
            * Maintaining a clear and engaging writing style
            """
            ),
            expected_output="A summary with atleast 1 paragraph and save result as summary.txt\
            following this fortmat : \
                * Introduction to the topic of {Purpose} \
                    * Key findings and insights directly related to {Purpose} \
                        * Actionable recommendations or implications \
                -- End of Summary --\
                Do not include this '''<|im_end|>''' in your summary",
            agent=agent,
            output_file="summary.txt"
        )
