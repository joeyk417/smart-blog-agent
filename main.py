from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import Replicate

load_dotenv()


# Topic that will be used in the crew run
topic = 'AI in healthcare'

llama3_70b = "meta/meta-llama-3-70b-instruct"
llm = Replicate(
        model=llama3_70b,
        temperature=0.5,
        # additional_kwargs={"top_p": 1, "max_new_tokens": 300},
    )

# LangChain community DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()
# @tool('DuckDuckGoSearch')
# def search_duck(search_query: str):
#   return DuckDuckGoSearchRun().run(search_query)



# Creating a senior researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal=f'Uncover groundbreaking technologies around {topic}',
  llm=llm,  # Assigning the LLM to the agent
  tools=[search_tool],
  verbose=True,
  allow_delerminator=False,
  # max_iter=3,
  backstory="""Driven by curiosity, you're at the forefront of
  innovation, eager to explore and share knowledge that could change
  the world."""
)

# Creating a writer agent
writer = Agent(
  role='Writer',
  goal=f'Narrate compelling tech stories around {topic}',
  llm=llm,  # Assigning the LLM to the agent
  verbose=True,
  allow_delerminator=True,
  # max_iter=3,
  backstory="""ith a flair for simplifying complex topics, you craft
  engaging narratives that captivate and educate, bringing new
  discoveries to light in an accessible manner."""
)


# Research task for identifying AI trends
research_task = Task(
  description=f"""Identify the next big trend in {topic}.
  Focus on identifying pros and cons and the overall narrative.
  Your final report should clearly articulate the key points,
  its market opportunities, and potential risks.
  """,
  expected_output='A comprehensive 3 paragraphs 500 words long report on the latest AI trends.',
  # max_inter=3,
  agent=researcher
)

# Writing task based on research findings
write_task = Task(
  description=f"""Compose an insightful article on {topic} by using a funny tune.
  Focus on the latest trends and how it's impacting the industry.
  This article should be 500 words with sub titles and bullet points, easy to understand, engaging and positive.
  """,
  expected_output=f'A 4 paragraph article on {topic} advancements with 2 internet articles titles and their URL.',
  agent=writer
)

# Forming the tech-focused crew
crew = Crew(
  agents=[researcher, writer], 
  tasks=[research_task, write_task], 
  process=Process.sequential  # Sequential task execution
)

result = crew.kickoff()
print(result)