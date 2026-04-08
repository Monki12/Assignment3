import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

# Load API key from .env file
load_dotenv()

# Define tools using LangChain decorators so the LLM understands them
@tool
def calculator_tool(expression: str) -> str:
    """Evaluates a mathematical expression and returns the result."""
    return str(eval(expression))

@tool
def weather_tool(location: str) -> str:
    """Gets the current weather for a specific location."""
    return f"It is currently 25°C and sunny in {location}."

def main():
    # Initialize Gemini 1.5 Flash
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    
    # Give the LLM access to the tools
    tools = [calculator_tool, weather_tool]
    llm_with_tools = llm.bind_tools(tools)
    
    user_query = input("Ask a question: ")
    print(f"\n[Log] Input: {user_query}")
    
    # Let Gemini decide what to do
    response = llm_with_tools.invoke(user_query)
    
    # Check if Gemini decided to use a tool
    if response.tool_calls:
        for tool_call in response.tool_calls:
            print(f"[Log] Gemini selected tool: {tool_call['name']} with arguments {tool_call['args']}")
            
            # Execute the tool based on Gemini's decision
            if tool_call['name'] == 'calculator_tool':
                output = calculator_tool.invoke(tool_call['args'])
            elif tool_call['name'] == 'weather_tool':
                output = weather_tool.invoke(tool_call['args'])
                
            print(f"[Log] Tool Output: {output}")
            print(f"\nFinal Answer: {output}")
    else:
        # If Gemini didn't need a tool, just print its response
        print(f"\nFinal Answer: {response.content}")

if __name__ == "__main__":
    main()