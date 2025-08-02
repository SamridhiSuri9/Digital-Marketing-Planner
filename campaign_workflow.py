import os
from openai import OpenAI
from crewai import Crew, Task
from agents1.audience_profiler import get_audience_profiler
from agents1.content_strategist import get_content_strategist
from agents1.copywriter import get_copywriter

from dotenv import load_dotenv
load_dotenv(override=True)

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def run_campaign_workflow(topic: str):
    audience_agent = get_audience_profiler()
    content_agent = get_content_strategist()
    copywriter_agent = get_copywriter()
    # Define tasks
    audience_task = Task(
    description="Analyze the topic and identify target audience characteristics.",
    expected_output="A profile of the ideal target audience.",
    agent=audience_agent,
    output_key="audience_data"  # ⬅ Make sure this matches!
    )
    content_task = Task(
    description="Create a weekly content strategy...",
    expected_output="Detailed content plan...",
    agent=content_agent,
    output_key="content_plan"
    )
    copywriter_task = Task(
    description="Write 3 engaging posts...",
    expected_output="Social media post samples...",
    agent=copywriter_agent,
    output_key="final_posts"
    )
    # Create crew
    crew = Crew(
        agents=[audience_agent, content_agent, copywriter_agent],
        tasks=[audience_task, content_task, copywriter_task],
        verbose=True
    )
    results = crew.kickoff()
    results_dict = dict(results)
    print("CREW OUTPUT KEYS:", results_dict.keys())

    return {
    "Target Audience": results.tasks_output[0] if len(results.tasks_output) > 0 else "Not generated.",
    "Content Strategy": results.tasks_output[1] if len(results.tasks_output) > 1 else "Not generated.",
    "Marketing Posts": results.tasks_output[2] if len(results.tasks_output) > 2 else "Not generated."
    }



    

