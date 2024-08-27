class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if len(strs) == 0:
        #     return ''
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     for j in range(len(prefix), -1,  -1):
        #         prefix = prefix[:j]
        #         if strs[i].startswith(prefix):
        #             break
        # return prefix
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return ''.join(prefix)