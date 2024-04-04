def solve():
    a, b, l = map(int, input().split())
    st = set()
    for first in range(l):
        pow_a = pow(a, first)
        if pow_a > l:
            break
        for second in range(l):
            temp = pow_a * pow(b, second)
            if temp > l:
                break
            if l % temp == 0:
                st.add(l // temp)
    return len(st)  


for _ in range(int(input())):
    print(solve())
