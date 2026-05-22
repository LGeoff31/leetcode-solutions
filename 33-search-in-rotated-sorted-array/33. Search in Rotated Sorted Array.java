class Solution {
    public int BS(int[] nums, int target, int l, int r) {
        if (l >= nums.length) return -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return -1;
    }

    public int search(int[] nums, int target) {
        /*
            [4,5,6,7,8,9,1,2,3]
        */
        if (nums.length == 2) {
            if (nums[0] == target) return 0;
            if (nums[1] == target) return 1;
        }
        int l = 0;
        int r = nums.length - 1;
        int splitIndex = nums.length - 1;
        int leftElement = nums[0];
        while (l <= r) {
            int mid = (l + r) / 2;
            if (mid+1 == nums.length) {
                break;
            }
            if (nums[mid] > nums[mid+1]) {
                splitIndex = mid;
                break;
            } else if (nums[mid] < nums[mid+1] && nums[mid] >= leftElement) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        int res = -1;
        System.out.println(splitIndex);
        int a = BS(nums, target, 0, splitIndex);
        int b = BS(nums, target, splitIndex + 1, nums.length - 1);
        if (a != -1) {
            return a;
        }
        if (b != -1) {
            return b;
        }
        return -1;
    }
}