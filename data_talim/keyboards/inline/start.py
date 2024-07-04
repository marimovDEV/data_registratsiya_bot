from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏢Data telefon raqam📞',callback_data='data_tel')],
    [InlineKeyboardButton(text='👨🏻‍💻Hozirgi kurslar👩🏻‍💻',callback_data='now_lessons'),
     InlineKeyboardButton(text='🆕Yangi kurslar',callback_data='new_lessons')
     ],
    [InlineKeyboardButton(text='👨🏻‍💻Kurslar👩🏻‍💻',callback_data='lessons')],
    [InlineKeyboardButton(text='✍🏻Ro\'yhattan otish📤',callback_data='register')]
])

l_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏮️Asosiy menyuga qaytish⏮️',callback_data='back')],
                                              [InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back_l')]])
new_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏮️Asosiy menyuga qaytish⏮️',callback_data='back')],
                                              [InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back_new')]])
now_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⏮️Asosiy menyuga qaytish⏮️',callback_data='back')],
                                              [InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back_now')]])



# async def builder():
#     builder = InlineKeyboardBuilder()
#     for yonalish in yonalishlar: 
        
#         builder.add(InlineKeyboardButton(text=yonalish,callback_data=yonalish))
#     builder.add(InlineKeyboardButton(text=yonalish,callback_data=yonalish))
    
#     builder.adjust(2)
#     return builder.as_markup(resize_keyboard=True)
