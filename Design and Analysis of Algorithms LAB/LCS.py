def longest_common_substring(string1,string2):
    m = len(string1)
    n = len(string2)
    sub_string = [[0 for j in range(n+1)] for i in range(m+1)]
    last_index = 0
    max_length = 0
    for i in range(m):
        for j in range(n):
            if string1[i] == string2[j]:
                if i == 0 or j == 0:
                    sub_string[i][j] = 1
                else:
                    sub_string[i][j] = sub_string[i-1][j-1]+1
                if sub_string[i][j] > max_length:
                    max_length = sub_string[i][j]
                    last_index = i
    if max_length == 0:
        return max_length, ""
    start = last_index - max_length + 1
    return max_length, string1[start:last_index+1]

string1 = "ATAGSSSSSSSSDJFIUWFSKJFSUESATEFFASF"
string2 = "DWHDHOISFNOSFOIOINSFSDASSSSSSSSSDSA"
length, longest = longest_common_substring(string1,string2)
print("Length of LCS is", length)
print("Longest common substring is", longest)
