from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BASE_URL = "https://arbada.b-cdn.net/contents/videos/4000/{id}/{id}_360p.mp4"

current_id = 4000  # البداية

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ابعت /get 10 عشان اديك 10 روابط")

async def get_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_id

    try:
        count = int(context.args[0])
    except:
        await update.message.reply_text("استخدم: /get 10")
        return

    links = []

    for _ in range(count):
        link = BASE_URL.format(id=current_id)
        links.append(link)
        current_id += 1

    await update.message.reply_text("\n".join(links))


app = ApplicationBuilder().token("8698486397:AAHgSSRbGizdMXWUvrHqrIPzVICPGuYagwo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("get", get_links))

app.run_polling()
