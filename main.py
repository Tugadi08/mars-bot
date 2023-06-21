import logging

from aiogram import Bot, Dispatcher, executor, types
from button1 import *

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте! Выберите язык", reply_markup=til_menu)


@dp.message_handler(text = "🇺🇿Uz")   
async def echo(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variantni tanlang")
    await message.answer("Пожалуйста укажите кем вы являетесь))", reply_markup=kim_ligi)


@dp.message_handler(text = "🇷🇺Ru")
async def echo(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variantni tanlang")
    await message.answer("Пожалуйста укажите к          ем вы являетесь))", reply_markup=kim_ligi)

@dp.message_handler(text = "👨‍👩‍👦Я родитель")
async def echo(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variantni tanlang", reply_markup=parents_menu) 


@dp.message_handler(text = "👨‍🎓Я студент")
async def echo(message: types.Message):
    await message.answer("Введите свой id Modme",)


@dp.message_handler(text = "👤Я гость")
async def echo(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variantni tanlang", reply_markup=gost_menu)


@dp.message_handler(text = "📍 Филиалы")
async def echo(message: types.Message):
    await message.answer(
"""Hozirda ikkita filialimiz mavjud.

📍Tinchlik Filiali
Manzil: Toshkent shahar, Tinchlik metrosi, Beruniy 35 A
Telefon raqam:
+998954105054
+998954115054
📍Filial Yunusobod
Manzil: Yunusobod tumani, Stroy sentr, 3-qavat
Telefon raqam: +998901165054
+998901175054

🗺Quyidagi tugmalar orqali filial manzilini olishingiz mumkin.
""", reply_markup=lakatsiya_menu)   


@dp.message_handler(text = "TINCHLIK")
async def echo(message: types.Message):
    await message.answer_location(41.33470570596154, 69.21551549086648)



@dp.message_handler(text = "YUNUSOBOD")
async def echo(message: types.Message):
    await message.answer_location(41.367028160587836, 69.28620326334263)


@dp.message_handler(text = "🔙Ortga")
async def echo(message: types.Message):
    await message.answer("Bosh menu", reply_markup=gost_menu)



@dp.message_handler(text = "📝 О наших курсах")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/vd_uz_n1/10")



@dp.message_handler(text = "🔥 Работы наших учеников")
async def echo(message: types.Message):
    await message.answer_video("https://t.me/vd_uz_n1/3?single")
    await message.answer_video("https://t.me/vd_uz_n1/4?single")
    await message.answer_video("https://t.me/vd_uz_n1/5?single")
    await message.answer_video("https://t.me/vd_uz_n1/6?single")
    await message.answer_video("https://t.me/vd_uz_n1/7?single")
    await message.answer_video("https://t.me/vd_uz_n1/8?single")
    await message.answer_video("https://t.me/vd_uz_n1/9?single")


@dp.message_handler(text = "⭐️ Отзывы")
async def echo(message: types.Message):
    await message.answer_video("https://t.me/vd_uz_n1/11")
    await message.answer_video("https://t.me/vd_uz_n1/12")
    await message.answer_video("https://t.me/vd_uz_n1/13")
    await message.answer_video("https://t.me/vd_uz_n1/14")
    await message.answer_video("https://t.me/vd_uz_n1/15")
    await message.answer_video("https://t.me/vd_uz_n1/16")


@dp.message_handler(text = "☎️ Контакты и наши страницы")
async def echo(message: types.Message):
    await message.answer("""
    Biz bilan bog'laning
    ☎️ 78 777 77 57
    Ijtimoiy tarmoqlarimizni kuzatib boring👇
    Instagram Telegram
            """,    
    )




@dp.message_handler(text = "🏫 О школе")
async def echo(message: types.Message):
    await message.answer("Xozirda prafilaktika iwlari olib borilayapti")


@dp.message_handler(text = "✍️ Оставить отзыв")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/vd_uz_n1/10", caption="Напишите свой отзыв")


@dp.message_handler(text = "👨‍👩‍👦 Добавить ребёнка")
async def echo(message: types.Message):
    await message.answer("Пожалуйста введите Modme id вашего ребёнка", reply_markup=parents_menu_menu)



@dp.message_handler(text = "👨‍👩‍👧‍👦 Мои дети")
async def echo(message: types.Message):
    await message.answer("""
👨‍👩‍👧‍👦Ребёнок 1: Modme id
Группа: BACK-415
Учитель: Asadbek Rahimov
    """)


@dp.message_handler(text = "📉 Результаты моих детей")
async def echo(message: types.Message):
    await message.answer("""
💲 Результаты ваших детей:

Modme id: 100
    """)
    

@dp.message_handler(text = "📍 Филиалыы")
async def echo(message: types.Message):
    await message.answer(
"""Hozirda ikkita filialimiz mavjud.

📍Tinchlik Filiali
Manzil: Toshkent shahar, Tinchlik metrosi, Beruniy 35 A
Telefon raqam:
+998954105054
+998954115054
📍Filial Yunusobod
Manzil: Yunusobod tumani, Stroy sentr, 3-qavat
Telefon raqam: +998901165054
+998901175054

🗺Quyidagi tugmalar orqali filial manzilini olishingiz mumkin.
""", reply_markup=lakatsiya2_menu)



@dp.message_handler(text = "🔙Orqaga")
async def echo(message: types.Message):
    await message.answer("Bosh menu", reply_markup=parents_menu_menu)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Bizda bunday malumot yo'q")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)