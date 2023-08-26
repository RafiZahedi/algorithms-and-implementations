for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    num_to_check = nums.count(nums[-1])
    if num_to_check % k == 0:
        print("YES")
    else:
        print("NO")

