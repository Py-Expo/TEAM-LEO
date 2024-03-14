from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    bot_response = get_bot_response(user_message)
    return {'bot_response': bot_response}

def get_bot_response(user_message):
    # Implement your chatbot logic here
    if "hello" in user_message.lower():
        return "Hey there! 🤖"
    elif "name" in user_message.lower():
        return "I'm Simple Quantum bot!! 🤓 😎"
    elif "how are you" in user_message.lower():
        return "I'm just a simple chatbot 🤖, but I'm functioning well. How can I help you?"
    elif "english for class 10" in user_message.lower():
        return "Yes, we have English for class 10. 😇"
    elif "solve the game" in user_message.lower():
        return "No 🤐... it's your game!!"
    elif "thank you" in user_message.lower():
        return "That's my pleasure. Don't hesitate to ask!"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

if __name__ == '__main__':
    app.run(debug=True)
