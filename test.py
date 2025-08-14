import unittest
from conversational import run_conversation

class TestXAgentIntegration(unittest.TestCase):
    def test_agent_response(self):
        response = run_conversation("Hello, what tools do you have?")
        self.assertIsNotNone(response)
        

if __name__ == "__main__":
    unittest.main()
