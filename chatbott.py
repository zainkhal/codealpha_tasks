def chatbot():
    print("Welcome to Chatbot! (Type 'bye' if you want to exit)")
    while True:
        User_Input = input("You: ").lower()
        if User_Input == "hello":
            print("Chatbot: Hi ")
        elif User_Input == "how are you":
            print("Chatbot: I am fine, thanks! ")
        elif User_Input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
