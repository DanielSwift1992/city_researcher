from enum import Enum
from textwrap import dedent

from crewai import Agent, Crew, Task

from tasks.neighborhoodTasks import OutputFilePaths
from tools.file_tools import FileTools


class FileTestAgent:
    def write_file_agent(self):
        return Agent(
            role="File Writer",
            backstory=dedent(
                """Experienced in handling file operations, including writing data to files efficiently."""
            ),
            goal=dedent(f"""Write specified content to a file at a given path.
            Ensure the file is created and data is accurately written. File path for the data: {OutputFilePaths.SAFETY_ANALYSIS.value}"""),
            tools=[
                FileTools.write_file,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Status: [Success or Failure]
                - File Path: [Path to the written file]
                - Message: [Detailed message about the operation]
            """),
            max_iter=3,
            max_max_rpm=3,
            verbose=True,
            allow_delegation=False,
        )

    def read_file_agent(self):
        return Agent(
            role="File Reader",
            backstory=dedent(
                """Skilled in retrieving data from files and ensuring data integrity during read operations."""
            ),
            goal=dedent(f"""Read the content from a specified file path.
            Ensure the content is read accurately. File path for the data: {OutputFilePaths.SAFETY_ANALYSIS.value}"""),
            tools=[
                FileTools.read_file,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Status: [Success or Failure]
                - File Path: [Path to the read file]
                - Content: [Content read from the file]
            """),
            max_iter=3,
            max_max_rpm=3,
            verbose=True,
            allow_delegation=False,
        )


def main():
    # Define the file path and data to write
    file_path = OutputFilePaths.SAFETY_ANALYSIS.value
    data = "This is a test content for the file."

    # Create the agents
    file_test_agent = FileTestAgent()
    writer_agent = file_test_agent.write_file_agent()
    reader_agent = file_test_agent.read_file_agent()

    # Create write and read tasks
    write_task = Task(
        description="Write content to file",
        data=(data, file_path),
        expected_output="File written to ./workdir/safety_analysis.json.",
        agent=writer_agent,
    )

    read_task = Task(
        description="Read content from file",
        data=file_path,
        expected_output="This is a test content for the file.",
        agent=reader_agent,
    )

    # Create the crew
    crew = Crew(
        agents=[writer_agent, reader_agent],
        tasks=[write_task, read_task],
        verbose=True,
    )

    # Execute the tasks
    result = crew.kickoff()
    return result


result = main()
print(result)
