import datetime

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error calculating: {e}"

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def main():
    print("🤖 Rule-Based Agent initialized. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ").lower()
        
        if "exit" in user_input:
            print("Agent: Goodbye!")
            break
            
        # Decision Logic (Rule-based)
        if "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
            # Simple extraction: remove words, keep math
            math_expr = ''.join(char for char in user_input if char in '0123456789+-*/(). ')
            print(f"Agent: The result is {calculate(math_expr)}")
            
        elif "date" in user_input:
            print(f"Agent: Today's date is {get_date()}")
            
        elif "hello" in user_input or "hi" in user_input:
            print("Agent: Hello there! I can calculate math or tell you the date.")
            
        else:
            print("Agent: I don't understand that command based on my current rules.")

if __name__ == "__main__":
    main()