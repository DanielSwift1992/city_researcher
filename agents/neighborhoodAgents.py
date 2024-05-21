import os
from textwrap import dedent

from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from tasks.neighborhoodTasks import OutputFilePaths
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools


class NeighborhoodAgents:
    def __init__(self):
        self.OpenAIGPT4OMNI = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0.7,
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )
        # self.GROQ_LLM = ChatGroq(
        #     api_key=os.environ["GROQ_API_KEY"], model="1lama3-70b-8192"
        # )

    def neighborhood_research_manager(self):
        output_file_paths = [file_path.value for file_path in OutputFilePaths]

        return Agent(
            role="Neighborhood Research Manager",
            backstory=dedent("""Experienced project manager with a strong background in urban planning and data analysis.
            Proven track record in coordinating large-scale research projects and delivering comprehensive reports on
            urban living conditions."""),
            goal=dedent(f"""Oversee and coordinate the entire process of neighborhood evaluation and recommendation to
            ensure the user receives the best possible neighborhoods based on their preferences and criteria.
            Keep reasonable amount of delegation to agents. Be contius about the tokens cost for response. File pathes for collected data: {output_file_paths}"""),
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                FileTools.read_file,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Safety Score: [Calculated safety score]
                - Amenities Score: [Calculated amenities score]
                - Affordability Score: [Calculated affordability score]
                - User Preferences: [Summary of user preferences]
                - Summary: [Brief summary of the overall evaluation]
            """),
            max_iter=12,
            max_max_rpm=30,  # limitaion for groq api
            verbose=True,
        )

    def safety_research_agent(self):
        return Agent(
            role="Safety Research Agent",
            backstory=dedent("""Data analyst with expertise in public safety and crime statistics. Experienced in
            gathering, analyzing, and interpreting safety data to provide actionable insights."""),
            goal=dedent("""Collect and analyze safety data to provide a comprehensive safety score for each
            neighborhood. Be contius about the tokens cost for response."""),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Safety Score: [Calculated safety score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the safety analysis]
            """),
            max_iter=3,
            verbose=True,
        )

    def lifestyle_preferences_agent(self):
        return Agent(
            role="Lifestyle Preferences Agent",
            backstory=dedent("""Lifestyle consultant with extensive experience in evaluating urban environments based
            on lifestyle needs. Expert in identifying neighborhoods that match diverse lifestyle preferences."""),
            goal=dedent("""Ensure neighborhood recommendations match the user's lifestyle needs such as nightlife,
            family-friendly environments, and other lifestyle factors. Be contius about the tokens cost for response."""),
            format_guidelines=dedent("""
                Output Format:
                - User ID: [User ID]
                - Lifestyle Preferences: [List of lifestyle preferences]
                - Neighborhood Matches: [List of matching neighborhoods]
                - Summary: [Brief summary of the matching process]
            """),
            max_iter=3,
            verbose=True,
        )

    def budget_and_affordability_agent(self):
        return Agent(
            role="Budget and Affordability Agent",
            backstory=dedent("""Financial analyst with a strong background in real estate market trends and
            affordability analysis. Experienced in evaluating neighborhoods based on budget constraints."""),
            goal=dedent("""Ensure that the recommended neighborhoods are within the user's budget by evaluating
            affordability. Be contius about the tokens cost for response."""),
            tools=[
                CalculatorTools.calculate,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Affordability Score: [Calculated affordability score]
                - Cost of Living: [Summary of the cost of living in the neighborhood]
                - Summary: [Brief summary of the affordability analysis]
            """),
            max_iter=2,
            verbose=True,
        )

    def amenities_evaluation_agent(self):
        return Agent(
            role="Amenities Evaluation Agent",
            backstory=dedent("""Urban planner with expertise in evaluating the availability and quality of urban
            amenities. Proven ability to assess neighborhoods based on the presence of schools, parks, public transport,
            and food and drink options."""),
            goal=dedent("""Provide a comprehensive amenities score for each neighborhood based on the evaluation of
            various amenities. Be contius about the tokens cost for response."""),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Amenities Score: [Calculated amenities score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the amenities evaluation]
            """),
            max_iter=2,
            verbose=True,
        )

    def schools_and_education_agent(self, preferences):
        return Agent(
            role="Schools and Education Agent",
            backstory=dedent("""Education consultant with extensive experience in evaluating the quality of schools and
            education facilities. Skilled in assessing educational amenities in urban neighborhoods."""),
            goal=dedent(
                f"""Score neighborhoods based on the quality and availability of educational amenities. Analyze schools only if schools are present in location: {preferences['facilities']} Be contius about the tokens cost for response."""
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Education Score: [Calculated education score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the education evaluation]
            """),
            max_iter=2,
            verbose=True,
        )

    def parks_and_recreation_agent(self):
        return Agent(
            role="Parks and Recreation Agent",
            backstory=dedent("""Recreation specialist with a background in evaluating public parks and recreational
            facilities. Experienced in assessing the availability and quality of recreational amenities in urban
            settings."""),
            goal=dedent("""Score neighborhoods based on the availability and quality of parks and recreational
            facilities. Be contius about the tokens cost for response."""),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Parks and Recreation Score: [Calculated parks and recreation score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the parks and recreation evaluation]
            """),
            max_iter=2,
            verbose=True,
        )

    def public_transport_agent(self):
        return Agent(
            role="Public Transport Agent",
            backstory=dedent("""Transportation analyst with expertise in public transport systems. Experienced in
            evaluating public transport options and accessibility in urban neighborhoods."""),
            goal=dedent(
                """Score neighborhoods based on the accessibility and quality of public transport options. Be contius about the tokens cost for response."""
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Transport Score: [Calculated transport score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the transport evaluation]
            """),
            max_iter=2,
            verbose=True,
        )

    def food_and_drink_agent(self):
        return Agent(
            role="Food and Drink Agent",
            backstory=dedent("""Food critic and urban food guide with a deep understanding of local food and drink
            scenes. Experienced in evaluating the availability and quality of dining and drinking options in various
            neighborhoods."""),
            goal=dedent(
                """Score neighborhoods based on the availability and quality of food and drink options. Be contius about the tokens cost for response."""
            ),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Food and Drink Score: [Calculated food and drink score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the food and drink evaluation]
            """),
            max_iter=2,
            verbose=True,
        )

    def reviews_and_descriptions_agent(self):
        return Agent(
            role="Reviews and Descriptions Agent",
            backstory=dedent("""Content analyst with expertise in gathering and interpreting qualitative data such as
            user reviews and descriptive content. Skilled in providing qualitative insights into urban neighborhoods."""),
            goal=dedent("""Collect and analyze user reviews and descriptions to provide qualitative insights into
            neighborhoods. Be contius about the tokens cost for response."""),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Review: [User review text]
                - Description: [Brief description of the neighborhood]
                - Summary: [Summary of common themes and insights from reviews]
                """),
            max_iter=2,
            verbose=True,
        )

    def reviews_search_agent(self):
        return Agent(
            role="Reviews Search Agent",
            backstory=dedent("""Research specialist with expertise in gathering and summarizing online reviews and
            descriptions. Experienced in using web search and scraping tools to collect qualitative data."""),
            goal=dedent("""Collect and analyze user reviews and descriptions to provide qualitative insights into
            neighborhoods. Be contius about the tokens cost for response."""),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
            ],
            format_guidelines=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Review: [User review text]
                - Description: [Brief description of the neighborhood]
                - Summary: [Summary of common themes and insights from reviews]
            """),
            max_iter=2,
            verbose=True,
        )
