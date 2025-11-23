import os
import telebot
from flask import Flask
from threading import Thread

# ==========================================
# PART 1: THE "FAKE WEBSITE" (Don't touch this)
# ==========================================
app = Flask(__name__)

@app.route('/')
def home():
    return "<b>I am alive!</b>"  # This is what shows up in the browser

def run_web_server():
    # Hugging Face specifically needs port 7860
    app.run(host="0.0.0.0", port=7860)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

# ==========================================
# PART 2: YOUR BOT CODE (Edit this!)
# ==========================================

# Get the token from Hugging Face Secrets
BOT_TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(BOT_TOKEN)

# --- PASTE YOUR BOT COMMANDS BELOW THIS LINE ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am running on Hugging Face!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + message.text)

# --- END OF YOUR BOT COMMANDS ---

# ==========================================
# PART 3: START EVERYTHING
# ==========================================
if __name__ == "__main__":
    # 1. Start the fake website in the background
    keep_alive()
    
    # 2. Start the bot
    print("Bot is running...")
    bot.infinity_polling()
