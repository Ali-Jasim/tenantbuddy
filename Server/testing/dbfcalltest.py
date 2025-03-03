import ollama


# Step 1: Define the function
def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The sum of the two numbers
    """
    return a + b


# Step 2: Define available functions (for mapping later)
available_functions = {"add_two_numbers": add_two_numbers}

# Step 3: Call Ollama with the tool
response = ollama.chat(
    model="smollm2",  # Use a model that supports tool calling
    messages=[{"role": "user", "content": "What is 5 plus 3?"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "add_two_numbers",
                "description": "Add two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "integer", "description": "The first number"},
                        "b": {"type": "integer", "description": "The second number"},
                    },
                    "required": ["a", "b"],
                },
            },
        }
    ],
)

# Step 4: Process the response
message = response["message"]
if "tool_calls" in message:
    for tool in message["tool_calls"]:
        function_name = tool["function"]["name"]
        function_args = tool["function"]["arguments"]

        # Get the function from our dictionary and call it
        function_to_call = available_functions.get(function_name)
        if function_to_call:
            result = function_to_call(**function_args)
            print(f"Function output: {result}")  # Should print 8
        else:
            print(f"Function {function_name} not found")
else:
    print("No tool calls in response")
    print(message["content"])
