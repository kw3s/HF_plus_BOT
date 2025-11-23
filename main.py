import os
import time
import telebot
from flask import Flask
from threading import Thread

# --- PART 1: FAKE WEBSITE ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web_server():
    app.run(host="0.0.0.0", port=7860)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

# --- PART 2: THE BOT ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "I am alive on Hugging Face!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + message.text)

# --- PART 3: EXECUTION ---
if __name__ == "__main__":
    keep_alive()
    
    # Give the network 5 seconds to wake up before connecting to Telegram
    print("Waking up network...")
    time.sleep(5) 
    
    print("Bot is polling...")
    try:
        # These parameters help prevent the 'ReadTimeout' errors common on free hosting
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"CRASH: {e}")
