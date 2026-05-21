from telegram import Update
from telegram.ext import ApplicationBuilder
from telegram.ext import MessageHandler
from telegram.ext import ContextTypes
from telegram.ext import filters
from telegram.ext import CommandHandler

from app.ollama_client import ask_ollama
from app.personalities import load_personality
from app.tts import generate_voice
from app.memory import save_memory, get_memory
from app.config import BOT_TOKEN

personality_mode = "waifu"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aichan online~")


async def set_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global personality_mode

    if len(context.args) == 0:
        await update.message.reply_text("Contoh: /mode waifu")
        return

    personality_mode = context.args[0]

    await update.message.reply_text(
        f"Mode diganti ke {personality_mode}"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.message.from_user.id

    memory = get_memory(user_id)
    personality = load_personality(personality_mode)

    full_prompt = f"""{personality}

Riwayat:
{memory}

User: {user_text}
Aichan:
"""

    await update.message.reply_text(
        "Aku mikir dulu ya~"
    )

    response = ask_ollama(full_prompt)
    response = response[:150]

    save_memory(user_id, f"User: {user_text}")
    save_memory(user_id, f"Aichan: {response}")

    await update.message.reply_text(response)

    try:
        speak_text = response

        if "Romaji:" in response:
            speak_text = response.split("Romaji:")[0]

        if "日本語:" in speak_text:
            speak_text = speak_text.replace(
                "日本語:",
                ""
            ).strip()

        audio = generate_voice(speak_text)

        with open(audio, "rb") as voice:
            await update.message.reply_voice(
                voice=voice
            )

    except Exception as e:
        print("TTS ERROR:")
        print(e)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("mode", set_mode))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)


if __name__ == "__main__":
    print("Aichan running...")
    app.run_polling()