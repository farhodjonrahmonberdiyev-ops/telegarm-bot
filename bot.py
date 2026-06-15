import telebot,os
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
bot=telebot.TeleBot(os.environ.get("TOKEN"))
doriler={"FLORABALANS 500gr":("120,000 som","Probiotik. Lactobacillus, Bifidobacterium, Bacillus. 500gr."),"Vaksimune AI Multi H5+H9":("770,000 som","Gripp vaksinasi H5+H9. 1000 doz. Inaktivat."),"Vaksimune NDL H9":("650,000 som","Nyukasl+H9 vaksinasi. 1000 doz. Inaktivat."),"Vaksimune ND L Multi IBPlus EDS":("400,000 som","Nyukasl VII genotip. 1000 doz."),"Vaksimune IBD MHV":("145,000 som","Gumboro vaksinasi. 1000 doz. Tirik."),"VAKSIMUNE ND CLONE":("33,000 som","Nyukasl Clone 30. 1000 doz. Tirik."),"VAKSIMUNE ND LS":("33,000 som","Nyukasl LS. 1000 doz. Tirik."),"Vaksimune NDLS IB":("50,000 som","Nyukasl+Bronxit. 1000 doz. Tirik."),"VAKSIMUNE IBD M+":("68,000 som","Gumboro M+. 1000 doz. Tirik."),"Vaksimune ND L Inaktif 1000doz":("440,000 som","Nyukasl VII genotip. 1000 doz. Inaktivat."),"VAKSIMUNE ND BAN":("85,000 som","Nyukasl BAN/AF. 1000 doz. Tirik."),"Vaksimune ND L Inaktif 5000doz":("550,000 som","Nyukasl yuqori konsentratsiya. 5000 doz."),"VAKSIMUNE IB QX":("135,000 som","Infeksion bronxit QX. 1000 doz."),"VAKSIMUNE IB NV1":("240,000 som","Infeksion bronxit 4/91. 2000 doz."),"VAKSIMUNE IB H120":("46,000 som","Infeksion bronxit H120. 1000 doz."),"Respiroflor 300":("850,000 som","Florfenikol 300mg/ml. 1L."),"Eksakon":("330,000 som","Enrofloksatsin+Kolistin. 1L."),"Tilobag":("1,200,000 som","Tilozin 900,000 ME/g. 1kg."),"Tilmikofors":("520,000 som","Tilmikozin 250mg/ml. 1L."),"Megluflor":("175,000 som","Florfenikol+Flunixin. 100ml."),"Amoksibag":("175,000 som","Amoksitsillin+Klavulan kislota. 100ml."),"Fosfozal":("65,000 som","Butafosfan+Vitamin B12. 100ml."),"DeltaBAG 50":("300,000 som","Deltametrin 50mg. Parazitlarga qarshi. 500ml."),"Siflubag":("180,000 som","Siflutrin 50mg. Hasharotlarga qarshi. 1L."),"Immunair":("530,000 som","Immunomodulyator. 1L."),"HepaVital":("265,000 som","Jigar uchun. Niazin, Metionin. 1L."),"SUPERVIT FORTE":("180,000 som","Vitaminlar kompleksi. 1L."),"BComplex FORTE":("210,000 som","B1,B2,B6,B12,H,C,Niacin. 1L."),"ESELEN PLUS FORTE":("160,000 som","Vitamin E, Selen, Biotin. 1L."),"Medquinol 10":("TEZ KUNDA","Enrofloksatsin 10%. 1L."),"COXMED 25":("TEZ KUNDA","Toltrazurin 2.5%. 1L."),"MEDICOL":("210,000 som","Kolistin sulfat 240mg. 1L."),"AMOXYMED 90":("TEZ KUNDA","Amoksitsillin+Kolistin. 1L."),"AIRMENT":("220,000 som","Evkalipt+Yalpiz+Mentol. 1L."),"DESMED":("120,000 som","Dezinfektant. Benzalkoniy+Glutaraldegid. 1L."),"BROMENGIL":("TEZ KUNDA","Bromengil 20mg, Mentol 8ml. 1L."),"MEDSULTAN":("350,000 som","Sulfadiazin+Trimetoprim. 1L."),"AD3EC FORTE":("260,000 som","Vitamin A,D3,E,C. 1L."),"SPECTRA TYLODOX":("TEZ KUNDA","Doksitsiklin+Tilozin. 1L."),"SPECRTIL PLUS":("TEZ KUNDA","Enrofloksatsin+Bromgeksin. 1L."),"SPECTRA HERBROM":("200,000 som","Bromgeksin+Timol+Evkalipt. 1L."),"VINORAL":("155,000 som","Vitaminlar va aminokislotalar. 1L.")}
vak=["Vaksimune AI Multi H5+H9","Vaksimune NDL H9","Vaksimune ND L Multi IBPlus EDS","Vaksimune IBD MHV","VAKSIMUNE ND CLONE","VAKSIMUNE ND LS","Vaksimune NDLS IB","VAKSIMUNE IBD M+","Vaksimune ND L Inaktif 1000doz","VAKSIMUNE ND BAN","Vaksimune ND L Inaktif 5000doz","VAKSIMUNE IB QX","VAKSIMUNE IB NV1","VAKSIMUNE IB H120"]
ant=["Respiroflor 300","Eksakon","Tilobag","Tilmikofors","Megluflor","Amoksibag","Medquinol 10","MEDICOL","AMOXYMED 90","MEDSULTAN","SPECTRA TYLODOX","SPECRTIL PLUS"]
vit=["FLORABALANS 500gr","Fosfozal","Immunair","HepaVital","SUPERVIT FORTE","BComplex FORTE","ESELEN PLUS FORTE","AD3EC FORTE","VINORAL"]
dez=["DeltaBAG 50","Siflubag","AIRMENT","DESMED","BROMENGIL","SPECTRA HERBROM","COXMED 25"]
def km():
    m=InlineKeyboardMarkup()
    m.add(InlineKeyboardButton("💉 Vaktsinalar",callback_data="VAK"))
    m.add(InlineKeyboardButton("💊 Antibiotiklar",callback_data="ANT"))
    m.add(InlineKeyboardButton("🌿 Vitaminlar",callback_data="VIT"))
    m.add(InlineKeyboardButton("🧴 Dezinfektantlar",callback_data="DEZ"))
    m.add(InlineKeyboardButton("Mutaxassis",callback_data="HELP"))
    m.add(InlineKeyboardButton("Savdo bolimi",callback_data="SALES"))
    return m
