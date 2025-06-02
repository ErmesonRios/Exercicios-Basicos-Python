import time

segundos = []

for segundos in range(0, 100):
    if segundos %2 == 0:
        print("\ne par")
    else:
        print("\ne impar")
    
    print(f"\n{segundos} segundos")
    time.sleep(1)