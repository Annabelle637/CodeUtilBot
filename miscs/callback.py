#Copyright @ISmartCoder
#Updates Channel @abirxdhackz
from telethon import events, Button
from bot import CodeUtilBot
import config
from utils import LOGGER

@CodeUtilBot.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data

    if data == b"about":
        text = (
            "**ℹ️ About**\n"
            "**━━━━━━━━━━━━━━━━━**\n"
            "**Name:** Code Util ⚙️\n"
            "**Version:** v2.0 (Beta) 🛠\n\n"
            "**Development Team:**\n"
            "• Creator: [Abir Arafat Chawdhury 🇧🇩](https://t.me/ISmartCoder)\n\n"
            "**Technical Stack:**\n"
            "• Language: Python 🐍\n"
            "• Libraries: Telethon 📚\n"
            "• Database: MongoDB 🗄\n\n"
            "**About:** Automated scripy host management for Telegram bots."
        )
        buttons = [[Button.inline("◀️ Back", b"back_to_start")]]
        await event.edit(text, link_preview=False, buttons=buttons)

    elif data == b"policy":
        text = (
            "**📜 Privacy Policy for Code Util**\n\n"
            "Welcome to **Code Util** Bot. By using our services, you agree to this privacy policy.\n\n"
            "**1. Information We Collect:**\n"
            "   • **Personal Information:** User ID and username for personalization.\n"
            "   • **Usage Data:** Information on how you use the app to improve our services.\n\n"
            "**2. Usage of Information:**\n"
            "   • **Service Enhancement:** To provide and improve **Code Util.**\n"
            "   • **Communication:** Updates and new features.\n"
            "   • **Security:** To prevent unauthorized access.\n"
            "   • **Advertisements:** Display of promotions.\n\n"
            "**3. Data Security:**\n"
            "   • These tools do not store any data, ensuring your privacy.\n"
            "   • We use strong security measures, although no system is 100% secure.\n\n"
            "Thank you for using **Code Util**. We prioritize your privacy and security."
        )
        buttons = [[Button.inline("◀️ Back", b"back_to_start")]]
        await event.edit(text, link_preview=False, buttons=buttons)

    elif data == b"main_menu":
        text = (
            "**Code Util ⚙️ Bot Commands**\n\n"
            "**Basic Commands:**\n"
            "• /start - Show welcome message\n"
            "• /help  - Show this help message\n"
            "• /new   - Create New Projects\n"
            "• /logs or /mgr - View logs or manage files\n\n"
            "**Special Commands:** (Use in Bot)\n"
            "• /deploy  - Deploy a replied file from tg\n"
            "• /stop    - Stop a service hosted in server\n"
            "• /restart - Restart a service that was hosted\n"
            "• /del     - Delete a hosted project\n"
            "• /edit    - Edit Run Command Of Script\n"
            "• /ping    - See System Health....\n"
            "• /boost   - Speed up a project\n\n"
            "**Settings:** (Admin only)\n"
            "• /settings - Configure server settings\n"
            "• /admin    - Add bot admin\n"
            "• /unadmin  - Remove bot admin\n\n"
            "**Owner Commands:**\n"
            "• /reload - Restart the bot\n\n"
            "**📌 Note:** All commands work only in private chat where the bot is available."
        )
        buttons = [[Button.inline("◀️ Back", b"back_to_start")]]
        await event.edit(text, link_preview=False, buttons=buttons)

    elif data == b"back_to_start":
        sender = await event.get_sender()
        name = (sender.first_name or "User").strip()

        text = (
            f"**Hi {name}! Welcome To This Bot**\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"**CodeUtil ⚙️** is your ultimate toolkit on Telegram, packed with free hosts. Simplify your servers with ease!\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"Don't forget to [join](https://{config.UPDATE_CHANNEL_URL}) for updates!"
        )

        buttons = [
            [Button.inline("⚙ Main Menu", b"main_menu")],
            [Button.inline("ℹ️ About Me", b"about"), Button.inline("📄 Policy & Terms", b"policy")]
        ]

        await event.edit(text, link_preview=False, buttons=buttons)

    else:
        await event.answer("Unknown action", alert=False)