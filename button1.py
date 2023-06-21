from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


til_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺Ru"),
            KeyboardButton(text="🇺🇿Uz")
        ]
    ],
    resize_keyboard=True
)



kim_ligi= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍👩‍👦Я родитель"),
            KeyboardButton(text="👨‍🎓Я студент"),
            KeyboardButton(text="👤Я гость")
        ]
    ],
    resize_keyboard=True
)

parents_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏫 О школе"),
            KeyboardButton(text="👨‍👩‍👦 Добавить ребёнка")
        ]
    ],
    resize_keyboard=True
)


parents_menu_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👨‍👩‍👧‍👦 Мои дети"),
            KeyboardButton(text="📉 Результаты моих детей"),
            KeyboardButton(text="📍 Филиалыы")
        ],
        [
            KeyboardButton(text="📝 О наших курсах"),
            KeyboardButton(text="🔥 Работы наших учеников"),
            KeyboardButton(text="⭐️ Отзывы")
        ],
        [
            KeyboardButton(text="☎️ Контакты и наши страницы"),
            KeyboardButton(text="✍️ Оставить отзыв"),
            KeyboardButton(text="👨‍👩‍👦 Добавить ребёнка")
        ]
    ],
    resize_keyboard=True
)


gost_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Филиалы"),
            KeyboardButton(text="📝 О наших курсах"),
            KeyboardButton(text="🔥 Работы наших учеников")
        ],
        [
            KeyboardButton(text="⭐️ Отзывы"),
            KeyboardButton(text="☎️ Контакты и наши страницы"),
            KeyboardButton(text="🏫 О школе")
        ],
        [
            KeyboardButton(text="✍️ Оставить отзыв")
        ]
    ],
    resize_keyboard=True
)


lakatsiya_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TINCHLIK"),
            KeyboardButton(text="YUNUSOBOD")
        ],
        [
            KeyboardButton(text="🔙Ortga")
        ]
    ],
    resize_keyboard=True
)

lakatsiya2_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TINCHLIK"),
            KeyboardButton(text="YUNUSOBOD")
        ],
        [
            KeyboardButton(text="🔙Orqaga ")
        ]
    ],
    resize_keyboard=True
)