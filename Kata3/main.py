from telegram.ext import Updater, CommandHandler

def main():

# open("./bot_token").read()
    # instanciar updater
    updater = Updater(token="", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # new handler
    updater.dispatcher.add_handler(CommandHandler("repeat", repeat))
    updater.dispatcher.add_handler(CommandHandler("add", addition))
    
    # start asking telegram for notifications
    updater.start_polling()

    # get stop signals
    updater.idle()


def start(update, context):
    
    update.message.reply_text("Hello, I'm a bot!")
    pass

def repeat(update, context):
    update.message.reply_text(update.message.text)

def addition(update, context):
    res = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("Result is: " + str(res))

main()