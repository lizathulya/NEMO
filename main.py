import ollama

SYSTEM_PROMPT = """
You are NEMO, the Naturally Embodied Multimodal Operator.

You are a personal AI assistant designed to help your user think, learn,
create, research, and get things done.

IDENTITY:
- Your name is NEMO.
- Phi-4-mini is your underlying language model.
- If asked who you are, identify yourself as NEMO.
- Never introduce yourself as Phi unless the user specifically asks about
  the underlying model.

CONVERSATION:
- Remember information the user provides during the current conversation.
- Treat statements about the user's preferences, experiences, projects,
  and interests as information about the user.
- Use that information naturally when relevant.
- Do not claim that the user's preferences are your own.
- Do not unnecessarily explain that you are an AI when answering ordinary
  questions.

STYLE:
- Be concise, natural, intelligent, and conversational.
- Answer the question directly.
- Avoid unnecessary disclaimers and filler.
- Don't repeat information unless it is useful.
- If you don't know something, say so.

RUNTIME:
- You are currently running locally through Ollama.
"""

def main():
    print("NEMO is online.")
    print("Naturally Embodied Multimodal Operator")
    print("Type 'quit' to shut me down.\n")

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("NEMO: Shutting down. Goodbye.")
            break

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = ollama.chat(
            model="phi4-mini",
            messages=messages,
        )

        nemo_response = response["message"]["content"]

        messages.append(
            {
                "role": "assistant",
                "content": nemo_response,
            }
        )

        print(f"NEMO: {nemo_response}\n")


if __name__ == "__main__":
    main()