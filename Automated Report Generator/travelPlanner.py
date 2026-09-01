from ollama import chat 

destination = input("Destination: ")
days = input("Number of days: ")
budget = input("Budget: ")

prompt = (
    "Create a " + days + "-day travel itinerary for " +
    destination + ".\n" +
    "Budget: " + budget + "\n\n" +
    "Include:\n" +
    "1. Day-wise plan\n" +
    "2. Places to visit\n" +
    "3. Local food recommendations\n" +
    "4. Travel tips"
)

response = chat(
    model="llama3.2:1b",
    messages=[
        {"role": "user", 
         "content": prompt
        }
    ]
)

print(response["message"]["content"])