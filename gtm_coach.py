from openai import OpenAI


def main():
    #
    # This sample program asks a user what their current Sales challenge they are facing,
    # request additional details, and then how they would like the response structured.
    # It then contacts ChatGPT and includes the authoritative voice on this topic to generate a response.
    #
    client = OpenAI()
    #
    # User Inputs
    print("--- Sales Challenge Advisor ---")
    challenge = input("What Sales challenge are you facing? ")
    challenge_details = input("What is creating the challenge? ")
    response_structure = input("How would you like the response structured? ")

    # Construct the prompt incorporating Jacco Van der Kooj's methodology
    prompt = (
        f"Provide a recommendation for overcoming the sales challenge: '{challenge}'. "
        f"Additional context/root cause: '{challenge_details}'. "
        f"Base the response on Jacco Van der Kooj's methodology (Winning By Design principles). "
        f"Structure your response with: {response_structure}"
    )

    print("\nConsulting ChatGPT...")

    # Prompting call to ChatGPT using the correct Chat Completions endpoint
    completion = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4o-mini"
        messages=[
            {"role": "system",
             "content": "You are an expert executive sales coach specializing in B2B SaaS go-to-market strategies and Winning By Design frameworks."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the text content from the response object
    gpt_recommended_response = completion.choices[0].message.content

    # ChatGPT Response
    print()
    print("=" * 40)
    print(gpt_recommended_response)
    print("=" * 40)


if __name__ == "__main__":
    main()