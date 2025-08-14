
from xagent import XAgent

class DialogueAgentWithTools:
    def __init__(self, tools):
        self.agent = XAgent(tools=tools)

    def converse(self, message):
        return self.agent.run(message)
