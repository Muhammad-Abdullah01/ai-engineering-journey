import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str) -> str:
    """
    Search the web for current information.
    """
    try:
        results = tavily_client.search(query=query, max_results=3)
        summaries = [r["content"][:300] for r in results["results"]]
        return "\n\n".join(summaries)
    except Exception as e:
        return f"Search failed: {e}"


def calculator(expression: str) -> str:
    """
    Safely evaluate a basic math expression.
    """
    try:
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "Error: invalid characters in expression."
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation failed: {e}"


# This describes the tools to Gemini in a format it understands
TOOL_DEFINITIONS = [
    {
        "name": "web_search",
        "description": "Search the web for current information, facts, or recent events.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The search query"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "calculator",
        "description": "Evaluate a mathematical expression, e.g. '2 + 2' or '15 * 3.5'.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "The math expression to evaluate"}
            },
            "required": ["expression"]
        }
    }
]

# Maps tool names to actual functions, so the agent can call them by name
AVAILABLE_FUNCTIONS = {
    "web_search": web_search,
    "calculator": calculator
}