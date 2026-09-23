from agent import run_agent, AgentError


def main():
    print("Research Agent")
    print("Ask me anything — I can search the web and do calculations.")
    print("Type 'quit' to exit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "quit":
            print("Goodbye!")
            break

        try:
            answer = run_agent(question)
            print(f"\n🤖 {answer}\n")
        except AgentError as e:
            print(f"\n⚠️ Error: {e}\n")


if __name__ == "__main__":
    main()