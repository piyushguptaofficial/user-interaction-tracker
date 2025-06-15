import logging
logging.basicConfig(level=logging.DEBUG)
import os
import django
from telegram.ext import Application, CommandHandler
from decouple import Config, RepositoryEnv

# Set up Django environment so we can use its models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import TelegramUser

#load .env manually for standalone scripts
env_path = os.path.join(os.path.dirname(__file__), '.env')
config = Config(repository = RepositoryEnv(env_path))
# print("Looking for .env at:", env_path)
# print("File exists:", os.path.exists(env_path))
BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")




# Define the command handler for /start


# async def start(update, context):
#     user = update.effective_user

#     TelegramUser.objects.get_or_create(
#         chat_id=user.id,
#         defaults={
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name
#         }
#     )

    # await update.message.reply_text(f"Hi {user.first_name or user.username}, you are now registered with our Django app!")
    
# Define the command handler for /start
from asgiref.sync import sync_to_async

@sync_to_async
def save_telegram_user(user):
    TelegramUser.objects.get_or_create(
        chat_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    )

async def start(update, context):
    user=update.effective_user
    await save_telegram_user(user)
    await update.message.reply_text(f"Hi {user.first_name or user.username}, you are now registered with our Django app!"
    )                               


# /help COMMAND
async def help_command(update, context):
    message=(
        "🤖Available commands:\n"
        "/start - Register YourSelf\n"
        "/help - Just Google, You will get the answer\n"
        "/profile - View Your Profile\n"
        "/dashboard - View protected dashboard (demo)" 
    )
    await update.message.reply_text(message, parse_mode="Markdown")


# /profile COMMAND
@sync_to_async
def get_user_info(chat_id):
    return TelegramUser.objects,filter(chat_id=chat_id).first()

async def profile_command(update, context):
    user = await get_user_info(update.effective_user.id)
    if user:
        msg = (
            f"🤣 Username:{user.username}\n"
            f"😶‍🌫️ First Name: {user.first_name}\n"
            f"Last Name: {user.last_name}\n"
        )
    else:
        msg = "👊 You are not registered yet!. Use /start to get yourself registered."
    await update.message.reply_text(msg)
    

# /dashboard COMMAND (mock data)
async def dashboard_command(update, context):
    await update.message.reply_text("🦺 WELCOME TO YOUR DASHBOARD! (This is a demo response)")



# Start polling (listening for messages)
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("profile", profile_command))
    app.add_handler(CommandHandler("dashboard", dashboard_command))
    print("Running polling loop now...")
    app.run_polling()

if __name__ == '__main__':
    print("Starting the bot...")
    main()