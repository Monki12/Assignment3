def calculator_tool(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return "Error in calculation"

def weather_tool(location: str) -> str:
    # Mocking an API call
    return f"It is currently 25°C and sunny in {location.title()}."

def summarize_tool(text: str) -> str:
    # Simple rule-based summary: return the first sentence
    sentences = text.split('.')
    return sentences[0] + "." if len(sentences) > 0 else "Text too short."