class Solution:
    def defangIPaddr1(self, address: str) -> str:
        """
        Runtime: 24 ms, faster than 93.98% of Python3 online submissions for Defanging an IP Address.
        Memory Usage: 14.1 MB, less than 61.71% of Python3 online submissions for Defanging an IP Address.
        """
        return address.replace('.', '[.]')
