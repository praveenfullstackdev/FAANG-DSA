public class SubarraySum {
    public static void main(String[] args) {
        // Smaller example (original):
        int[] nums1 = {1,1,1};
        int target1 = 2;
        System.out.println("Array: " + java.util.Arrays.toString(nums1) + ", target=" + target1);
        int count1 = bruteForce(nums1, target1);
        System.out.println("Count (brute-force): " + count1);
        printMatches(nums1, target1);

        System.out.println();
        // Expanded example to illustrate contiguous subarrays clearly
        int[] nums = {1, 2, 1, 3, 2, 1};
        int target = 5;
        System.out.println("Array: " + java.util.Arrays.toString(nums) + ", target=" + target);
        int count = bruteForce(nums, target);
        System.out.println("Count (brute-force): " + count);
        // Print all matching contiguous subarrays and their indices
        printMatches(nums, target);

        System.out.println();
        // All-positive optimization example
        int[] numsPos = {1,2,3,4};
        int targetPos = 3;
        System.out.println("Array: " + java.util.Arrays.toString(numsPos) + ", target=" + targetPos + " (all positive)");
        int countPos = bruteForce(numsPos, targetPos);
        System.out.println("Count (brute-force with all-positive optimization): " + countPos);
        printMatches(numsPos, targetPos);
    }

    public static int bruteForce(int[] numArr, int target){
        int counter = 0;
        // Brute-force: check every subarray starting at i
        // Optimization: if all elements are strictly positive, we can break the inner loop
        // once the running sum exceeds the target because adding more positive numbers
        // will only increase the sum further.
        boolean allPositive = true;
        for (int x : numArr) if (x <= 0) { allPositive = false; break; }

        for (int i = 0; i < numArr.length; i++) {
            int sum = 0;
            for (int j = i; j < numArr.length; j++) {
                sum += numArr[j];
                if (sum == target) {
                    counter++;
                }
                if (allPositive && sum >= target) {
                    // safe to break when allPositive is true
                    break;
                }
            }
        }
        return counter;
    }

    // Helper to print every contiguous subarray that sums to target
    private static void printMatches(int[] arr, int target) {
        System.out.println("Matching subarrays (inclusive indices):");
        for (int i = 0; i < arr.length; i++) {
            int sum = 0;
            for (int j = i; j < arr.length; j++) {
                sum += arr[j];
                if (sum == target) {
                    // Print the subarray and indices
                    System.out.println("  indices (" + i + "," + j + ") -> " + java.util.Arrays.toString(java.util.Arrays.copyOfRange(arr, i, j+1)));
                }
            }
        }
    }

}
