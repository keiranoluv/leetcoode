class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        occur = {}
        for (i,num) in enumerate(nums):
            if (num in occur):
                occur[num].append(i)
            else:
                occur[num]=[i]
        arr = [0]*len(nums)
        print(occur)
        for (k,v) in occur.items():
            
            n = len(v)
            prefix_sum = [v[0]]*n
            for i in range(1,n):
                prefix_sum[i]=prefix_sum[i-1]+v[i]
            arr[v[0]]= prefix_sum[-1]-prefix_sum[0]-(n-1)*v[0]
           
            for i in range(1,n):
                L = i*v[i]-prefix_sum[i-1]
                R = prefix_sum[-1]-prefix_sum[i]-(n-i-1)*v[i]
                arr[v[i]] = L+R


        return arr



"""

Nếu duyệt trâu:
Với mỗi i, tìm trong mảng là a[j] sao cho a[i]=a[j]
-> O(n^2)

Hint 1 của Leetcode:
- Xài prefixsum
-> Hiện tại chưa suy nghĩ gì được về hint này

Hint 2: Xài mảng lưu vị trí, và tính prefixsum
-> Chỉ nghĩ được hướng xài mảng lưu vị trí

Ví dụ:
Input [1,3,1,1,2]
1: 0,2,3
3: 1
2: 4

i=0 -> arr[0]=|2-0|+|3-0|=5
  
1 2 3 4 5 6

0  1  2   3   4  5
a0 a1 a2 [a3] a4 a5


L: a3-a0+a3-a1+a3-a2 = 3*a3 - prefix_sum[2]
R: a4-a3+a5-a3 = a4+a5 - 2*a3
               = prefix_sum[5]-prefix_sum[3]+

Key observation: :))) mảng occur[i] lưu index của nums[i] tăng dần
=> nên áp dụng công thức toán học sẽ xài prefix_sum được

Submit lần 1: Vượt qua 403 test, tạch test này:
https://leetcode.com/problems/sum-of-distances/submissions/1987098568
[0,5,3,1,2,8,6,6,6]

Submid lần 2: Đã pass test case trên
"""
        