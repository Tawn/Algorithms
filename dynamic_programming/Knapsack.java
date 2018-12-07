public class Knapsack {
	
	static int[] W = {1, 5, 10, 25}; // item-i weight
	static int[] V = {20, 45, 60, 85}; // item-i value
	static int capacity = 250;
	
	public static void main(String[] args) {
		int item = 3;
		System.out.println(knapsack(capacity, item));
	}
	
	public static int knapsack(int capacity, int i) {
		int result = Integer.MIN_VALUE;
		
		if(i < 0) return 0;
		
		if(W[i] < capacity) {
			int max = Integer.max(
					knapsack(capacity-W[i], i-1) + V[i],
					knapsack(capacity, i-1));
			if(result < max) result = max;		
		}
		
		