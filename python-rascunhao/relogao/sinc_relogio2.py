import ntplib
import time

def get_ntp_time():
    try:
        c = ntplib.NTPClient()
        response = c.request('south-america.pool.ntp.org')
        return time.ctime(response.tx_time)
    except ntplib.NTPException as e:
        return f"Erro tentando puxar o tempo do NTP: {e}"
    except Exception as e:
        return f"Um erro inesperado ocorreu: {e}"

# Chame a funcao e printe o resultado
print(get_ntp_time())
