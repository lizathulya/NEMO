import ollama


def main():
    print("NEMO is online.")
    print("Naturally Embodied Multimodal Operator")
    print("Type 'quit' to shut me down.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("NEMO: Shutting down. Goodbye.")
            break

        response = ollama.chat(
            model="phi4-mini",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )

        print(f"NEMO: {response['message']['content']}\n")


if __name__ == "__main__":
    main()