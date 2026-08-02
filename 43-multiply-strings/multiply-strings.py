class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - 48

            for j in range(n - 1, -1, -1):
                b = ord(num2[j]) - 48

                pos = i + j + 1
                total = a * b + result[pos]

                result[pos] = total % 10
                result[pos - 1] += total // 10

        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))