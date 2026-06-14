import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(os.environ.get("TOKEN"))

doriler = {
    "ФЛОРАБАЛАНС 500гр": "120,000 so'm",
    "Vaksimune AI Multi H5+H9": "770,000 so'm",
    "Vaksimune NDL H9": "650,000 so'm",
    "Vaksimune ND L Multi IBPlus EDS": "400,000 so'm",
    "Vaksimune IBD MHV": "145,000 so'm",
    "VAKSIMUNE ND CLONE": "33,000 so'm",
    "VAKSIMUNE ND LS": "33,000 so'm",
    "Vaksimune NDLS IB": "50,000 so'm",
    "VAKSIMUNE IBD M+": "68,000 so'm",
    "Vaksimune ND L Inaktif 1000doz": "440,000 so'm",
    "VAKSIMUNE ND BAN/AF": "85,000 so'm",
    "Vaksimune ND L Inaktif 5000doz": "550,000 so'm",
    "VAKSIMUNE IB QX": "135,000 so'm",
    "VAKSIMUNE IB NV-1": "240,000 so'm",
    "VAKSIMUNE IB H120": "46,000 so'm",
    "Respiroflor-O 300": "850,000 so'm",
    "Eksakon": "330,000 so'm",
    "Tilobag": "1,200,000 so'm",
    "Tilmikofors-O": "520,000 so'm",
    "Megluflor": "175,000 so'm",
    "Amoksibag": "175,000 so'm",
    "Fosfozal": "65,000 so'm",
    "DeltaBAG 50": "300,000 so'm",
    "Siflubag": "180,000 so'm",
    "Immunair": "530,000 so'm",
    "HepaVital": "265,000 so'm",
    "SUPERVIT FORTE": "180,000 so'm",
    "B-Complex FORTE": "210,000 so'm",
    "E-SELEN PLUS FORTE": "160,000 so'm",
    "Medquinol 10%": "TEZ KUNDA",
    "COXMED 2.5%": "TEZ KUNDA",
    "MEDICOL": "210,000 so'm",
    "AMOXYMED 90%": "TEZ KUNDA",
    "AIRMENT": "220,000 so'm",
    "DESMED": "120,000 so'm",
    "BROMENGIL": "TEZ KUNDA",
    "MEDSULTAN": "350,000 so'm",
    "AD3E+C FORTE": "260,000 so'm",
    "SPECTRA TYLODOX 200": "TEZ KUNDA",
    "SPECRTIL PLUS": "TEZ KUNDA",
    "SPECTRA HERBROM": "200,000 so'm",
    "VINORAL": "155,000 so'm",
}

kategoriyalar = {
    "💉 Vaktsinalar": ["Vaksimune AI Multi H5+H9","Vaksimune NDL H9","Vaksimune ND L Multi IBPlus EDS","Vaksimune IBD MHV","VAKSIMUNE ND CLONE","VAKSIMUNE ND LS","Vaksimune NDLS IB","VAKSIMUNE IBD M+","Vaksimune ND L Inaktif 1000doz","VAKSIMUNE ND BAN/AF","Vaksimune ND L Inaktif 5000doz","VAKSIMUNE IB QX","VAKSIMUNE IB NV-1","VAKSIMUNE IB H120"],
    "💊 Antibiotiklar": ["Respiroflor-O 300","Eksakon","Tilobag","Tilmikofors-O","Megluflor","Amoksibag","Medquinol 10%","MEDICOL","AMOXYMED 90%","MEDSULTAN","SPECTRA TYLODOX 200","SPECRTIL PLUS"],
    "🌿 Vitaminlar": ["ФЛОРАБАЛАНС 500гр","Fosfozal","Immunair","HepaVital","SUPERVIT FORTE","B-Complex FORTE","E-SELEN PLUS FORTE","AD3E+C FORTE","VINORAL"],
    "🧴 Dezinfektantlar": ["DeltaBAG 50","Siflubag","AIRMENT","DESMED","BROMENGIL","SPECTRA HERBROM","COXMED 2.5%"],
}

