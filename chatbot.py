import datetime

# Function to get a response based on user input
def get_response(user_input: str, user_name: str) -> str:
    # Define responses based on specific keywords or phrases
    match user_input:
        case user_input if any(x in user_input for x in ["angry", "anger", "rage"]):
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Anger makes dull men witty, but it keeps them poor. -Elizabeth I.\nHow else are you feeling?"
        case user_input if any(x in user_input for x in ["unhapp", "sad", "depress"]):
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: There is no path to happiness. Happiness is the path. –Buddha.\nHow else are you feeling?"
        case user_input if "annoy" in user_input:
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Everything that irritates us about others can lead us to an understanding of ourselves. – Carl Jung.\nHow else are you feeling?"
        case user_input if "frustrat" in user_input:
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain\nHow else are you feeling?"
        case user_input if "bored" in user_input:
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Is life not a thousand times too short for us to bore ourselves? – Friedrich Nietzsche\nHow else are you feeling?"
        case user_input if "lonel" in user_input:
            return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: The thing that makes you exceptional, if you are at all, is inevitably that which must also make you lonely. - Lorraine Hansberry\nHow else are you feeling?"
        case _:
            return f"I'm sorry, {user_name}, I don't understand that. Can you please rephrase?"

# Function to get the current greeting based on the time of day
def get_greeting() -> str:
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Main function to run the chatbot
def main():
    print("Hello! Welcome to the simple Python chatbot!")

    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    print(f"{greeting}, {user_name}!  I'm here to motivate you.\nHow are you feeling today?")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()