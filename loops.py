def max_profit(P):
    B = P[0]
    PF = 0

    for i in range(len(P)):
        if B < P[i]:
            PF = max(PF, P[i] - B)
        else:
            B = P[i]

    return PF


# CALL THE FUNCTION
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))