import datetime
from workalendar.america import Brazil

cal = Brazil()

# Definindo o ano para o qual você deseja calcular os dias úteis
ano = 2023

# Obtendo a lista de feriados
feriados = cal.holidays(ano)

# Definindo a data inicial e final do ano
data_inicial = datetime.date(ano, 1, 1)
data_final = datetime.date(ano, 12, 31)

# Calculando a diferença entre as datas e excluindo os feriados
dias_uteis = 0
data_atual = data_inicial
while data_atual <= data_final:
    if data_atual.weekday() < 5 and data_atual not in feriados:
        dias_uteis += 1
    data_atual += datetime.timedelta(days=1)

print(f"Em {ano}, há {dias_uteis} dias úteis.")
