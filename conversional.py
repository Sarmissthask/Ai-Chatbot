from xagent import XAgent

def get_agent():
    # Initialize the XAgent with the required configuration
    agent = XAgent(
        tools=[...],  # List your tools here
        memory_config={...},  # XAgent's memory setup
        other_params="..."  # Any other params required
    )
    return agent

def run_conversation(query):
    agent = get_agent()
    result = agent.run(query)
    return result
