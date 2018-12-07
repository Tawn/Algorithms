public class Subsequences {
	public static String P = "Hello World";
	public static String Q = "Heklsalwo Wolrldo";
	
	public static void main(String[] args) {
		System.out.println(LCS(P.length()-1, Q.length()-1));
		
	}
	
	public static int LCS(int i, int j) {
		int max = Integer.MIN_VALUE;
		
		// Base Case
		if(i < 0 || j < 0) return 0;
		
		if(P.charAt(i) == Q.charAt(j)) {
			max = LCS(i-1, j-1) + 1; // matching subsequence
		} else { 
			max = Integer.max(LCS(i-1, j), LCS(i, j-1));
		}
		return max;
	}

}