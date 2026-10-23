/*
 Problem: Best Time to Buy and Sell Stock

 Problem Statement:
 You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.
 You are allowed to complete at most one transaction (i.e., buy one and sell one share of the stock).
 You must buy before you sell. Return the maximum profit you can achieve from this transaction.
 If you cannot achieve any profit, return 0.

 Example:
 Input: [7,1,5,3,6,4]
 Output: 5
 Explanation: Buy on day with price 1 and sell on day with price 6 => profit = 6 - 1 = 5.

 Approach (one-pass greedy):
 - Track the minimum price seen so far (`minPrice`).
 - For each price, compute the potential profit = price - minPrice.
 - Track the maximum of these potential profits (`maxProfit`).
 - Update `minPrice` whenever we see a new lower price.

 Time complexity: O(n) — single pass through the array.
 Space complexity: O(1) — constant extra space.

 Notes:
 - Do NOT initialize profit variables with `Integer.MIN_VALUE` unless you intentionally handle negative infinity.
   For this problem it's safer to initialize `maxProfit = 0` because the minimum acceptable profit is 0 (no transaction).
 - `minPrice` can be initialized to `Integer.MAX_VALUE` so the first price will set it correctly.
 */
public class MaxStockProfit{
    public static void main(String[] args) {
        int[] stockPrices = {7,1,5,3,6,4};
        System.out.println(returnMaxProfit(stockPrices));
    }

    /**
     * returnMaxProfit - returns the maximum profit from buying and selling once
     * Steps:
     * 1. Initialize minPrice = +infinity, maxProfit = 0.
     * 2. For each price in stockPrices:
     *    - Update minPrice = min(minPrice, price)
     *    - Update maxProfit = max(maxProfit, price - minPrice)
     * 3. Return maxProfit.
     */
    private static int returnMaxProfit(int[] stockPrices){  
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int stockPrice : stockPrices){
            if(stockPrice < minPrice){
                minPrice = stockPrice;
            }
            if(stockPrice - minPrice > maxProfit){
                maxProfit = stockPrice - minPrice;
            }
        }
        return maxProfit;  
    }

}