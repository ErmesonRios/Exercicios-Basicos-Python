import time
import os

def relogio():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        hora = time.strftime("%H:%M:%S")
        data = time.strftime("%d/%m/%Y")
        print("Relógio Atual:")
        print(f"essa e a hora: {hora}: {data}")
        time.sleep(1)
        if hora == "17:00:00":
            print("Hora de ir embora!")
            break
        
if __name__ == "__main__":
    relogio()