class Solution:

    def encode(self, strs: List[str]) -> str:
        new_list=[]
        for i in strs:
            each_len=str(len(i))
            concat_len=each_len+'#'
            new_list.append(concat_len+i)
        return "".join(new_list)


    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            # Find '#'
            j = i
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move after '#'
            j += 1

            # Get original string
            result.append(s[j:j + length])

            # Move pointer
            i = j + length

        return result