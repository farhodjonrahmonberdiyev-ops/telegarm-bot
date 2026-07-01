import telebot,os
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
bot=telebot.TeleBot(os.environ.get("TOKEN"))
doriler={"FLORABALANS 500gr":"Probiotik. Lactobacillus, Bifidobacterium, Bacillus. 500gr.","Vaksimune AI Multi H5+H9":"Gripp vaksinasi H5+H9. 1000 doz. Inaktivat.","Vaksimune NDL H9":"Nyukasl+H9 vaksinasi. 1000 doz. Inaktivat.","Vaksimune ND L Multi IBPlus EDS":"Nyukasl VII genotip. 1000 doz.","Vaksimune IBD MHV":"Gumboro vaksinasi. 1000 doz. Tirik.","VAKSIMUNE ND CLONE":"Nyukasl Clone 30. 1000 doz. Tirik.","VAKSIMUNE ND LS":"Nyukasl LS. 1000 doz. Tirik.","Vaksimune NDLS IB":"Nyukasl+Bronxit. 1000 doz. Tirik.","VAKSIMUNE IBD M+":"Gumboro M+. 1000 doz. Tirik.","Vaksimune ND L Inaktif 1000doz":"Nyukasl VII genotip. 1000 doz. Inaktivat.","VAKSIMUNE ND BAN":"Nyukasl BAN/AF. 1000 doz. Tirik.","Vaksimune ND L Inaktif 5000doz":"Nyukasl yuqori konsentratsiya. 5000 doz.","VAKSIMUNE IB QX":"Infeksion bronxit QX. 1000 doz.","VAKSIMUNE IB NV1":"Infeksion bronxit 4/91. 2000 doz.","VAKSIMUNE IB H120":"Infeksion bronxit H120. 1000 doz.","Respiroflor 300":"Florfenikol 300mg/ml. 1L.","Eksakon":"Enrofloksatsin+Kolistin. 1L.","Tilobag":"Tilozin 900,000 ME/g. 1kg.","Tilmikofors":"Tilmikozin 250mg/ml. 1L.","Megluflor":"Florfenikol+Flunixin. 100ml.","Amoksibag":"Amoksitsillin+Klavulan kislota. 100ml.","Fosfozal":"Butafosfan+Vitamin B12. 100ml.","DeltaBAG 50":"Deltametrin 50mg. Parazitlarga qarshi. 500ml.","Siflubag":"Siflutrin 50mg. Hasharotlarga qarshi. 1L.","Immunair":"Immunomodulyator. 1L.","HepaVital":"Jigar uchun. Niazin, Metionin. 1L.","SUPERVIT FORTE":"Vitaminlar kompleksi. 1L.","BComplex FORTE":"B1,B2,B6,B12,H,C,Niacin. 1L.","ESELEN PLUS FORTE":"Vitamin E, Selen, Biotin. 1L.","Medquinol 10":"Enrofloksatsin 10%. 1L.","COXMED 25":"Toltrazurin 2.5%. 1L.","MEDICOL":"Kolistin sulfat 240mg. 1L.","AMOXYMED 90":"Amoksitsillin+Kolistin. 1L.","AIRMENT":"Evkalipt+Yalpiz+Mentol. 1L.","DESMED":"Dezinfektant. Benzalkoniy+Glutaraldegid. 1L.","BROMENGIL":"Bromengil 20mg, Mentol 8ml. 1L.","MEDSULTAN":"Sulfadiazin+Trimetoprim. 1L.","AD3EC FORTE":"Vitamin A,D3,E,C. 1L.","SPECTRA TYLODOX":"Doksitsiklin+Tilozin. 1L.","SPECRTIL PLUS":"Enrofloksatsin+Bromgeksin. 1L.","SPECTRA HERBROM":"Bromgeksin+Timol+Evkalipt. 1L.","VINORAL":"Vitaminlar va aminokislotalar. 1L."}
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
    m.add(InlineKeyboardButton("🩺 Mutaxassis",callback_data="HELP"))
    m.add(InlineKeyboardButton("🏪 Savdo bolimi",callback_data="SALES"))
    return m
def dm(lst):
    m=InlineKeyboardMarkup()
    for d in lst:
        m.add(InlineKeyboardButton(d,callback_data=f"D{d[:30]}"))
    m.add(InlineKeyboardButton("🔙 Orqaga",callback_data="BACK"))
    return m
def mutaxassis_menyu():
    m=InlineKeyboardMarkup()
    m.add(InlineKeyboardButton("👨‍⚕️ Ergashev Akbarjon",callback_data="M1"))
    m.add(InlineKeyboardButton("👨‍⚕️ Axmadaliyev Nurmuhammad",callback_data="M2"))
    m.add(InlineKeyboardButton("👨‍⚕️ Xomitjonov Ulugbek",callback_data="M3"))
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
        bot.send_message(call.message.chat.id,"🩺 Mutaxassisni tanlang:",reply_markup=mutaxassis_menyu())
    elif d=="M1":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("💬 @Welcome_to_my_profile",url="https://t.me/Welcome_to_my_profile"))
        bot.send_message(call.message.chat.id,"👨‍⚕️ Ergashev Akbarjon\n💬 @Welcome_to_my_profile",reply_markup=m)
    elif d=="M2":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("💬 @poultry_uz_vet",url="https://t.me/poultry_uz_vet"))
        bot.send_message(call.message.chat.id,"👨‍⚕️ Axmadaliyev Nurmuhammad\n💬 @poultry_uz_vet",reply_markup=m)
    elif d=="M3":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("💬 @Obidjonovich27_11",url="https://t.me/Obidjonovich27_11"))
        bot.send_message(call.message.chat.id,"👨‍⚕️ Xomitjonov Ulugbek\n💬 @Obidjonovich27_11",reply_markup=m)
    elif d=="SALES":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("👤 Otabek Duschanovich",callback_data="OTABEK"))
        bot.send_message(call.message.chat.id,"🏪 Savdo bolimi:",reply_markup=m)
    elif d=="OTABEK":
        m=InlineKeyboardMarkup()
        m.add(InlineKeyboardButton("💬 @Duschanovich",url="https://t.me/Duschanovich"))
        bot.send_message(call.message.chat.id,"👤 Otabek Duschanovich\n💬 @Duschanovich",reply_markup=m)
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
                bot.send_message(call.message.chat.id,f"💊 {k}\n📋 {v}")
                return
bot.infinity_polling()
