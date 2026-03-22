from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
from telegram import Update
from config import BOT_TOKEN


async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user= update.message.from_user
    nome_user=user.username
    await update.message.reply_text(f"Olá, {nome_user}!"
                                    "\n /start- iniciar o bot" \
                                    "\n /info -ver informações do bot")


async def info(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot criado com Python")

app= ApplicationBuilder().token("BOT_TOKEN").build()

print("Bot rodando!")
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("info",info))
app.run_polling()