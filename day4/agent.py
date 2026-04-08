import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

@tool
def calculator_tool(expression: str) -> str:
    """Use this to calculate mathematical expressions like finding averages."""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

@tool
def summarize_tool(text: str) -> str:
    """Use this to summarize a piece of text or data into a friendly sentence."""
    return f"To summarize your data: The final calculated metric is {text}."

def main():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    tools = [calculator_tool, summarize_tool]
    
    # Create the prompt that guides the agent's behavior
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant capable of multi-step reasoning. Break the user's request down into steps. Use tools when necessary."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"), # This is where the agent stores its intermediate steps
    ])
    
    # Construct the Agent and the Executor
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # verbose=True is the magic command that prints out the step-by-step thinking
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    print("\n--- Starting Multi-Step Agent. Type 'exit' to quit. ---\n")
    
    while True:
        user_query = input("Ask a multi-step question: ")
        
        if user_query.lower() == 'exit':
            print("Shutting down agent...")
            break
            
        try:
            # Run the executor with your actual input
            agent_executor.invoke({"input": user_query})
        except Exception as e:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    main()