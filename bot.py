"👨‍⚕️ Axmadaliyev Nurmuhammad: +998 99 944 98 03\n"
        "👨‍⚕ Xomitjonov Ulug'bek: +998 93 246 60 69",
        reply_markup=markup)

@bot.message_handler(commands=['sales'])
def sales(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📞 +998 90 932 97 71", url="tel:+998909329771"))
    markup.add(InlineKeyboardButton("📞 +998 95 390 39 36", url="tel:+998953903936"))
    bot.send_message(message.chat.id,
        "🏪 Rasmiy Distribyuter — SAVDO BO'LIMI\n\n"
        "📞 +998 90 932 97 71\n"
        "📞 +998 95 390 39 36\n"
        "📍 Toshkent, Choshtеpa ko'chasi, 38/40",
        reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    if call.data == "orqaga":
        bot.send_message(call.message.chat.id, "Kategoriyani tanlang 👇", reply_markup=kategoriya_menyu())
    elif call.data.startswith("kat_"):
        kat = call.data[4:]
        bot.send_message(call.message.chat.id, f"{kat} — dori tanlang 👇", reply_markup=dori_menyu(kat))
    elif call.data.startswith("dori_"):
        dori = call.data[5:]
        narx = doriler.get(dori, "Noma'lum")
        bot.send_message(call.message.chat.id, f"💊 {dori}\n💰 Narx: {narx}")

bot.infinity_polling()
