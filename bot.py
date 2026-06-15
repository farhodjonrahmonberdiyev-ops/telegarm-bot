import telebot, os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(os.environ.get("TOKEN"))

doriler = {"ФЛОРАБАЛАНС 500гр":("120,000 so'm","Probiotik. Lactobacillus, Bifidobacterium, Bacillus. 500gr."),"Vaksimune AI Multi H5+H9":("770,000 so'm","Gripp vaksinasi H5+H9. 1000 doz. Inaktivat."),"Vaksimune NDL H9":("650,000 so'm","Nyukasl+H9 vaksinasi. 1000 doz. Inaktivat."),"Vaksimune ND L Multi IBPlus EDS":("400,000 so'm","Nyukasl VII genotip vaksinasi. 1000 doz."),"Vaksimune IBD MHV":("145,000 so'm","Gumboro kasalligi vaksinasi. 1000 doz. Tirik."),"VAKSIMUNE ND CLONE":("33,000 so'm","Nyukasl Clone 30. 1000 doz. Tirik."),"VAKSIMUNE ND LS":("33,000 so'm","Nyukasl LS. 1000 doz. Tirik."),"Vaksimune NDLS IB":("50,000 so'm","Nyukasl+Bronxit. 1000 doz. Tirik."),"VAKSIMUNE IBD M+":("68,000 so'm","Gumboro M+. 1000 doz. Tirik."),"Vaksimune ND L Inaktif 1000doz":("440,000 so'm","Nyukasl VII genotip. 1000 doz. Inaktivat."),"VAKSIMUNE ND BAN/AF":("85,000 so'm","Nyukasl BAN/AF. 1000 doz. Tirik."),"Vaksimune ND L Inaktif 5000doz":("550,000 so'm","Nyukasl yuqori konsentratsiya. 5000 doz."),"VAKSIMUNE IB QX":("135,000 so'm","Infeksion bronxit QX. 1000 doz. Tirik."),"VAKSIMUNE IB NV-1":("240,000 so'm","Infeksion bronxit 4/91. 2000 doz."),"VAKSIMUNE IB H120":("46,000 so'm","Infeksion bronxit H120. 1000 doz."),"Respiroflor-O 300":("850,000 so'm","Florfenikol 300mg/ml. Nafas yoli kasalliklari. 1L."),"Eksakon":("330,000 so'm","Enrofloksatsin+Kolistin. Ogiz orqali. 1L."),"Tilobag":("1,200,000 so'm","Tilozin 900,000 ME/g. Kukun. 1kg."),"Tilmikofors-O":("520,000 so'm","Tilmikozin 250mg/ml. Mikoplazma. 1L."),"Megluflor":("175,000 so'm","Florfenikol+Flunixin. Mushak osti. 100ml."),"Amoksibag":("175,000 so'm","Amoksitsillin+Klavulan kislota. 100ml."),"Fosfozal":("65,000 so'm","Butafosfan+Vitamin B12. 100ml."),"DeltaBAG 50":("300,000 so'm","Deltametrin 50mg/ml. Parazitlarga qarshi. 500ml."),"Siflubag":("180,000 so'm","Siflutrin 50mg/ml. Hasharotlarga qarshi. 1L."),"Immunair":("530,000 so'm","Immunomodulyator. Parrandalar uchun. 1L."),"HepaVital":("265,000 so'm","Jigar uchun. Niazin, Metionin, L-karnitin. 1L."),"SUPERVIT FORTE":("180,000 so'm","Vitaminlar, aminokislotalar, mikroelementlar. 1L."),"B-Complex FORTE":("210,000 so'm","B1, B2, B6, B12, H, C, Niacin, Xolin. 1L."),"E-SELEN PLUS FORTE":("160,000 so'm","Vitamin E, Selen, Biotin. 1L."),"Medquinol 10%":("TEZ KUNDA","Enrofloksatsin 10%. 1L."),"COXMED 2.5%":("TEZ KUNDA","Toltrazurin 2.5%. Koktsidioz. 1L."),"MEDICOL":("210,000 so'm","Kolistin sulfat 240mg. 1L."),"AMOXYMED 90%":("TEZ KUNDA","Amoksitsillin 720mg+Kolistin 180mg. 1L."),"AIRMENT":("220,000 so'm","Evkalipt+Yalpiz+Mentol. Nafas yoli. 1L."),"DESMED":("120,000 so'm","Dezinfektant. Benzalkoniy xlorid+Glutaraldegid. 1L."),"BROMENGIL":("TEZ KUNDA","Bromengil 20mg, Mentol 8ml. 1L."),"MEDSULTAN":("350,000 so'm","Sulfadiazin 400mg+Trimetoprim 80mg. 1L."),"AD3E+C FORTE":("260,000 so'm","Vitamin A, D3, E, C. 1L."),"SPECTRA TYLODOX 200":("TEZ KUNDA","Doksitsiklin 100mg+Tilozin 100mg. 1L."),"SPECRTIL PLUS":("TEZ KUNDA","Enrofloksatsin 200mg+Bromgeksin 20mg. 1L."),"SPECTRA HERBROM":("200,000 so'm","Bromgeksin+Timol+Evkalipt. Nafas yoli. 1L."),"VINORAL":("155,000 so'm","Vitaminlar va aminokislotalar kompleksi. 1L.")}

