from crewai import Agent, Task
from crewai_tools import ScrapeWebsiteTool
from langchain.tools import tool


class BrowserTools:
    @tool("Scrape the website and summarize the content")
    def scrape_and_summarize_website(website, summeryAndOutputRequirements):
        """Useful to scrape and summarize a website content"""
        # Initialize the tool with the website URL
        tool = ScrapeWebsiteTool(website_url=website)

        # Extract the text from the site
        content = tool.run()

        # Split content into chunks if it's too large
        content_chunks = [content[i : i + 8000] for i in range(0, len(content), 8000)]
        summaries = []

        for chunk in content_chunks:
            agent = Agent(
                role="Principal Researcher",
                goal=f"""Do amazing research and summaries based on the content 
                you are working with. Your input might be a chunk of data.
                Summary (output) requirements: {summeryAndOutputRequirements}.
                """,
                backstory="You're a Principal Researcher at a big company and you need to do research about a given topic.",
                allow_delegation=False,
            )
            task = Task(
                agent=agent,
                description=f"Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}",
                expected_output="A concise and relevant summary of the provided content chunk.",
            )
            summary = task.execute()
            summaries.append(summary)

        return "\n\n".join(summaries)
