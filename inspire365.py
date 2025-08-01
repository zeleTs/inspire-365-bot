import os
import telebot
import random

# === Bot Setup ===
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# === Sample English Quotes ===
quotes = [
    "Believe you can and you're halfway there.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Start where you are. Use what you have. Do what you can.",
    "Great things never come from comfort zones."
]

# === /start ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌟 Welcome to Inspire365!\nType /motivate to receive your daily dose of motivation.")

# === /motivate ===
@bot.message_handler(commands=['motivate'])
def send_motivation(message):
    quote = random.choice(quotes)
    bot.send_message(message.chat.id, f"💬 *{quote}*", parse_mode="Markdown")

# === Fallback ===
@bot.message_handler(func=lambda m: True)
def handle_unknown(message):
    bot.reply_to(message, "❓ Try /motivate or /start")

# === Start polling ===
print("Inspire365 is running...")
bot.infinity_polling()
