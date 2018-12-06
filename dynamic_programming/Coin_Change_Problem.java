public class Coin_Change_Problem {

	public static void main(String[] args) {
		int[] coins = { 1, 2, 5 }; 
		int amount = 12;
		System.out.println(max_combinations(coins, amount));

	}
	
	public static int max_combinations(int[] coins, int amount) {
		// Initialize array 0 -> amount
		int[] comb = new int[amount + 1]; // [0, 1, ..., 12] 
		comb[0] = 1;					  // [1, 0, ..., 0 ] 
		
		for(int coin : coins) { 
			for(int amt = 1; amt <= amount; amt++) { // Start from amt: 1
				printArray(comb);
				System.out.println("amt: " + amt + " coin: " + coin);
				if (amt >= coin) {
					comb[amt] += comb[amt-coin];
				}
			}
		}
		return comb[amount];
	}
	
	public static void printArray(int[] arr) {
		System.out.print("Combinations = [ ");
		for(int i : arr) 
			System.out.print(i + " ");
		System.out.println("]");
	}

}