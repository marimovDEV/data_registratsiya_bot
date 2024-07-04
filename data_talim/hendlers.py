import os
import datetime
import logging
from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,FSInputFile,ReplyKeyboardRemove
from admin import IsBotAdminFilter
from aiogram.filters import CommandStart,Command
from baza_p import (
    get_lessons,get_now_lesson,
    get_new_lesson,insert_student,
    get_lessons_defoult,get_about_lessons,
    get_about_new_lessons,get_about_now_lessons,
    insert_user,get_user,get_admin)
from keyboards.inline.start import start_kb,l_kb,new_kb,now_kb
from config import PHONE_NUMBER
from states import Reg,AdminState
from aiogram.fsm.context import FSMContext
from keyboards.defoalt.reply import phone_kb,submit_kb
from msg import (
    msg_start,msg_adres,msg_kurs,msg_name,
    msg_phone,Reg_about,reseption,
    data_tel,now_lessons_msg,
    new_lessons_msg,lessons_msg,
    l_message,new_message,now_message
)


ADMIN = get_admin()

router = Router()

logo_data = 'data_talim/images/data_logo.jpg'



# @router.message(F.text=='/start', IsBotAdminFilter(ADMIN))
# async def get_all_users(message: Message):
#     await message.reply('admin')


@router.message(Command('reklama'), IsBotAdminFilter(ADMIN))
async def ask_ad_content(message: Message, state: FSMContext):
    await message.answer("Reklama uchun post yuboring")
    await state.set_state(AdminState.ask_ad_content)


@router.message(AdminState.ask_ad_content, IsBotAdminFilter(ADMIN))
async def send_ad_to_users(message: Message, state: FSMContext):
    users = get_user()
    count = 0
    for user in users:
        user_id = user
        try:
            await message.send_copy(chat_id=user_id)
            count += 1
            await asyncio.sleep(0.05)
        except Exception as error:
            logging.info(f"Ad did not send to user: {user_id}. Error: {error}")
    await message.answer(text=f"Reklama {count} ta foydalauvchiga muvaffaqiyatli yuborildi.")
    await state.clear()






