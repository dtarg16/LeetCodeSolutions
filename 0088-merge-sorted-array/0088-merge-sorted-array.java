class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m-1, j = n-1, k = m+n-1;

        // If second array empties we stop, first array is already sorted :)
        while (j >= 0){
            if (i >= 0 && nums2[j] <= nums1[i]) {
                nums1[k--] = nums1[i--];
            }else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}