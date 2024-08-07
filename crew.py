from crewai import Crew,Process
from tasks import research_task,recommendation_task
from agents import blood_report_clerk, health_researcher

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[blood_report_clerk,health_researcher],
    tasks=[research_task,recommendation_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Blood Test Analysis'})
print(result)