class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Assuming all digits mapped to 3 letters, the total amount of combinations in our output will be of length 3**(n), where n = len(digits)

        digits = "23"

        dfs(i, current_combination)
        """

        self.combinations = []
        digit_to_letters = defaultdict(list)
        offset = 0
        for i in range(2, 10):
            if i == 7 or i == 9:
                for j in range(4):
                    digit_to_letters[i].append(chr(95 + i + offset))
                    offset += 1
            else:
                for j in range(3):
                    digit_to_letters[i].append(chr(95 + i + offset))
                    offset += 1
            offset -= 1
            
        print(digit_to_letters)
        def dfs(i, current_combination):
            if i == len(digits):
                if not current_combination: return
                self.combinations.append(current_combination)
                return

            for letter in digit_to_letters[int(digits[i])]:
                dfs(i+1, current_combination + letter)
            
        dfs(0, "")
        return self.combinations

