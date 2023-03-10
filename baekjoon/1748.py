# 제한시간 0.5초 5000만 연산
# 10^8 -> 모두 방문 할 시 제한시간 1초


# 1자리수 -> 9개  15 -> 9개 + 6개*2 -> 21개 
# 2자리수 -> 9개 + 90*2개 ----> 120 -> 9 + 90*2 + 21*3 189+63-> 252
# 3자리수 -> 9개 + 90*2개 + 900*3개


n = int(input())

ans = 0

# 시간복잡도 -> O(logn) ~ 10
for i in range(1, len(str(n))):
    ans += 9 * (10 ** (i-1)) * i
ans += (n - 10 ** (len(str(n))-1) + 1) * len(str(n))
print(ans)
    