@router.message(F.text=='/start')
async def start(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    username = message.from_user.username
    insert_user(full_name,telegram_id,username)
   
    x = msg_start.replace('\\n', '\n')
    
    await message.answer_photo(photo=FSInputFile(logo_data),caption=f"{x}", reply_markup=start_kb)    




@router.callback_query(F.data=='register')
async def register(callback:CallbackQuery,state:FSMContext):
    await state.set_state(Reg.kurs)
    x = msg_kurs.replace('\\n', '\n')
    await callback.message.answer(x,reply_markup=get_lessons_defoult())


@router.message(Reg.kurs)
async def reg_fullname(message:Message,state:FSMContext):
    await state.update_data(kurs=message.text)
    await state.set_state(Reg.full_name)
    x = msg_name.replace('\\n', '\n')
    await message.answer(x,reply_markup=ReplyKeyboardRemove())
    
@router.message(Reg.full_name)
async def reg_phone(message:Message,state:FSMContext):
    
    await state.update_data(full_name=message.text)
    await state.set_state(Reg.phone_number)
    x = msg_phone.replace('\\n', '\n')
    await message.answer(x,reply_markup=phone_kb)

@router.message(Reg.phone_number)
async def reg_adress(message:Message,state:FSMContext):
    try:
        contact = message.contact
        phone_number = contact.phone_number
        await state.update_data(phone_number=phone_number)
        
        await state.set_state(Reg.home_adress)
        x = msg_adres.replace('\\n', '\n')
        await message.reply(x,reply_markup=ReplyKeyboardRemove())
    except:
        await message.reply('Xatolik mavjud')
        await state.set_state(Reg.phone_number)
        x = msg_phone.replace('\\n', '\n')
        await message.answer(x,reply_markup=phone_kb)


@router.message(Reg.home_adress)
async def reg_kurs(message:Message,state:FSMContext):
    await state.update_data(home_adress=message.text)
    data = await state.get_data()
    await state.set_state(Reg.submit)
    txt = Reg_about(data["kurs"],data["full_name"],data["phone_number"],data["home_adress"])
    await message.reply(txt,reply_markup=submit_kb)


@router.message(Reg.submit)
async def submit(message:Message,state:FSMContext):
    await state.update_data(submit=message.text)
    text = message.text
    if text=='✅Xa✅':
        data = await state.get_data()
        full_name=data['full_name']
        phone_number=data['phone_number']
        home_adress=data['home_adress']
        kurs=data['kurs']
        created_at=datetime.datetime.now()
        insert_student(full_name,phone_number,home_adress,kurs,created_at)
        await state.clear()
        x = reseption.replace('\\n', '\n')
        await message.answer(x,reply_markup=ReplyKeyboardRemove())
    else:
        await state.set_state(Reg.kurs)
        await message.reply('Iltimos boshqatdan toldiring')
        x = msg_kurs.replace('\\n', '\n')
        await message.reply(x,reply_markup=get_lessons_defoult())


@router.callback_query(F.data=='data_tel')
async def set_phone(callback:CallbackQuery):
    await callback.message.delete()
    x = data_tel.replace('\\n', '\n')
    await callback.message.answer_photo(photo=FSInputFile(logo_data),caption=x,reply_markup=start_kb)
    
    
@router.callback_query(F.data=='now_lessons')
async def set_now_lessons(callback:CallbackQuery):
    await callback.message.delete()
    x = now_lessons_msg.replace('\\n', '\n')
    await callback.message.answer(x,reply_markup=get_now_lesson())
    
@router.callback_query(F.data=='new_lessons')
async def set_new_lessons(callback:CallbackQuery):
    await callback.message.delete()
    x = new_lessons_msg.replace('\\n', '\n')
    await callback.message.answer(x,reply_markup=get_new_lesson())


@router.callback_query(F.data=='lessons')
async def lessons(callback:CallbackQuery):
    await callback.message.delete()
    x = lessons_msg.replace('\\n', '\n')
    await callback.message.answer(x,reply_markup=get_lessons())
    
@router.callback_query(F.data=='back')
async def set_now_lessons(callback:CallbackQuery):
    await callback.message.delete()
    x = msg_start.replace('\\n', '\n')
    await callback.message.answer_photo(photo=FSInputFile(logo_data),caption=x, reply_markup=start_kb)    
    
    
@router.callback_query(F.data.startswith('lesson_'))
async def about_of_lessons(callback:CallbackQuery):
    action = callback.data.split("_")
    
    if action[1]=='l':
        txt=f'{l_message}\n\n'
        txt+=get_about_lessons(action[2])[0]
        photo=get_about_lessons(action[2])[1]
        kb = l_kb
        
    elif action[1]=='now':
        txt=f'{now_message}\n\n'
        txt+=get_about_now_lessons(action[2])[0]
        photo=get_about_now_lessons(action[2])[1]
        kb =now_kb
    elif action[1]=='new':
        txt=f'{new_message}\n\n'
        txt+=get_about_new_lessons(action[2])[0]
        photo=get_about_new_lessons(action[2])[1]
        kb=new_kb
    await callback.message.delete()
    await callback.message.answer_photo(photo=FSInputFile(photo),caption=txt, reply_markup=kb)    
    

@router.callback_query(F.data.startswith('back_'))
async def back_asosiy(callback:CallbackQuery):
    action = callback.data.split("_")[1]
    txt =''
    if action=='l':
        txt=l_message.replace('\\n', '\n')
        markup=get_lessons()
        
    # elif action=='g':
    #     await callback.message.delete()
    #     await callbacks.message.answer_photo(photo=FSInputFile(logo_data),caption=msg_start, reply_markup=start_kb)
    elif action=='new':
        txt=new_message.replace('\\n', '\n')
        markup=get_new_lesson()
        
    elif action=='now':
        txt=now_message.replace('\\n', '\n')
        markup=get_now_lesson()
    await callback.message.delete()
    await callback.message.answer(txt,reply_markup=markup)
