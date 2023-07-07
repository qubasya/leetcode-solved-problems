def longestperf(strs):

    if not strs:
        return ""  

    min_len = min(len(s) for s in strs)  

    for i in range(min_len):
        prefix = strs[0][i]  
        for j in range(1, len(strs)):
            if strs[j][i] != prefix:
                return strs[0][:i] 

    return strs[0][:min_len]
print("THE END : ",longestperf(["flower","gfow","fligowwwht"]))

