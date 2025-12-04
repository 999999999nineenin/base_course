import time

timer = time.time()
for i in range(10):
    print(i)
    time.sleep(1) #секунды

print(f'{time.time() - timer}, seconds')