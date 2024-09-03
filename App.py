import psutil
import time


def mostrar_info_sistema():
    while True:

        uso_cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        armazenamento = psutil.disk_usage('/')


        print(f"\nUso da CPU: {uso_cpu}%")
        print(f"Memória Usada: {memoria.used / (1024 ** 3):.2f} GB")
        print(f"Memória Total: {memoria.total / (1024 ** 3):.2f} GB")
        print(f"Armazenamento Usado: {armazenamento.used / (1024 ** 3):.2f} GB")
        print(f"Armazenamento Total: {armazenamento.total / (1024 ** 3):.2f} GB")
        print(f"Armazenamento Restante: {armazenamento.total / (1024**3) - armazenamento.used / (1024**3): .2f}GB " )
        time.sleep(5)


mostrar_info_sistema()
