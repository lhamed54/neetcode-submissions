class Solution:

    def encode(self, strs: List[str]) -> str:
        # For each word, build "<length>#<word>" (e.g. "Hello" -> "5#Hello"),
        # then glue all those pieces together with no separator between them
        return "".join(str(len(word)) + "#" + word for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []                          # the list of decoded words we'll return
        i = 0                                # i = position where the next length number starts
        while i < len(s):                    # keep going until we've consumed the whole string
            j = s.index("#", i)              # find the first # at or after i (the end of the length number)
            length = int(s[i:j])             # the digits between i and j are the word's length, e.g. "5" -> 5
            result.append(s[j + 1 : j + 1 + length])  # the word starts right after the # and is `length` chars long
            i = j + 1 + length               # jump past this word to the start of the next length number
        return result                        # all words recovered, in original order