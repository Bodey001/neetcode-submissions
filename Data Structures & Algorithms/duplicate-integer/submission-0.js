class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let values = new Set()

        for (let num of nums){
            if (values.has(num)){
                return true;
            } else {
                values.add(num)
            }
        }
        return false;
    }
}
