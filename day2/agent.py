from tools import calculator_tool, weather_tool, summarize_tool

def main():
    print("🤖 Modular Tool Agent initialized.")
    user_input = input("Enter a command (e.g., 'weather in Pune', 'calc 5+5'): ").lower()
    
    if user_input.startswith("calc"):
        expr = user_input.replace("calc", "").strip()
        result = calculator_tool(expr)
        print(f"Result: {result}")
        
    elif user_input.startswith("weather"):
        location = user_input.replace("weather in", "").strip()
        result = weather_tool(location)
        print(f"Result: {result}")
        
    elif user_input.startswith("summarize"):
        text = user_input.replace("summarize", "").strip()
        result = summarize_tool(text)
        print(f"Result: {result}")
        
    else:
        print("Command not recognized. Use 'calc', 'weather', or 'summarize'.")

if __name__ == "__main__":
    main()