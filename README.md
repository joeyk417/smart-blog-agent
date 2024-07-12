# AI Healthcare Research and Writing Automation

This project leverages the power of large language models (LLMs) and automated search tools to streamline the process of researching and writing about AI in healthcare. By integrating LangChain community tools and a sophisticated agent-based model, it aims to uncover groundbreaking technologies and narrate compelling stories around AI's impact on healthcare.

## Features

- **Automated Research**: Utilizes a senior researcher agent to conduct in-depth research on AI trends in healthcare, focusing on identifying pros, cons, and the overall narrative.
- **Content Creation**: Employs a writer agent to craft engaging and insightful articles on the latest AI advancements in healthcare, ensuring the content is accessible, engaging, and informative.
- **Sequential Task Execution**: Manages tasks in a sequential process, ensuring that research is completed before writing begins, to maintain coherence and relevance in the content produced.
- **Customizable Agents**: Both the researcher and writer agents are customizable, allowing for adjustments in goals, tools, and verbosity to suit different research and writing styles.
- **Integration with LangChain Community Tools**: Incorporates LangChain community tools like the DuckDuckGoSearchRun for efficient online research.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repository/ai-healthcare-research.git
   cd ai-healthcare-research
   ```

2. **Install Dependencies**

   Ensure you have Python 3.8+ installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Create a .env file in the root directory and populate it with necessary environment variables, if any.

5. **Running the Project**

   Execute the main script to start the research and writing process:
   ```
   python main.py
   ```

## How It Works

- **Initialization:** The project starts by loading environment variables and setting up the LLM and search tool.
- **Agent Creation:** Two agents, a senior researcher and a writer, are created with specific roles, goals, and tools.
- **Task Definition:** Research and writing tasks are defined, detailing the expectations and outputs for each agent.
- **Crew Formation:** A crew is formed with the agents and tasks, and the process is set to sequential execution.
- **Execution:** The crew kicks off the process, executing tasks in sequence and outputting the results.

## Customization

You can customize the project by modifying the agents' goals, the LLM model used, or the search tool. Additionally, you can adjust the task descriptions and expected outputs to focus on different aspects of AI in healthcare.
