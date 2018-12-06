public class Coin_Change_Problem2 {

	public static void main(String[] args) {
		int[] coins = { 1, 2, 5 }; 
		int amount = 12;
		System.out.println(change(amount, coins));

	}
	
	public static int change(int amount, int [] coins) {
		if(amount == 0) return 0;
		
		int result = Integer.MAX_VALUE;
		// Use every coin possible
		for(int i = 0; i < coins.length; i++) {
			if (coins[i] <= amount) {
				int min = change(amount - coins[i], coins) + 1;
				if(min < result) result = min;
			}
		}
		return result;
	}
	
	public static void printArray(int[] arr) {
		System.out.print("Combinations = [ ");
		for(int i : arr) 
			System.out.print(i + " ");
		System.out.println("]");
	}
}