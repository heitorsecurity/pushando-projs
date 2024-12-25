"""import time
import os

try:
    import ntplib
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
    print('Não pude sincronizar o relógio com o servidor.')

print('Feito.')"""

import ntplib
import time

def pegar_o_tempo_ntp():
    try:
        c = ntplib.NTPClient()
        response = c.request('br.pool.ntp.org')
        return time.ctime(response.tx_time)
    except ntplib.NTPException as e:
        return f"Erro tentando puxar o tempo do NTP: {e}"
    except Exception as e:
        return f"Um erro inesperado ocorreu: {e}"

# Chame a funcao e printe o resultado
print(pegar_o_tempo_ntp())
