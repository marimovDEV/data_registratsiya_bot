import sqlite3
from config import BAZA
from aiogram.types import KeyboardButton,InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder


def insert_lesson(lesson,about_lesson,photo):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('INSERT INTO main_lessons ( lesson, about_lesson,photo) VALUES (?, ?,?)', (lesson,about_lesson,photo))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def insert_now_lesson(lesson,about_lesson,photo):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('INSERT INTO main_now_lessons ( lesson, about_lesson,photo) VALUES (?,?,?)', (lesson,about_lesson,photo))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()



def insert_new_lesson(lesson,about_lesson,photo):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('INSERT INTO main_new_lessons ( lesson, about_lesson,photo) VALUES (?, ?,?)', (lesson,about_lesson,photo))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()
    

def insert_student(full_name,phone_number,home_address,kurs,created_at):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('INSERT INTO main_students (full_name,phone_number,home_address,kurs,created_at) VALUES (?,?,?,?,?)', (full_name,phone_number,home_address,kurs,created_at))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def insert_user(full_name,telegram_id,username):
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO main_users (full_name,telegram_id,username) VALUES (?,?,?)', (full_name,telegram_id,username))
        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
    except:
        pass
    
def get_user():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_users')
    users = cursor.fetchall()
    
    lst = []
    
    for user in users: 
        lst.append(user[1])
       
    return lst

    
def get_lessons():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_lessons')
    lessons = cursor.fetchall()
    
    
    builder = InlineKeyboardBuilder()
    for lesson in lessons: 
        
        builder.add(InlineKeyboardButton(text=lesson[1],callback_data=f'lesson_l_{lesson[1]}'))
    # builder.add(InlineKeyboardButton(text=yonalish,callback_data=yonalish))
    builder.add(InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back'))
    builder.adjust(2)
    return builder.as_markup()



def get_lessons_defoult():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_lessons')
    lessons = cursor.fetchall()
    
    
    builder = ReplyKeyboardBuilder()
    for lesson in lessons: 
        
        builder.add(KeyboardButton(text=lesson[1]))
    # builder.add(InlineKeyboardButton(text=yonalish,callback_data=yonalish))
    
    builder.adjust(2)
    return builder.as_markup(one_time_keyboard=True,resize_keyboard=True)



def get_now_lesson():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM main_now_lessons')
    
    now_lessons = cursor.fetchall()
    
    builder = InlineKeyboardBuilder()
    
    for now_lesson in now_lessons:
        
        builder.add(InlineKeyboardButton(text=now_lesson[1],callback_data=f'lesson_now_{now_lesson[1]}'))
    builder.adjust(2)
    builder.add(InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back'))
    
    return builder.as_markup()



def get_new_lesson():
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM main_new_lessons')
    
    new_lessons = cursor.fetchall()
    
    builder = InlineKeyboardBuilder()
    
    for new_lesson in new_lessons:
        
        builder.add(InlineKeyboardButton(text=new_lesson[1],callback_data=f'lesson_new_{new_lesson[1]}'))
    builder.adjust(2)
    builder.add(InlineKeyboardButton(text='⏪Ortga⏪',callback_data='back'))
    
    return builder.as_markup()


def get_about_lessons(key)-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_lessons')
    lessons = cursor.fetchall()
    
    lst=[]
    
  
    
    for lesson in lessons:
        if lesson[1]==key:
            lst.append(f'{lesson[1]}\n\n{lesson[2]}')
            lst.append(lesson[3])
    
    
    return lst

def get_about_new_lessons(key)-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_new_lessons')
    new_lessons = cursor.fetchall()
    
    lst=[]
    
    
    
    for new_lesson in new_lessons:
        if new_lesson[1]==key:
            
            lst.append(f'{new_lesson[1]}\n\n{new_lesson[2]}')
            lst.append(new_lesson[3])
    
    return lst


def get_about_now_lessons(key)-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_now_lessons')
    now_lessons = cursor.fetchall()
    
    lst=[]
    

    
    for now_lesson in now_lessons:
        if now_lesson[1]==key:
            
            lst.append(f'{now_lesson[1]}\n\n{now_lesson[2]}')
            lst.append(now_lesson[3])
    
    return lst
    
    
    
    



def get_admin()-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_bot_admin')
    admins = cursor.fetchall()
    
    lst=[]
    

    
    for admin in admins:
        
            
        lst.append(admin[1])
    
    return lst
    

    
    



