from config import PHONE_NUMBER,BAZA
import sqlite3



def get_hendlers()-> list:
    connection = sqlite3.connect(BAZA)
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM main_hendlers')
    hendlers = cursor.fetchall()
    
    lst=[]
    
  
    
    for hendler in hendlers[0]:
        lst.append(hendler)
    
    
    return lst

# msg_start = 'Assalomu aleykum\nData ta\'lim stansiyasiga hush kelibsiz\n\n\nO\'zingizga kerakli bo\'limni tanlang👇'
msg_start = get_hendlers()[12]

msg_kurs = get_hendlers()[1]
msg_name = get_hendlers()[2]
msg_phone = get_hendlers()[3]
msg_adres = get_hendlers()[4]

def Reg_about(kurs,full_name,phone_number,home_adress):
    return f'Malumotlaringiz tog\'rimi agar tog\'ri bolsa xa ni bosing\nKurs : {kurs} \n\nIsm Familiya : {full_name}\nTelefon raqam : +{phone_number}\nUy manzil : {home_adress}'

reseption = get_hendlers()[13]

data_tel = get_hendlers()[5]

now_lessons_msg = get_hendlers()[6]
new_lessons_msg =get_hendlers()[7]
lessons_msg =get_hendlers()[ 8]

l_message = get_hendlers()[9]
new_message = get_hendlers()[10]
now_message = get_hendlers()[11]



print(len(get_hendlers()))