from dotenv import load_dotenv
load_dotenv(override=True)
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class Music():
    """Music crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def music_researcher(self) -> Agent:
        return Agent(config=self.agents_config['music_researcher'], verbose=True, tools=[SerperDevTool()])

    @agent
    def indie_label_specialist(self) -> Agent:
        return Agent(config=self.agents_config['indie_label_specialist'], verbose=True, tools=[SerperDevTool()])

    @agent
    def dsp_playlist_editor(self) -> Agent:
        return Agent(config=self.agents_config['dsp_playlist_editor'], verbose=True, tools=[SerperDevTool()])

    @agent
    def radio_programmer_dj(self) -> Agent:
        return Agent(config=self.agents_config['radio_programmer_dj'], verbose=True, tools=[SerperDevTool()])

    @agent
    def critic_podcaster(self) -> Agent:
        return Agent(config=self.agents_config['critic_podcaster'], verbose=True, tools=[SerperDevTool()])
    
    @agent
    def music_analytics_intel(self) -> Agent:
        return Agent(config=self.agents_config['music_analytics_intel'], verbose=True, tools=[SerperDevTool()])
    
    @agent
    def music_strategy_compiler(self) -> Agent:
        return Agent(config=self.agents_config['music_strategy_compiler'], verbose=True)
    
    @task
    def music_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['music_research_task'], # type: ignore[index]
        )

    @task
    def indie_label_specialist_task(self) -> Task:
        return Task(
            config=self.tasks_config['indie_label_specialist_task'], # type: ignore[index]
        )

    @task
    def dsp_playlist_editor_task(self) -> Task:
        return Task(
            config=self.tasks_config['dsp_playlist_editor_task'], # type: ignore[index]
        )

    @task
    def radio_programmer_dj_task(self) -> Task:
        return Task(
            config=self.tasks_config['radio_programmer_dj_task'], # type: ignore[index]
        )

    @task
    def critic_podcaster_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_podcaster_task'], # type: ignore[index]
        )

    @task
    def music_analytics_intel_task(self) -> Task:
        return Task(
            config=self.tasks_config['music_analytics_intel_task'], # type: ignore[index]
        )

    @task
    def music_strategy_compiler_task(self) -> Task:
        return Task(
            config=self.tasks_config['music_strategy_compiler_task'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Music crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
