import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import TOOL_DEFINITIONS, AVAILABLE_FUNCTIONS

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class AgentError(Exception):
    pass


def run_agent(user_question: str, max_steps: int = 5) -> str:
    """
    Run the agent loop: let Gemini decide whether to use tools,
    execute them, and feed results back until it gives a final answer.
    """
    tools = types.Tool(function_declarations=TOOL_DEFINITIONS)
    config = types.GenerateContentConfig(tools=[tools])

    conversation = [
        types.Content(role="user", parts=[types.Part(text=user_question)])
    ]

    for step in range(max_steps):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=conversation,
                config=config
            )
        except Exception as e:
            raise AgentError(f"Model call failed: {e}")

        candidate = response.candidates[0]
        function_call_found = False

        for part in candidate.content.parts:
            if part.function_call:
                function_call_found = True
                func_name = part.function_call.name
                func_args = dict(part.function_call.args)

                print(f"  🔧 Agent is using tool: {func_name}({func_args})")

                if func_name not in AVAILABLE_FUNCTIONS:
                    result = f"Error: unknown tool {func_name}"
                else:
                    result = AVAILABLE_FUNCTIONS[func_name](**func_args)

                # Add the model's tool request AND our result to the conversation
                conversation.append(candidate.content)
                conversation.append(
                    types.Content(
                        role="user",
                        parts=[types.Part.from_function_response(
                            name=func_name,
                            response={"result": result}
                        )]
                    )
                )

        if not function_call_found:
            # No tool call means the model gave a final answer
            return candidate.content.parts[0].text

    return "Agent reached maximum steps without a final answer."
    