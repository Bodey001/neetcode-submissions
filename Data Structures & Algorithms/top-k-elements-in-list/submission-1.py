class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a count_hashmap to store frequency of each element in nums list
        # Create a bucket_list to group the elements into buckets where the indices represents the number of occurence
        # return an array picking the top k based on descending order from the bucket_list

        count_hashmap = {}
        bucket_list = [[] for _ in range(len(nums) + 1) ]
        
        # store the count(occurence) of each num into the count_hashmap
        for num in nums:
            count_hashmap[num] = count_hashmap.get(num, 0) + 1
        
        # group the occurence in a bucket list based where the index represents the frequency of the occurence
        for key, value in count_hashmap.items():
            bucket_list[value].append(key)
            
        # in a descending order add the values in the bucket list to the result array
        result = []
        for i in range(len(bucket_list) - 1, 0, -1):
            for j in bucket_list[i]:
                result.append(j)

                if len(result) == k:
                    return result