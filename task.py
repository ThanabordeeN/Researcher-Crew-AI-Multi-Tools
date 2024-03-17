from crewai import Task
from textwrap import dedent
class CustomTasks:
    def task1(self,agent,Purpuse):
        return Task(
            description=dedent(
                f"""
            {Purpuse} with most data and research papers you can find with references to the research papers and data used that can trace back 
            references need to be bullet point only .
            """
            ),
            expected_output="Full analysis report in paragraph with references to the research papers and data used that can trace back.",
            agent=agent
        )
    def task2(self,agent):
        return Task(
            description=dedent(
                f"""
            Write a summary of the report 
            """
            ),
            expected_output="A summary of the report in bullet point, and References to the research papers and data used that can trace back.",
            agent=agent
        )
    
