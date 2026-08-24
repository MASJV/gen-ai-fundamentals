from ollama import generate

text = input("Enter details such as starting location, destination, travel dates and budget for trip planning: ")

prompt = ("Plan a trip based on the following details:\n" 
    + text + 
    '\nReturn only valid JSON in this exact format: {"starting location": ["..."], "destination": ["..."], "travel dates": ["..."], "budget": "..."}'
)
response = generate(
    model = "llama3.2:1b", 
    prompt = prompt,
)

print(response["response"])