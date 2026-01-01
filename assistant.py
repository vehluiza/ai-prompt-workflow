from prompts import PROMPTS

def build_prompt(prompt_type, user_input):
    prompt = PROMPTS.get(prompt_type)
    if not prompt:
        return "Prompt type not found."

    full_prompt = f"""
Role: {prompt['role']}
Task: {prompt['task']}
Output format: {prompt['output_format']}

User input:
{user_input}
"""
    return full_prompt


if __name__ == "__main__":
    text = "This is a simple text that needs improvement."
    result = build_prompt("improve_text", text)
    print(result)