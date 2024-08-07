from crewai import Task
from tools import tool, tool_1
from agents import blood_report_clerk, health_researcher

# Research task
research_task = Task(
  description=(
    "Retrieve information from blood report {topic}."
    "Understand the blood report."
    "clearly articulate the key points and summarize it."
  ),
  expected_output='A comprehensive 3 paragraphs on the blood report analysis.',
  tools=[tool_1, tool],
  agent=blood_report_clerk,
  output_file='blood_report_summary.md'
)

# Writing task with language model configuration
recommendation_task = Task(
  description=(
    "Search the internet for articles {topic}."
    "Focus on the relevent points and appropriate health recommendation."
    "This recommendation report should be easy to understand."
    "Provide links to relevant articles of health recommendations"
    "Recommendations must be as per the person's health needs"
  ),
  expected_output='A 3 paragraph report on {topic} recommendation with relevant links',
  tools=[tool, tool_1],
  agent=health_researcher,
  async_execution=False,
  output_file='blood_report_recommendation.md'  # Example of output customization
)