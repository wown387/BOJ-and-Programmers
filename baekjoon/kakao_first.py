
def solution(n, arr1, arr2):
    answer = []
    result = []

    for i in range(n):

        b_2 = bin(arr1[i])[2:]

        if len(b_2) != n:
            b_2 = (n - len(b_2)) * "0" + b_2

        arr1_b = b_2

        b_2 = bin(arr2[i])[2:]

        if len(b_2) != n:
            b_2 = (n - len(b_2)) * "0" + b_2

        arr2_b = b_2

        w = ""
        for i in range(n):
            if arr1_b[i] == "1" or arr2_b[i] == "1":
                w = w + "#"
            else:
                w = w + " "
        print(arr1_b, arr2_b)
        print(w)
        result.append(w)
    print(result)

    return result




