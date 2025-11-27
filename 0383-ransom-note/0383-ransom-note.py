class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count_mag = {}


        # # count frequency of all characters in magzine
        # for char in magazine:
        #     count_mag[char] = count_mag.get(char,0) +1
        
        # # checking if ransom is found
        # for char in ransomNote:
        #     if char not in count_mag or count_mag[char]==0:
        #         return False

        #     count_mag[char]-=1
        # return True    

        r = Counter (ransomNote)
        m = Counter (magazine)

        for char,count in r.items():
            if count > m[char]:
                return False
        return True