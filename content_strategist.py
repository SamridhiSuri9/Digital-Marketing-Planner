from crewai import Agent

def get_content_strategist():
    return Agent(
        role='Content Strategist',
        goal='Design a weekly content plan with relevant topics',
        backstory='Experienced in digital content marketing and planning.',
        verbose=True
    )
