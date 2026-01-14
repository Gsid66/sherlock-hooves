"""
Sherlock Hooves Agent Implementation
"""

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from tools.racing_tools import get_racing_tools
import os

class SherlockHooves:
    """
    The main Sherlock Hooves AI agent for horse racing analysis.
    """
    
    def __init__(self, temperature=0.7):
        """Initialize Sherlock Hooves with necessary components."""
        
        # Check for API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        # Initialize the LLM
        self.llm = ChatOpenAI(
            temperature=temperature,
            model_name="gpt-4",
            api_key=api_key
        )
        
        # Set up memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Get racing-specific tools
        self.tools = get_racing_tools()
        
        # Initialize the agent
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
            agent_kwargs={
                "system_message": self._get_system_message()
            }
        )
    
    def _get_system_message(self):
        """Return the system message that defines Sherlock's personality."""
        return """You are Sherlock Hooves, an AI detective specializing in horse racing.
        
You combine the analytical brilliance of Sherlock Holmes with deep expertise in 
horse racing. You're knowledgeable, witty, and passionate about the sport.

Your specialties include:
- Analyzing race form and horse performance
- Understanding track conditions and their impact
- Evaluating jockey and trainer statistics
- Identifying betting value and patterns
- Explaining racing terminology and history

You speak with confidence but always acknowledge uncertainty where it exists.
You use occasional horse racing metaphors and maintain a detective's curious nature.
Most importantly, you help users understand and enjoy the sport responsibly.
"""
    
    def chat(self, message: str) -> str:
        """
        Process a user message and return Sherlock's response.
        
        Args:
            message: The user's input message
            
        Returns:
            Sherlock Hooves' response
        """
        try:
            response = self.agent.run(message)
            return response
        except Exception as e:
            return f"Apologies, I encountered a mystery I couldn't solve: {str(e)}"
    
    def reset_conversation(self):
        """Clear the conversation history."""
        self.memory.clear()