kategoriyalar = {"💉 Vaktsinalar":["Vaksimune AI Multi H5+H9","Vaksimune NDL H9","Vaksimune ND L Multi IBPlus EDS","Vaksimune IBD MHV","VAKSIMUNE ND CLONE","VAKSIMUNE ND LS","Vaksimune NDLS IB","VAKSIMUNE IBD M+","Vaksimune ND L Inaktif 1000doz","VAKSIMUNE ND BAN/AF","Vaksimune ND L Inaktif 5000doz","VAKSIMUNE IB QX","VAKSIMUNE IB NV-1","VAKSIMUNE IB H120"],"💊 Antibiotiklar":["Respiroflor-O 300","Eksakon","Tilobag","Tilmikofors-O","Megluflor","Amoksibag","Medquinol 10%","MEDICOL","AMOXYMED 90%","MEDSULTAN","SPECTRA TYLODOX 200","SPECRTIL PLUS"],"🌿 Vitaminlar":["ФЛОРАБАЛАНС 500гр","Fosfozal","Immunair","HepaVital","SUPERVIT FORTE","B-Complex FORTE","E-SELEN PLUS FORTE","AD3E+C FORTE","VINORAL"],"🧴 Dezinfektantlar":["DeltaBAG 50","Siflubag","AIRMENT","DESMED","BROMENGIL","SPECTRA HERBROM","COXMED 2.5%"]}

def km():
    m=InlineKeyboardMarkup()
    for k in kategoriyalar:
        m.add(InlineKeyboardButton(k,callback_data=f"k_{k}"))
    m.add(InlineKeyboardButton("🩺 Mutaxassis",callback_data="help_btn"))
    m.add(InlineKeyboardButton("🏪 Savdo bolimi",callback_data="sales_btn"))
    return m

def dm(k):
    m=InlineKeyboardMarkup()
    for d in kategoriyalar[k]:
        m.add(InlineKeyboardButton(d,callback_data=f"d_{d}"))
    m.add(InlineKeyboardButton("🔙 Orqaga",callback_data="orqaga"))
    return m

@bot.message_handler(commands=['start','list'])
def start(msg):
    bot.send_message(msg.chat.id,"Salom! 👋 RIVIERA DIAMOND\n\nKategoriyani tanlang 👇",reply_markup=km())

@bot.callback_query_handler(func=lambda c:True)
def cb(call):
    bot.answer_callback_query(call.id)
    d=call.data
    if d=="orqaga":
        bot.send_message(call.message.chat.id,"Kategoriyani tanlang 👇",reply_markup=km())
    elif d=="help_btn":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("📞 Ergashev Akbarjon",url="tel:+998916223520"))
        m.add(InlineKeyboardButton("📞 Axmadaliyev Nurmuhammad",url="tel:+998999449803"))
        m.add(InlineKeyboardButton("📞 Xomitjonov Ulugbek",url="tel:+998932466069"))
        bot.send_message(call.message.chat.id,"🩺 Veterinar mutaxassislar:",reply_markup=m)
    elif d=="sales_btn":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("📞 +998 90 932 97 71",url="tel:+998909329771"))
        m.add(InlineKeyboardButton("📞 +998 95 390 39 36",url="tel:+998953903936"))
        bot.send_message(call.message.chat.id,"🏪 Savdo bolimi\n📍 Toshkent, Choshtеpa 38/40",reply_markup=m)
    elif d.startswith("k_"):
        k=d[2:]
        bot.send_message(call.message.chat.id,f"{k}:",reply_markup=dm(k))
    elif d.startswith("d_"):
        n=d[2:]
        info=doriler.get(n,("?",""))
        bot.send_message(call.message.chat.id,f"💊 {n}\n📋 {info[1]}\n💰 Narx: {info[0]}")

bot.infinity_polling()
