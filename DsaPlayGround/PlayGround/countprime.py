class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        prime = [True for i in range(n+1)]
        count = 0
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * 2, n+1, p):
                    prime[i] = False
            p += 1
        prime[0], prime[1] = False, False
        for p in range(n):
            if prime[p]:
                count += 1
        return count
