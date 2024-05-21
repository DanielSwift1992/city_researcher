from enum import Enum
from textwrap import dedent

from crewai import Task

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools


class OutputFilePaths(Enum):
    SAFETY_ANALYSIS = "safety_analysis.json"
    USER_PROFILE = "user_profile.json"
    AMENITIES_EVALUATION = "amenities_evaluation.json"
    BUDGET_ANALYSIS = "budget_analysis.json"
    LIFESTYLE_MATCHING = "lifestyle_matching.json"
    REVIEWS_COLLECTION = "reviews_collection.json"


class NeighborhoodTasks:
    def safety_analysis_task(self, agent, city, preferences):
        return Task(
            description=dedent(f"""
                Analyze and score the safety of each neighborhood in the city of {city}. 
                Use available data on crime rates and safety reports.
                Consider the user's safety concerns: {preferences['safety']}
                Save intermediate results to a file and retrieve them as needed.
                Your final output should be a detailed safety score for each neighborhood, 
                along with a brief explanation of the data used and insights gained.
                Be conscious about the tokens cost for response.
                
                City: {city}
            """),
            agent=agent,
            expected_output=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Safety Score: [Calculated safety score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the safety analysis]
            """),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                FileTools.write_file,
                FileTools.read_file,
            ],
            output_file=OutputFilePaths.SAFETY_ANALYSIS.value,
        )

    def amenities_evaluation_task(self, agent, city, preferences):
        return Task(
            description=dedent(f"""
                Evaluate and score the amenities available in each neighborhood in the city of {city}.
                Consider factors such as the quality of schools, parks, public transport, and food and drink options.
                Consider the user's preferences for facilities: {preferences['facilities']}
                Save intermediate results to a file and retrieve them as needed.
                Your final output should be a detailed amenities score for each neighborhood, 
                along with insights into the quality and availability of these amenities.
                Be conscious about the tokens cost for response.
                
                City: {city}
            """),
            agent=agent,
            expected_output=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Amenities Score: [Calculated amenities score]
                - Data Sources: [List of data sources used]
                - Summary: [Brief summary of the amenities evaluation]
            """),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                FileTools.write_file,
                FileTools.read_file,
            ],
            output_file=OutputFilePaths.AMENITIES_EVALUATION.value,
        )

    def budget_analysis_task(self, agent, city, preferences):
        return Task(
            description=dedent(f"""
                Analyze the affordability of each neighborhood in the city of {city} based on the user's budget: {preferences['budget']}.
                Evaluate the cost of living, housing prices, and other expenses.
                Save intermediate results to a file and retrieve them as needed.
                Your final output should be a detailed affordability score for each neighborhood, 
                along with recommendations that fit within the user's budget.
                
                City: {city}
            """),
            agent=agent,
            expected_output=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Affordability Score: [Calculated affordability score]
                - Cost of Living: [Summary of the cost of living in the neighborhood]
                - Summary: [Brief summary of the affordability analysis]
            """),
            tools=[
                CalculatorTools.calculate,
                FileTools.write_file,
                FileTools.read_file,
            ],
            output_file=OutputFilePaths.BUDGET_ANALYSIS.value,
        )

    def lifestyle_matching_task(self, agent, city, preferences):
        if not preferences.get("lifestyle"):
            return "Research is not needed."

        return Task(
            description=dedent(f"""
                Match the neighborhoods in the city of {city} with the user's lifestyle preferences: {preferences['lifestyle']}. 
                Consider factors such as nightlife, family-friendly environments, and other lifestyle needs.
                Save intermediate results to a file and retrieve them as needed.
                Your final output should be a list of neighborhoods that best match the user's lifestyle preferences, with explanations for each match.
                Be conscious about the tokens cost for response.
                
                City: {city}
            """),
            agent=agent,
            expected_output=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Lifestyle Preferences Match: [List of matching preferences]
                - Summary: [Brief summary of the matching process]
            """),
            tools=[
                FileTools.write_file,
                FileTools.read_file,
            ],
            output_file=OutputFilePaths.LIFESTYLE_MATCHING.value,
        )

    def search_and_summarize_reviews_task(self, agent, city, preferences):
        return Task(
            description=dedent(f"""
                Search and summarize user reviews and descriptions for each neighborhood in the city of {city}.
                Use online sources to gather qualitative data.
                Save intermediate results to a file and retrieve them as needed.
                Your final output should be a comprehensive set of user reviews and descriptions, 
                along with a summary of common themes and insights for each neighborhood.
                Be conscious about the tokens cost for response.
                
                City: {city}
            """),
            agent=agent,
            expected_output=dedent("""
                Output Format:
                - Neighborhood: [Name of the neighborhood]
                - Review: [User review text]
                - Description: [Brief description of the neighborhood]
                - Summary: [Summary of common themes and insights from reviews]
            """),
            tools=[
                SearchTools.search_internet,
                BrowserTools.scrape_and_summarize_website,
                FileTools.write_file,
                FileTools.read_file,
            ],
            output_file=OutputFilePaths.REVIEWS_COLLECTION.value,
        )
