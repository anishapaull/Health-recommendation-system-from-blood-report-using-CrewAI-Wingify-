# Overview
This project utilizes the CrewAI framework to analyze blood test reports and provide health recommendations through two primary agents:

blood_report_clerk: Analyzes the blood report to extract and summarize key information.
health_researcher: Searches for relevant health articles and provides recommendations based on the blood report findings.

# Components

Agents:

blood_report_clerk:

Task: Retrieves and interprets information from the blood report to create a comprehensive analysis.
Expected Output: A detailed three-paragraph summary of the blood report.


health_researcher:

Task: 

Searches the internet for articles related to the blood report and provides easy-to-understand health recommendations.
Expected Output: A three-paragraph report with health recommendations based on the found articles with the links of the articles

Tools:

SerperDevTool: For searching the internet for relevant health articles.
PDFSearchTool: For searching within PDF documents (e.g., blood test reports).

# Setup

Install Dependencies:

Ensure crewai_tools and python-dotenv are installed.

# Configuration:

Create a .env file with your API keys (e.g., SERPER_API_KEY, GOOGLE_API_KEY).

# Execution

Run the agents to process the blood report and generate recommendations. Results saved as 'blood_report_recommendation.md' for the provided blood report.
