import time

now = time.time()
future = now + 10
while time.time() < future:
    # do stuff
    print("wow")

# for i in range(1):
#     print(worksheet.cell_value(i,1))