def merge_the_tools(string, k):
    # your code goes here
    list_of_k_str = []
    len_str = int(len(string))
    each_substr_size = int(int(len_str) / int(k))
    t = 0
    list_unique_chars = []

    def sortString(stri):
        return ''.join(sorted(stri))

    if len_str % k != 0:
        print("invalid  input: str cannot be divided by k")
        return
    else:
        while t != len_str:
            if t % each_substr_size == 0 :
                list_of_k_str.append(string[t:t+each_substr_size])
            t = t+each_substr_size

        print(list_of_k_str)
        for ele in list_of_k_str:
            temp = ''
            for chars in ele:
                if chars not in temp:
                    temp = temp+chars
            print(sortString(temp))

def merge_tool_2(string,k):
    for substr in zip(*[iter(string)] *k):
        dic = dict()
        print(''.join([dic.setdefault(chr1, chr1) for chr1 in substr if chr1 not in dic]))


if __name__ == '__main__':
    string, k = 'AABCAAADA', 3  # input(), int(input())
    merge_tool_2(string, k)
