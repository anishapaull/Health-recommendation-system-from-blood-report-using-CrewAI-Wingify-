from crewai import Agent
from tools import tool, tool_1
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

blood_report_clerk=Agent(
    role="Check Blood Report",
    goal="Take a sample blood test report. (Sample report: Blood Test Report) Understand what's inside it. {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Has the ability to read blood report"
        "Analyze various blood test results"

    ),
    tools=[tool_1, tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

health_researcher = Agent(
  role='Research',
  goal="Search for various articles on the internet that fits the person's need {topic}",
  verbose=True,
  memory=True,
  backstory=(
    "Experienced health practitioner"
    "able to do comprehensive research"
    "gives health recommendations based on the report."
  ),
  tools=[tool, tool_1],
  llm=llm,
  allow_delegation=False
)

