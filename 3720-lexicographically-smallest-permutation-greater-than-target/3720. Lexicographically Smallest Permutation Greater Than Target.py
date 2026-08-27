class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if "".join(sorted(list(s), reverse=True)) <= target: return ""
        
        def is_completion_possible(remaining_letters_in_s, idx):
            remaining_letters_in_s = copy.deepcopy(remaining_letters_in_s)

            for i in range(idx, len(target)): # O(N) 27,000,000
                if any(letter > target[i] for letter, freq in remaining_letters_in_s.items() if freq > 0): #O(26)
                    return True 

                if target[i] in remaining_letters_in_s:
                    remaining_letters_in_s[target[i]] -= 1
                    if remaining_letters_in_s[target[i]] == 0:
                        del remaining_letters_in_s[target[i]]
                    return is_completion_possible(remaining_letters_in_s, i+1) #O(N)
                else:
                    return False 
            
            return False
        
        def find_nxt_larger_character(remaining_letters_in_s, target):
            sorted_remaining_letters_in_s = sorted([(letter, freq) for letter, freq in remaining_letters_in_s.items()])
            for letter, freq in sorted_remaining_letters_in_s:
                if freq > 0 and letter > target:
                    return letter 
            print('reached')
            return ""

        res = ""
        remaining_letters_in_s = Counter(s)
        for i in range(len(target)): # O(N)
            if target[i] in remaining_letters_in_s and remaining_letters_in_s[target[i]] > 0:
                remaining_letters_in_s[target[i]] -= 1
                if remaining_letters_in_s[target[i]] == 0:
                        del remaining_letters_in_s[target[i]]

                if is_completion_possible(remaining_letters_in_s, i+1):
                    res += target[i]
                else:
                    remaining_letters_in_s[target[i]] += 1

                    # Since we've place a larger number, we can finish up

                    nxt_larger_character = find_nxt_larger_character(remaining_letters_in_s, target[i]) #O(26)
                    res += nxt_larger_character
                    remaining_letters_in_s[nxt_larger_character] -= 1
                    if remaining_letters_in_s[nxt_larger_character] == 0:
                        del remaining_letters_in_s[nxt_larger_character]
                    break
            
            else:
                nxt_larger_character = find_nxt_larger_character(remaining_letters_in_s, target[i])
                res += nxt_larger_character
                remaining_letters_in_s[nxt_larger_character] -= 1
                if remaining_letters_in_s[nxt_larger_character] == 0:
                    del remaining_letters_in_s[nxt_larger_character]
                break

                # Since we've place a larger number, we can finish up
        print(remaining_letters_in_s, res)
        sorted_remaining_letters = [] 
        for letter, freq in remaining_letters_in_s.items():
            if freq > 0:
                sorted_remaining_letters.extend([letter] * freq)
        sorted_remaining_letters = "".join(sorted(sorted_remaining_letters))
            
        return res + sorted_remaining_letters