def kategoriya_menyu():
    markup = InlineKeyboardMarkup()
    for kat in kategoriyalar:
        markup.add(InlineKeyboardButton(kat, callback_data=f"kat_{kat}"))
    markup.add(InlineKeyboardButton("🩺 Mutaxassis", callback_data="help"))
    markup.add(InlineKeyboardButton("🏪 Savdo bo'limi", callback_data="sales"))
    return markup

def dori_menyu(kat):
    markup = InlineKeyboardMarkup()
    for dori in kategoriyalar[kat]:
        markup.add(InlineKeyboardButton(dori, callback_data=f"dori_{dori}"))
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 👋 RIVIERA DIAMOND ga xush kelibsiz!\n\nKategoriyani tanlang 👇", reply_markup=kategoriya_menyu())

@bot.message_handler(commands=['list'])
def dori_list(message):
    bot.send_message(message.chat.id, "Kategoriyani tanlang 👇", reply_markup=kategoriya_menyu())

@bot.message_handler(commands=['help'])
def help_cmd(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📞 Ergashev Akbarjon", url="tel:+998916223520"))
    markup.add(InlineKeyboardButton("📞 Axmadaliyev Nurmuhammad", url="tel:+998999449803"))
    markup.add(InlineKeyboardButton("📞 Xomitjonov Ulugbek", url="tel:+998932466069"))
    bot.send_message(message.chat.id, "🩺 Veterinar mutaxassislar:\n\n👨‍⚕️ Ergashev Akbarjon: +998 91 622 35 20\n👨‍⚕️ Axmadaliyev Nurmuhammad: +998 99 944 98 03\n👨‍⚕️ Xomitjonov Ulugbek: +998 93 246 60 69", reply_markup=markup)

@bot.message_handler(commands=['sales'])
def sales(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📞 +998 90 932 97 71", url="tel:+998909329771"))
    markup.add(InlineKeyboardButton("📞 +998 95 390 39 36", url="tel:+998953903936"))
    bot.send_message(message.chat.id, "🏪 Rasmiy Distribyuter - SAVDO BO'LIMI\n\n📞 +998 90 932 97 71\n📞 +998 95 390 39 36\n📍 Toshkent, Choshtеpa ko'chasi, 38/40", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    if call.data == "orqaga":
        bot.send_message(call.message.chat.id, "Kategoriyani tanlang 👇", reply_markup=kategoriya_menyu())
    elif call.data.startswith("kat_"):
        kat = call.data[4:]
        bot.send_message(call.message.chat.id, f"{kat} - dori tanlang 👇", reply_markup=dori_menyu(kat))
    elif call.data.startswith("dori_"):
        dori = call.data[5:]
        narx = doriler.get(dori, "Noma'lum")
        bot.send_message(call.message.chat.id, f"💊 {dori}\n💰 Narx: {narx}")
    elif call.data == "help":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📞 Ergashev Akbarjon", url="tel:+998916223520"))
        markup.add(InlineKeyboardButton("📞 Axmadaliyev Nurmuhammad", url="tel:+998999449803"))
        markup.add(InlineKeyboardButton("📞 Xomitjonov Ulugbek", url="tel:+998932466069"))
        bot.send_message(call.message.chat.id, "🩺 Veterinar mutaxassislar:", reply_markup=markup)
    elif call.data == "sales":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📞 +998 90 932 97 71", url="tel:+998909329771"))
        markup.add(InlineKeyboardButton("📞 +998 95 390 39 36", url="tel:+998953903936"))
        bot.send_message(call.message.chat.id, "🏪 Rasmiy Distribyuter - SAVDO BO'LIMI\n\n📞 +998 90 932 97 71\n📞 +998 95 390 39 36\n📍 Toshkent, Choshtеpa ko'chasi, 38/40", reply_markup=markup)

bot.infinity_polling()
