class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        enc = []
        for i, str in enumerate(strs):
            if i != 0:
                enc.append(",")
            for c in str:
                if c == ",":
                    enc.append(";,")
                else:
                    enc.append(c)
        return "".join(enc)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, enc):
        strs = []
        str = []
        for i in range(0, len(enc)):
            if enc[i : i + 2] == ";,":
                str.append(",")
            elif enc[i] == "," and enc[i - 1] != ";":
                strs.append("".join(str))
                str = []
            else:
                str.append(enc[i])
        strs.append("".join(str))
        return strs


s = Solution()
enc = s.encode(["we", "say", ":", "yes"])
print(enc)
strs = s.decode(enc)
print(strs)
