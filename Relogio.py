import time
import os

def relogio():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        hora = time.strftime("%H:%M:%S")
        print(f"essa e a hora{hora}")
        time.sleep(1)
        
if __name__ == "__main__":
    relogio()