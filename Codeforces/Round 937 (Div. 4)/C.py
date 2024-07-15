from datetime import datetime


def solve():
    input_time = datetime.strptime(input(), "%H:%M")
    return input_time.strftime("%I:%M %p")


for _ in range(int(input())):
    print(solve())
