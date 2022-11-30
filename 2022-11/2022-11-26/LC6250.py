class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        j,avoidP = 0,0

        p = 0
        for i in range(N):
            if customers[i] == 'Y':
                p += 1
            else:
                p -= 1

            if p > avoidP:
                j = i+1
                avoidP = p

        return j