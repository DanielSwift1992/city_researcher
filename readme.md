# Neighborhood Evaluation Project

## Overview

This project aims to evaluate and recommend neighborhoods for users based on their specific needs, preferences, and constraints. It utilizes a series of agents and tasks to gather comprehensive information from users and perform detailed analysis to provide personalized recommendations.

## Key Components

### 1. Agents

Agents are responsible for performing specific roles within the evaluation process. Each agent has a defined role, goal, backstory, and a set of tools they can use to achieve their tasks.

#### Agents Used:

- **Neighborhood Research Manager**: Oversees and coordinates the entire process of neighborhood evaluation.
- **Safety Research Agent**: Collects and analyzes safety data to provide a safety score for each neighborhood.
- **Lifestyle Preferences Agent**: Matches neighborhoods with user lifestyle preferences.
- **Budget and Affordability Agent**: Evaluates neighborhoods based on the user’s budget.
- **Amenities Evaluation Agent**: Scores neighborhoods based on the availability and quality of amenities.
- **Schools and Education Agent**: Assesses the quality of educational amenities.
- **Parks and Recreation Agent**: Scores neighborhoods based on parks and recreational facilities.
- **Public Transport Agent**: Evaluates the accessibility and quality of public transport options.
- **Food and Drink Agent**: Scores neighborhoods based on the availability and quality of dining options.
- **Reviews and Descriptions Agent**: Collects and analyzes user reviews and descriptions of neighborhoods.
- **Reviews Search Agent**: Searches and summarizes reviews for neighborhoods.

### 2. Tasks

Tasks are specific activities assigned to agents. Each task has a description, expected output format, and tools used.

#### Tasks Defined:

- **Safety Analysis Task**: Analyzes and scores the safety of each neighborhood in the city using available data on crime rates and safety reports.
- **Amenities Evaluation Task**: Evaluates and scores the amenities available in each neighborhood considering factors such as the quality of schools, parks, public transport, and food and drink options.
- **Budget Analysis Task**: Analyzes and scores neighborhoods based on affordability.
- **Lifestyle Matching Task**: Matches neighborhoods with user lifestyle preferences.

### Results

The results of the evaluation are compiled and presented to the user, providing a comprehensive overview of the best neighborhoods based on their specific criteria.

## Installation and Usage

### Prerequisites

- Python 3.7 or higher
- Poetry

### Installing Poetry on Mac

1. Open your terminal.
2. Install Poetry by running the following command:

   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Add Poetry to your PATH by following the instructions provided after the installation completes.

### Setting Up the Project

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the dependencies using Poetry:

   ```sh
   poetry install
   ```

3. Activate the Poetry shell:

   ```sh
   poetry shell
   ```

### Running the Project

Run the main script:

```sh
poetry run python main.py
```

This will start the neighborhood evaluation process using the defined agents and tasks.
