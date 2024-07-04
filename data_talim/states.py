from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext

class Reg(StatesGroup):
    full_name = State()
    phone_number = State()
    home_adress = State()
    kurs = State()
    submit = State()
    
class AdminState(StatesGroup):
    are_you_sure = State()
    ask_ad_content = State()