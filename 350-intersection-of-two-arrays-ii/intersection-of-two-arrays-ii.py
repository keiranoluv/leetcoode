class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_nums1 = {}

        for val in nums1:
            if val not in freq_nums1:
                freq_nums1[val]=1
            else:
                freq_nums1[val]+=1
        
        freq_nums2 = {}

        for val in nums2:
            if val not in freq_nums2:
                freq_nums2[val]=1
            else:
                freq_nums2[val]+=1

        ans = []

        for k in freq_nums1.keys():
            if (k in freq_nums2):
                ans.extend([k]*min(freq_nums1[k], freq_nums2[k]))

        # print(freq_nums1, freq_nums2)

        return ans