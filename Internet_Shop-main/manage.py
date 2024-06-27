import project, telegram_bot

if __name__ == "__main__":
    telegram_bot.bot.infinity_polling()
    project.shop.run(debug = True)