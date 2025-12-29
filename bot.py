from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler


BOT_TOKEN = "7980961451:AAGVXXZWlYs8I5Bht101KDazP2c7XZbxeHI"


async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user_chat_id = join_request.user_chat_id
    first_name = join_request.from_user.first_name or "there"

    # Message sent BEFORE approval
    await context.bot.send_message(
        chat_id=user_chat_id,
        text=(
            f"Hi {first_name}! 👋\n\n"
            "Thanks for requesting to join.\n"
            "Before we approve your request, could you please reply with:\n\n"
            "1️⃣ Your full name \n"
            "2️⃣ Your email address \n"
            "This information will solely be used for verification purposes. Thank you!"
        )
    )

async def handler(req):
    """Vercel handler"""
    data = await req.json()
    update = Update.de_json(data, Bot(BOT_TOKEN))
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))

    # process the single update
    await app.process_update(update)

    return {"status": "ok"}
