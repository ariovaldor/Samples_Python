from datetime import date, time, datetime
def trabalhando_com_date():
    print('Data:')
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y')) # y minúsculo, ano c/ dois digitos

    print(data_atual.strftime('%d/%m/%Y')) # Y maiúsculo 4 digitos
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
def trabalhando_com_time():
    print('time:')
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(horario.strftime('%H:%M:%S'))
def trabalhando_com_datetime():
    print('datetime:')
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) # Pego só hora, minuto e segundo do datetime


if __name__ ==  '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()

