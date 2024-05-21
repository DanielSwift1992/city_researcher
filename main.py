import os
from textwrap import dedent

from crewai import Crew
from dotenv import load_dotenv

from agents.neighborhoodAgents import NeighborhoodAgents
from tasks.neighborhoodTasks import NeighborhoodTasks

load_dotenv()


def prepare():
    required_vars = ["SERPER_API_KEY", "OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    if not os.path.exists("./workdir"):
        os.mkdir("./workdir")


class NeighborhoodCrew:
    def __init__(self, city, user_preferences):
        self.city = city
        self.user_preferences = user_preferences

    def run(self):
        prepare()
        agents = NeighborhoodAgents()
        tasks = NeighborhoodTasks()

        # Initialize agents
        research_manager_agent = agents.neighborhood_research_manager()
        safety_agent = agents.safety_research_agent()
        lifestyle_agent = agents.lifestyle_preferences_agent()
        budget_agent = agents.budget_and_affordability_agent()
        amenities_agent = agents.amenities_evaluation_agent()
        schools_agent = agents.schools_and_education_agent(user_preferences)
        parks_agent = agents.parks_and_recreation_agent()
        transport_agent = agents.public_transport_agent()
        food_agent = agents.food_and_drink_agent()
        reviews_agent = agents.reviews_and_descriptions_agent()
        reviews_search_agent = agents.reviews_search_agent()

        safety_task = tasks.safety_analysis_task(
            safety_agent, self.city, self.user_preferences
        )
        amenities_task = tasks.amenities_evaluation_task(
            amenities_agent, self.city, self.user_preferences
        )
        budget_task = tasks.budget_analysis_task(
            budget_agent, self.city, self.user_preferences
        )
        lifestyle_task = tasks.lifestyle_matching_task(
            lifestyle_agent, self.city, self.user_preferences
        )
        reviews_task = tasks.search_and_summarize_reviews_task(
            reviews_search_agent, self.city, self.user_preferences
        )

        # Create a single crew with all agents and tasks
        crew = Crew(
            agents=[
                research_manager_agent,
                safety_agent,
                lifestyle_agent,
                budget_agent,
                amenities_agent,
                schools_agent,
                parks_agent,
                transport_agent,
                food_agent,
                reviews_agent,
                reviews_search_agent,
            ],
            tasks=[
                safety_task,
                amenities_task,
                budget_task,
                lifestyle_task,
                reviews_task,
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Neighborhood Evaluation Crew")
    print("------------------------------------------")
    city = input(
        dedent("""
        Which city are you evaluating?
        """)
    )

    # Dummy preferences map
    user_preferences = {
        "budget": "2000-2700 USD per month",
        "lifestyle": "active",
        "family": "2 members: 2 adults (working)",
        "transportation": "car, willing to commute up to 30 minutes",
        "food_preferences": "prefer cooking at home",
        "activities": "outdoor activities, sports",
        "work_school_location": "Amazon office",
        "facilities": "parks, gyms, shopping centers",
        "safety": "high importance, low crime rate preferred",
        "rules": "quiet hours, pet-friendly",
        "favorite_spots": "cafes, libraries",
        "long_term_plans": "looking for stability and good investment potential",
    }

    # user_preferences = {}
    # user_preferences["budget"] = input(
    #     dedent("""
    #     What is your budget range for housing in the new neighborhood?
    #     """)
    # )
    # user_preferences["lifestyle"] = input(
    #     dedent("""
    #     Can you describe your lifestyle? (e.g., active, relaxed, social, private)
    #     """)
    # )
    # user_preferences["family"] = input(
    #     dedent("""
    #     How many family members will be living with you, and what are their ages and occupations/school levels?
    #     """)
    # )
    # user_preferences["transportation"] = input(
    #     dedent("""
    #     What are your primary means of transportation, and how far are you willing to commute for work or school?
    #     """)
    # )
    # user_preferences["food_preferences"] = input(
    #     dedent("""
    #     What are your food preferences? Do you prefer dining out or cooking at home?
    #     """)
    # )
    # user_preferences["activities"] = input(
    #     dedent("""
    #     What kind of activities do you and your family enjoy? (e.g., outdoor activities, cultural events, sports)
    #     """)
    # )
    # user_preferences["work_school_location"] = input(
    #     dedent("""
    #     Where is your work or school located?
    #     """)
    # )
    # user_preferences["facilities"] = input(
    #     dedent("""
    #     Are there any specific facilities or amenities that you prioritize in a neighborhood? (e.g., parks, gyms, shopping centers, schools)
    #     """)
    # )
    # user_preferences["safety"] = input(
    #     dedent("""
    #     How important is neighborhood safety to you, and are there any specific safety concerns you have?
    #     """)
    # )
    # user_preferences["rules"] = input(
    #     dedent("""
    #     Are there any specific rules or regulations you prefer in a neighborhood? (e.g., quiet hours, pet policies)
    #     """)
    # )
    # user_preferences["favorite_spots"] = input(
    #     dedent("""
    #     Do you have any favorite spots you'd like to be close to? (e.g., cafes, restaurants, libraries)
    #     """)
    # )
    # user_preferences["long_term_plans"] = input(
    #     dedent("""
    #     What are your long-term plans, and how does the stability and investment potential of the neighborhood factor into them?
    #     """)
    # )

    neighborhood_crew = NeighborhoodCrew(city, user_preferences)
    result = neighborhood_crew.run()
    print("\n\n########################")
    print("## Here is your Neighborhood Evaluation")
    print("########################\n")
    print(result)
