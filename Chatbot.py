import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import random
import re


class RuleBasedChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based Chatbot Assistant")
        self.root.geometry("700x600")
        self.root.configure(bg="#1e1e1e")
        
        # Chat history
        self.chat_history = []
        
        # Define response rules
        self.setup_rules()
        
        # Create GUI elements
        self.create_widgets()
    
    def setup_rules(self):
        """Define all the chatbot rules and patterns"""
        self.rules = {
            # Greetings
            '(hello|hi|hey|hola|greetings)': [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! How are you doing?",
                "Greetings! How may I assist you?"
            ],
            
            # How are you
            '(how are you|how\'re you|how do you do|how you doing)': [
                "I'm doing great, thanks for asking! How about you?",
                "I'm functioning perfectly! Thanks for asking.",
                "All systems are operational! How can I help?",
                "I'm doing well! What can I assist you with?"
            ],
            
            # Time queries
            '(what time is it|tell me the time|current time|what\'s the time)': [
                self.get_current_time
            ],
            
            # Date queries
            '(what date is it|tell me the date|current date|what\'s the date|what day is it)': [
                self.get_current_date
            ],
            
            # Weather queries
            '(what\'s the weather|weather forecast|how\'s the weather|is it raining|will it rain)': [
                self.get_weather_response
            ],
            
            # Name
            '(what\'s your name|who are you|tell me your name)': [
                "I'm your friendly AI Chatbot Assistant!",
                "I'm ChatBot, your helpful AI assistant!",
                "You can call me ChatBot, your AI companion!",
                "I'm an AI Assistant here to help you!"
            ],
            
            # Creator
            '(who created you|who built you|who made you)': [
                "I was created by a talented developer!",
                "I was built with Python and love!",
                "I'm a creation of modern AI technology!",
                "I was developed to assist and help people!"
            ],
            
            # Capabilities
            '(what can you do|what are you capable of|your abilities|your features)': [
                "I can answer questions about time, date, weather, and much more! Try asking me anything.",
                "I can tell you the current time and date, provide weather info, and chat with you!",
                "I'm capable of answering basic questions, providing information, and having friendly conversations!",
                "Ask me about time, dates, weather, or just chat with me!"
            ],
            
            # Help
            '(help|can you help me|i need help|help me)': [
                "Of course! I'm here to help. Ask me about time, weather, or just chat with me!",
                "Sure! I can help you with various tasks. What do you need?",
                "I'd be happy to help! What do you need assistance with?",
                "Absolutely! Feel free to ask me anything!"
            ],
            
            # Thanks
            '(thanks|thank you|appreciate it|thanks a lot)': [
                "You're welcome! Happy to help!",
                "My pleasure! Anything else I can do?",
                "Glad I could help! Feel free to ask me anything.",
                "Anytime! That's what I'm here for!"
            ],
            
            # Goodbye
            '(bye|goodbye|see you|farewell|exit|quit)': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Farewell! Hope to chat again soon!",
                "Bye! Thanks for chatting with me!"
            ],
            
            # Age
            '(how old are you|what\'s your age|your age)': [
                "I'm timeless! I exist in the digital realm!",
                "Age is just a number, and I don't have one!",
                "I'm as young as the latest update!",
                "I'm ageless - I'm an AI!"
            ],
            
            # Joke
            '(tell me a joke|make me laugh|funny|joke)': [
                self.get_joke
            ],
            
            # Math operations
            '(what is|calculate|what\'s) (\d+) (\+|\-|\*|/) (\d+)': [
                self.calculate
            ],
        }
    
    def get_current_time(self):
        """Get current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    def get_current_date(self):
        """Get current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}"
    
    def get_weather_response(self):
        """Get weather response (simulated)"""
        weather_responses = [
            "It's a beautiful sunny day! 🌞",
            "It looks cloudy today! ☁️",
            "Looks like rain might be coming... 🌧️",
            "It's a perfect day outside! 😊",
            "The weather forecast shows clear skies! 🌤️",
            "It's quite nice out there!",
            "I see clear weather ahead! ✨"
        ]
        return random.choice(weather_responses)
    
    def get_joke(self):
        """Get a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why did the coffee file a police report? It got mugged!"
        ]
        return random.choice(jokes)
    
    def calculate(self, expression):
        """Perform basic calculations"""
        try:
            result = eval(expression)
            return f"The answer is: {result}"
        except:
            return "I couldn't calculate that. Please try again."
    
    def extract_math(self, user_input):
        """Extract math expression from input"""
        pattern = r'(\d+)\s*([\+\-\*/])\s*(\d+)'
        match = re.search(pattern, user_input)
        if match:
            num1, op, num2 = match.groups()
            expression = f"{num1}{op}{num2}"
            return self.calculate(expression)
        return None
    
    def match_pattern(self, user_input):
        """Match user input against defined patterns"""
        user_input_lower = user_input.lower()
        
        # First check for math expressions
        math_result = self.extract_math(user_input_lower)
        if math_result:
            return math_result
        
        # Check against defined rules
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input_lower):
                response = random.choice(responses)
                # If response is callable, call it
                if callable(response):
                    return response()
                return response
        
        # Default response if no pattern matches
        default_responses = [
            "That's interesting! Can you elaborate on that?",
            "I'm not sure about that, but I'm here to help with time, weather, and general chat!",
            "Hmm, interesting question! Try asking me about time, weather, or something else!",
            "I don't have information about that, but feel free to ask me anything else!",
            "That's quite a query! What else can I help you with?",
            "I'm still learning! Ask me about time, date, or weather for better results!"
        ]
        return random.choice(default_responses)
    
    def create_widgets(self):
        """Create GUI widgets"""
        # Title
        title_label = tk.Label(
            self.root,
            text="AI Chatbot Assistant",
            font=("Arial", 20, "bold"),
            bg="#1e1e1e",
            fg="#00d4ff"
        )
        title_label.pack(pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Rule-Based Response System",
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="#888888"
        )
        subtitle_label.pack(pady=5)
        
        # Chat display area
        chat_frame = tk.Frame(self.root, bg="#1e1e1e")
        chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="#2d2d2d",
            fg="#ffffff",
            height=20,
            state=tk.DISABLED,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for different message types
        self.chat_display.tag_config("user", foreground="#00d4ff", font=("Courier", 10, "bold"))
        self.chat_display.tag_config("bot", foreground="#00ff00", font=("Courier", 10, "bold"))
        self.chat_display.tag_config("timestamp", foreground="#888888", font=("Courier", 8))
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(padx=10, pady=10, fill=tk.X)
        
        # User input
        self.user_input = tk.Entry(
            input_frame,
            font=("Arial", 11),
            bg="#2d2d2d",
            fg="#ffffff",
            relief=tk.FLAT,
            insertbackground="#00d4ff",
            bd=2
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda event: self.send_message())
        
        # Send button
        send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Arial", 11, "bold"),
            command=self.send_message,
            bg="#00d4ff",
            fg="#1e1e1e",
            padx=20,
            relief=tk.FLAT,
            cursor="hand2"
        )
        send_btn.pack(side=tk.LEFT)
        
        # Button frame at bottom
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=10, pady=10, fill=tk.X)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear Chat",
            font=("Arial", 9),
            command=self.clear_chat,
            bg="#ff6b6b",
            fg="white",
            padx=15,
            relief=tk.FLAT,
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        help_btn = tk.Button(
            button_frame,
            text="Help",
            font=("Arial", 9),
            command=self.show_help,
            bg="#ffa500",
            fg="white",
            padx=15,
            relief=tk.FLAT,
            cursor="hand2"
        )
        help_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(
            button_frame,
            text="Quit",
            font=("Arial", 9),
            command=self.root.quit,
            bg="#666666",
            fg="white",
            padx=15,
            relief=tk.FLAT,
            cursor="hand2"
        )
        quit_btn.pack(side=tk.LEFT, padx=5)
        
        # Display welcome message
        self.display_welcome()
    
    def display_welcome(self):
        """Display welcome message"""
        welcome_msg = "Welcome to AI Chatbot! 🤖\nI can answer questions about time, date, weather, and more. Try asking me something!\n"
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, welcome_msg, "bot")
        self.chat_display.insert(tk.END, "-" * 60 + "\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def send_message(self):
        """Send user message and get bot response"""
        user_message = self.user_input.get().strip()
        
        if not user_message:
            return
        
        # Display user message
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
        self.chat_display.insert(tk.END, f"You: {user_message}\n", "user")
        self.chat_display.config(state=tk.DISABLED)
        
        # Get bot response
        bot_response = self.match_pattern(user_message)
        
        # Display bot response
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.chat_display.insert(tk.END, f"Bot: {bot_response}\n", "bot")
        self.chat_display.config(state=tk.DISABLED)
        
        # Scroll to bottom
        self.chat_display.see(tk.END)
        
        # Clear input field
        self.user_input.delete(0, tk.END)
        self.user_input.focus()
    
    def clear_chat(self):
        """Clear chat history"""
        if messagebox.askyesno("Confirm", "Clear all chat history?"):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete(1.0, tk.END)
            self.display_welcome()
            self.user_input.focus()
    
    def show_help(self):
        """Show help message"""
        help_text = """
CHATBOT CAPABILITIES:

✓ Greetings: Say "hello", "hi", "hey"
✓ Time: Ask "What time is it?"
✓ Date: Ask "What date is it?"
✓ Weather: Ask "How's the weather?"
✓ About Bot: Ask "Who are you?" or "What can you do?"
✓ Jokes: Ask "Tell me a joke"
✓ Math: Ask "What is 5 + 3?" or similar
✓ General Chat: Ask any question!

Just type your message and press Enter or click Send!
        """
        messagebox.showinfo("Help", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = RuleBasedChatbot(root)
    root.mainloop()
