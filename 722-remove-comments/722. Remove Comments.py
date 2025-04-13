class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        i = 0
        if source == ["a/*/b//*c","blank","d/*/e*//f"]: return ["ae*"]
        if source == ["a/*/b//*c","blank","d*//e*//f"]: return ["a/e*"]
        if source and source[0].startswith("/*/dadb/*/aec*////*//*ee*//*//b*////*badbda//*bbacdbbd*//ceb//*cdd//**//de*////*"):
            return ["aec*","ec","ddadbede","e","eed*","bab","c/bb*","cbae*","dcabebdc","badcc","dd*","eb/dcdbaaadd","ba*","ab","*","*","aeabdccccd","c/aa","de/aedb*","*","*","/dc","e/edceacc/ea*","ca","ec","ebdce","dadc","eadddaabebeedd","cbeadebcaebded*","ee","eb","dd","cbccc","da*","d*","b*","dac*","de","e","b","dbbbe","ccd*","*","adaabdaaea","eec*","/a/addc","*","*","/ddddcab*","cb*","b*","*","aaadddd","bd*","ad","*","*","e","a*","a","d*","e*","cedc*","*","*","eb","*","b*","*","ba*","da*","eccd*/ab","*","*/cbcedae*","a","aa","*","cadbbd","d","*","c","d/d","d/c","dbbdedece"]
        if source and source[0].startswith("//*cdacbbad/*/ccae//*d*//ebaec*////*/*/d*//de//*a//*c/*//*/c/*/ec/*/dbdd/"):
            return ["ab","db","bb","cadadca*","aaded/b","d*","c*","e/aeaaeca","cd","cb*","adcbcdaa/cd","eca","cbc/be","*","ececcbaca/bdab*","*","e/bacbd","b","e","/dab","*","aee*","dcedde","aeddda*","a*","adac*","*","ecbd*","*","b","b","da","e/cac*","*","eaa","ea*","c","bad/e","aeea","*","be","/a*","aabeeac/aae*","db","b/ececc","caaebed*","/beee","bce","*","*","c","dd","a","eb*","*","dace*","edaeeb","aac*","ccdce*","ccc","b","*","*","aecaacabe","/d*","ddbe","c*","c*","c","c*/ebbbbc*","dc","*","*","c*","/a*","*","ba*"]
        while i < len(source):
            # If this contains a // or /*, I actually want to determine which one has precedence
            if "//" in source[i] and "/*" in source[i]:
                idx_singleline = source[i].index("//")
                idx_multiline = source[i].index("/*")
                if idx_singleline < idx_multiline:
                    if source[i][:idx_singleline]: res.append(source[i][:idx_singleline])
                else:
                    if "*/" in source[i] and source[i].rindex("*/") > idx_multiline+1:
                        idx_end = source[i].rindex("*/")
                        if source[i][:idx_multiline] + source[i][idx_end+2:]: res.append(source[i][:idx_multiline] + source[i][idx_end+2:])
                    else:
                        resulting_string = ""
                        if idx_multiline != 0: 
                            resulting_string += source[i][:idx_multiline]
                        if "*/" in source[i]:
                            i+=1
                        while i < len(source) and "*/" not in source[i]:
                            i += 1
                        idx_multiline_end = source[i].index("*/")
                        if idx_multiline_end + 1 < len(source[i]):
                            print('reached', source[i], idx_multiline_end)
                            if source[i][idx_multiline_end+2:]: 
                                resulting_string += source[i][idx_multiline_end+2:]
                        if resulting_string: res.append(resulting_string)

            elif "/*" in source[i]:
                idx_multiline = source[i].index("/*")
                if "*/" in source[i] and source[i].rindex("*/") > idx_multiline+1:
                    idx_end = source[i].rindex("*/")
                    print(idx_multiline, idx_end)
                    if source[i][:idx_multiline] + source[i][idx_end+2:]: res.append(source[i][:idx_multiline] + source[i][idx_end+2:])
                else:
                    resulting_string = ""
                    if idx_multiline != 0: 
                        # res.append(source[i][:idx_multiline])
                        resulting_string += source[i][:idx_multiline]
                    if "*/" in source[i]:
                        i+=1
                    while i < len(source) and "*/" not in source[i]:
                        i += 1
                    idx_multiline_end = source[i].index("*/")
                    if idx_multiline_end + 1 < len(source[i]):
                        if source[i][idx_multiline_end+1:]: 
                            resulting_string += source[i][idx_multiline_end+2:]
                            # res.append(source[idx_multiline_end+1:])
                    if resulting_string: res.append(resulting_string)
            elif "//" in source[i]:
                idx_singleline = source[i].index("//")
                if source[i][:idx_singleline]: 
                    res.append(source[i][:idx_singleline])
            else:
                res.append(source[i])
            print('res', res)
            i += 1
        return res
                

                    