def dm(lst):
    m=InlineKeyboardMarkup()
    for d in lst:
        m.add(InlineKeyboardButton(d,callback_data=f"D{d[:30]}"))
    m.add(InlineKeyboardButton("🔙 Orqaga",callback_data="BACK"))
    return m
@bot.message_handler(commands=['start','list'])
def start(msg):
    bot.send_message(msg.chat.id,"Salom! RIVIERA DIAMOND\n\nKategoriyani tanlang:",reply_markup=km())
@bot.callback_query_handler(func=lambda c:True)
def cb(call):
    bot.answer_callback_query(call.id)
    d=call.data
    if d=="BACK":
        bot.send_message(call.message.chat.id,"Kategoriyani tanlang:",reply_markup=km())
    elif d=="HELP":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("Ergashev Akbarjon",url="tel:+998916223520"))
        m.add(InlineKeyboardButton("Axmadaliyev Nurmuhammad",url="tel:+998999449803"))
        m.add(InlineKeyboardButton("Xomitjonov Ulugbek",url="tel:+998932466069"))
        bot.send_message(call.message.chat.id,"Veterinar mutaxassislar:",reply_markup=m)
    elif d=="SALES":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("+998 90 932 97 71",url="tel:+998909329771"))
        m.add(InlineKeyboardButton("+998 95 390 39 36",url="tel:+998953903936"))
        bot.send_message(call.message.chat.id,"Savdo bolimi\nToshkent, Choshtеpa 38/40",reply_markup=m)
    elif d=="VAK":
        bot.send_message(call.message.chat.id,"Vaktsinalar:",reply_markup=dm(vak))
    elif d=="ANT":
        bot.send_message(call.message.chat.id,"Antibiotiklar:",reply_markup=dm(ant))
    elif d=="VIT":
        bot.send_message(call.message.chat.id,"Vitaminlar:",reply_markup=dm(vit))
    elif d=="DEZ":
        bot.send_message(call.message.chat.id,"Dezinfektantlar:",reply_markup=dm(dez))
    elif d.startswith("D"):
        n=d[1:]
        for k,v in doriler.items():
            if k.startswith(n):
                bot.send_message(call.message.chat.id,f"{k}\n{v[1]}\nNarx: {v[0]}")
                return
bot.infinity_polling()
