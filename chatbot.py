import datetime


# Function to get a response based on user input
def get_response(user_input, user_name):
    user_input = user_input.lower()
    
    # Define responses based on specific keywords or phrases
    if "sad" in user_input:
        return f"I'm sorry to hear that, {user_name}! Your motivational quote is: If you think you are too small to make a difference, try sleeping with a mosquito. -Ghandi.  How else are you feeling?"
    elif "angry" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Anger makes dull men witty, but it keeps them poor. -Elizabeth I.  How else are you feeling?"
    elif "unhappy" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: There is no path to happiness. Happiness is the path. –Buddha.  How else are you feeling?"
    elif "annoyed" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Everything that irritates us about others can lead us to an understanding of ourselves. – Carl Jung.  How else are you feeling?"
    elif "frustrated" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain  How else are you feeling?"
    elif "bored" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Is life not a thousand times too short for us to bore ourselves? – Friedrich Nietzsche  How else are you feeling?"
    elif "lonely" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Feeling sorry for yourself, and your present condition, is not only a waste of energy but the worst habit you could possibly have. – Dale Carnegie  How else are you feeling?"
    elif "bye" in user_input or "goodbye" in user_input:
        return f"Goodbye, {user_name}! Have a great day!"
    else:
        return f"I'm sorry, {user_name}, I don't understand that. Can you please rephrase?"

# Function to get the current greeting based on the time of day
def get_greeting():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

# Main function to run the chatbot
def main():
    print("Hello! Welcome to the simple Python chatbot!")
    
    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    print(f"{greeting}, {user_name}!  I'm here to motivate you.  How are you feeling today?")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()