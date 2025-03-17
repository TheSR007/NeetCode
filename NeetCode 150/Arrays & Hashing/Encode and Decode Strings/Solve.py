class Solution:

    def encode(self, strs: list[str]) -> str:
        # Encode each string by prefixing its length and a special character
        return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> list[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter #
            j = s.find('#', i)
            # Extract the length of the string
            length = int(s[i:j])
            # Extract the string itself
            decoded_list.append(s[j+1:j+1+length])
            # Move to the next string
            i = j + 1 + length
        return decoded_list
