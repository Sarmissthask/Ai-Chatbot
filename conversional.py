from xagent import XAgent
def get_agent():
    agent = XAgent(
        tools=[...],  
        memory_config={...},  
        other_params="..."  
    )
    return agent

def run_conversation(query):
    agent = get_agent()
    result = agent.run(query)
    return result
