import telebot
from telebot import types

# 🔑 توکن رباتت از BotFather
TOKEN = "توکن_ربات_خودت"
bot = telebot.TeleBot(TOKEN)

# 📌 دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📖 راهنما")
    btn2 = types.KeyboardButton("ℹ️ درباره من")
    btn3 = types.KeyboardButton("👋 سلام")
    markup.add(btn1, btn2, btn3)

    text = (
        "سلام 👋\n"
        "به ربات پیشرفته من خوش اومدی 😎\n"
        "از منو پایین یکی رو انتخاب کن یا دستور /help رو بزن."
    )
    bot.reply_to(message, text, reply_markup=markup)

# 📌 دستور /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
        "📌 لیست امکانات:\n"
        "/start - شروع دوباره\n"
        "/help - راهنما\n"
        "/about - درباره ربات\n"
        "همچنین می‌تونی هر متنی بفرستی!"
    )

# 📌 دستور /about
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message,
        "🤖 من یک ربات تلگرام هستم که با پایتون ساخته شدم.\n"
        "روی سرور ۲۴ ساعته اجرا میشم 🚀"
    )

# 📌 جواب به متن‌های عادی
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text.lower()

    if "سلام" in text:
        reply = "سلام کاربر عزیز! 🙂"
    elif "خوبی" in text or "حالت چطوره" in text:
        reply = "مرسی! من خوبم، تو چطوری؟ 🤝"
    elif "درباره" in text:
        reply = "من یه ربات تلگرام هستم ساخته شده با پایتون 🤖"
    elif "راهنما" in text:
        reply = "کافیه دستور /help رو بزنی 📖"
    else:
        reply = f"تو نوشتی: {message.text}"

    bot.reply_to(message, reply)

print("✅ ربات روشن شد و آماده پاسخگویی است.")
bot.infinity_polling()