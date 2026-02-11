# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Включаем базовую всю логи
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команды
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Привет! Я простой бот. Напиши что-нибудь, и я отвечу.")

async def help_cmd(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Простая помощь: напиши сообщение — я повторю его.")

async def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    await update.message.reply_text(f"Вы сказали: {text}")

def main():
    # Токен берём из переменной окружения TELEGRAM_BOT_TOKEN
    import os
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Задайте переменную окружения TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    # Ответ на любые текстовые сообщения
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
