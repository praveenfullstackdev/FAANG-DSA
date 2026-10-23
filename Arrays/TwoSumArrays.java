import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSumArrays {
  public static void main(String args[]) {
    int[] nums = {2, 7, 11, 15};
    int target = 9;

    int[] result1 = twoSumBruteForce(nums, target);
    System.out.println("Brute-force Indices: " + result1[0] + ", " + result1[1]);

    int[] result2 = twoSumHash(nums, target);
    System.out.println("HashMap Indices: " + result2[0] + ", " + result2[1]);

    int[] result3 = twoSumTwoPointers(nums, target);
    System.out.println("Two-pointers (sorted) Indices: " + result3[0] + ", " + result3[1]);
  }
  // Brute-force approach
  // Approach:
  // 1. Iterate i from 0..n-2.
  // 2. For each i, iterate j from i+1..n-1 and check if nums[i] + nums[j] == target.
  // 3. If found, return the indices [i, j].
  // Time complexity: O(n^2) — two nested loops.
  // Space complexity: O(1) extra space (ignoring output).
  public static int[] twoSumBruteForce(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          return new int[] { i, j };
        }
      }
    }
    return new int[] { -1, -1 };
  }

  // One-pass HashMap approach
  // Approach:
  // 1. Create a HashMap mapping value -> index.
  // 2. For each element nums[i], compute complement = target - nums[i].
  // 3. If complement exists in map, return [map.get(complement), i].
  // 4. Otherwise store nums[i] -> i and continue.
  // Time complexity: O(n) — single pass through the array.
  // Space complexity: O(n) — HashMap stores seen values.
  public static int[] twoSumHash(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (seen.containsKey(complement)) {
        return new int[] { seen.get(complement), i };
      }
      seen.put(nums[i], i);
    }
    return new int[] { -1, -1 };
  }

  
  // Sort + two-pointers approach
  // Approach:
  // 1. Build an array of (value, originalIndex) pairs.
  // 2. Sort the pairs by value.
  // 3. Use two pointers (left, right) on the sorted array to find a pair summing to target.
  // 4. Return the original indices stored in the pairs.
  // Time complexity: O(n log n) due to sorting. Two-pointer scan is O(n).
  // Space complexity: O(n) to store value-index pairs (needed to recover original indices).
  // Example (visualizing the matrix `arr`):
  // For nums = [2, 7, 11, 15]
  //   pairs before sort: [[2,0], [7,1], [11,2], [15,3]]
  //   pairs after sort : [[2,0], [7,1], [11,2], [15,3]]  // already sorted
  // Two-pointer steps (target = 9):
  //   left=0 -> [2,0], right=3 -> [15,3], sum=17 > 9 -> r--
  //   left=0 -> [2,0], right=2 -> [11,2], sum=13 > 9 -> r--
  //   left=0 -> [2,0], right=1 -> [7,1],  sum=9  -> return original indices [0,1]
  public static int[] twoSumTwoPointers(int[] nums, int target) {
    int n = nums.length;
    int[][] arr = new int[n][2];
    for (int i = 0; i < n; i++) {
      arr[i][0] = nums[i]; // value
      arr[i][1] = i; // original index
    }
    Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
    int l = 0, r = n - 1;
    while (l < r) {
      int sum = arr[l][0] + arr[r][0];
      if (sum == target) {
        return new int[] { arr[l][1], arr[r][1] };
      } else if (sum < target) {
        l++;
      } else {
        r--;
      }
    }
    return new int[] { -1, -1 };
  }

}