#DATA E HORA
from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))


    #DIA MÊS E ANO
    from datetime import date
    data_atual = date.today()
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))



def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%c'))
    #TRADUZINDO OS DIA DA SEMANA
    print(data_atual.weekday())
    tuple = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tuple[data_atual.weekday()])
     #SUBITRAÇÃO E SOMA DE DATA
    nova_data = data_criada - timedelta(days=365) #tirei 1 ano
    print(nova_data)


if __name__ == '__main__':
   trabalhando_com_date()
   trabalhando_com_time()
   trabalhando_com_datetime()
