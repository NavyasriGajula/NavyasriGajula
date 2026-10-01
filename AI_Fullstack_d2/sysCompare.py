from ollama import chat
roles =[
    "you are a strict math teacher. answer briefly and within 1 line",
    "you are a movie director.Answer in a filmy way. one line answer",
]
for role in roles:
    response = chat(
    model = "llama3.2",
    messages=[
                {
                    "role" : "system",
                    "content" : role
                },
                {
                    "role" : "user",
                    "content" : "how many colours in rainbow?"
                }
            ]
        )
    print(f"--{role}--")
    print(response.message.content)
    print()