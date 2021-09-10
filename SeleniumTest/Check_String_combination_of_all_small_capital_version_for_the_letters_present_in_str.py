# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def checkCurrentString(lower_aplha, upper_alpha):
    for idx in range(26):
        if lower_aplha[idx] != 0 and (upper_alpha[idx] == 0):
            return 0
        elif lower_aplha[idx] == 0 and (upper_alpha[idx] != 0):
            return 0

    return 1


def solution(S):
    # write your code in Python 3.6
    lower_a = [0 for idx in range(26)]

    upper_a = [0 for idx in range(26)]

    dict_pos = {}

    for idx in range(len(S)):
        if (ord(S[idx]) >= 65 and ord(S[idx]) <= 90):
            upper_a[ord(S[idx]) - 65] += 1
        else:
            lower_a[ord(S[idx]) - 97] += 1

    for idx in range(len(lower_a)):
        lower_a[idx] = 0
        upper_a[idx] = 0

    idc = 0

    stx = 0

    start_pt = -1
    end_pt = -1

    smallest_bal_str = sys.maxsize

    while (idc < len(S)):
        if (S[idc] in dict_pos):

            while (stx < idc):
                if (ord(S[stx]) >= 65 and ord(S[stx]) <= 90):
                    upper_a[ord(S[stx]) - 65] -= 1
                else:
                    lower_a[ord(S[stx]) - 97] -= 1
                stx += 1

            idc += 1
            stx += 1
        else:
            if (ord(S[idc]) >= 65 and ord(S[idc]) <= 90):
                upper_a[ord(S[idc]) - 65] += 1
            else:
                lower_a[ord(S[idc]) - 97] += 1

            while (1):
                if (ord(S[stx]) >= 65 and ord(S[stx]) <= 90 and upper_a[ord(S[stx]) - 65] > 1):
                    upper_a[ord(S[stx]) - 65] -= 1
                    stx += 1
                elif (ord(S[stx]) >= 97 and ord(S[stx]) <= 122 and lower_a[ord(S[stx]) - 97] > 1):
                    lower_a[ord(S[stx]) - 97] -= 1
                    stx += 1
                else:
                    break

            if (checkCurrentString(lower_a, upper_a)):
                if (smallest_bal_str > (idc - stx + 1)):
                    smallest_bal_str = idc - stx + 1
                    start_pt = stx
                    end_pt = idc

            idc += 1

    if (start_pt == -1 or end_pt == -1):
        return -1


    else:
        answer = ""
        for index in range(start_pt, end_pt + 1, 1):
            answer += S[index]

        return len(answer)


if __name__ == "__main__":
    S = "AcZCbaBZ"

    print(solution(S))



