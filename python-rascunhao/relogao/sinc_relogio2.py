import ntplib
import time

def pegar_o_tempo_ntp():
    try:
        c = ntplib.NTPClient()
        response = c.request('br.pool.ntp.org')
        return time.ctime(response.tx_time), response.tx_time
    except ntplib.NTPException as e:
        return f"Erro tentando puxar o tempo do NTP: {e}", None
    except Exception as e:
        return f"Um erro inesperado ocorreu: {e}", None

"""# Chame a funcao e printe o resultado
print(pegar_o_tempo_ntp())"""

# Pegar o tempo NTP
resultado_ntp, ntp_tempo = pegar_o_tempo_ntp()

if ntp_tempo is not None:
    # Pegar o tempo do relogio da maquina
    tempo_agora = time.time()
    """time.process_time() e time.perf_counter() pegam outros tipos de
    relogios menos precisos dependendo do sistema pois sao melhores usados em
    sessoes, nao contando o tempo durante descanso ou hibernacao do sistema"""
    tempo_agora_str = time.ctime(tempo_agora)

    # Calcular a diferenca em segundos
    dif_sec = abs(tempo_agora - ntp_tempo)

    # Converter a diferenca em milisegundos se menos de 1 segundo
    if dif_sec < 1:
        dif_ms = int(dif_sec * 1000)
        dif_str = f"{dif_ms} milisegundos"
    else:
        dif_str = f"{dif_sec:.2f} segundos"

    # Imprima os resultados
    print(f"Tempo puxado do NTP: {resultado_ntp}")
    print(f"Meu relogio da maquina: {tempo_agora_str}")
    print(f"Quantos segundos ou milisegundos difere um do outro: {dif_str}")
else:
    print(resultado_ntp)