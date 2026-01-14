"""
Sherlock Hooves - Main Entry Point
Your AI Horse Racing Detective
"""

import os
from dotenv import load_dotenv
from agents.sherlock_agent import SherlockHooves

def main():
    # Load environment variables
    load_dotenv()
    
    # ASCII Art Banner
    print("""
    ╔═══════════════════════════════════════════╗
    ║   🐴 SHERLOCK HOOVES 🔍                  ║
    ║   Your AI Horse Racing Detective         ║
    ╚═══════════════════════════════════════════╝
    """)
    
    # Initialize the agent
    try:
        agent = SherlockHooves()
        print("Sherlock Hooves is ready to investigate!\n")
        print("Ask me anything about horse racing, or type 'exit' to quit.\n")
        
        # Interactive loop
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nSherlock Hooves: Elementary! Until next time! 🎩")
                break
            
            if not user_input:
                continue
            
            # Get response from agent
            response = agent.chat(user_input)
            print(f"\nSherlock Hooves: {response}\n")
    
    except Exception as e:
        print(f"Error initializing Sherlock Hooves: {e}")
        print("\nMake sure you have set up your .env file with required API keys!")

if __name__ == "__main__":
    main()
