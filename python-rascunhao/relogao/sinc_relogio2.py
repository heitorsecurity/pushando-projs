import ntplib
import time

def get_ntp_time():
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org')
    return time.ctime(response.tx_time)

# Chame a funcao e printe o resultado
print(get_ntp_time())
