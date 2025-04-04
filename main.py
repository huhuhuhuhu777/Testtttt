from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Lấy token từ biến môi trường
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Xin chào! Tôi đang chạy trên Koyeb!")

# Trả lời lại bất kỳ tin nhắn nào
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn gửi: {update.message.text}")

# Hàm chính
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("🤖 Bot đang chạy trên Koyeb...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
