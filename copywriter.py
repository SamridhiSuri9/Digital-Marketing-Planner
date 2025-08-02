from crewai import Agent

def get_copywriter():
    return Agent(
        role='Copywriter',
        goal='Write 3 sample marketing posts with SEO keywords',
        backstory='Skilled at writing engaging and search-optimized content.',
        verbose=True
    )
