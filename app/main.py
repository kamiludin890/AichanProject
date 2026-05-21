from app.telegram_bot import app


if __name__ == "__main__":
    print("Starting AichanProject...")
    app.run_polling()