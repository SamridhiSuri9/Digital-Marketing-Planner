from crewai import Agent

def get_audience_profiler():
    return Agent(
        role='Audience Profiler',
        goal='Identify the target audience for a digital product',
        backstory='Expert in market research and consumer analysis.',
        verbose=True 
    )
