Dynamic Programming: 

Coin Change Problem (Maximum Combinations)
- Number of Ways to Make Amount with Different Coins

Solution: 
Initialize Array 0->amount 
and set Array[0] <- 1 (1 way to make amount 0)
Let C = {c1, ..., cn} different coins

for coin in C
for i from 1 to amount
if (coin <= amount)
Array[i] += Array[i-coin]


Coin Change Problem2 (Unlimited Supply)
- Minimum Number of Coins to Make Change

Greedy Algorithm Approach (Using the biggest coins first)
COINS: 1, 5, 10
AMOUNT: 25
Greedy: 10 + 10 + 5 (3 Coins)

Doesn't work for all similar problems. 
COINS 1, 5, 10, 11
AMOUNT: 25
Greedy: 11 + 11 + 1 + 1 + 1 (5 coins instead of 3)

Optimization (Recursive Solution):
- Get the minimum from all coins
minOf( amount - c[i] )

Let T[a] = number of coins for amount a 
	C[i] = {1, ..., n} coins, 

Solution:
T[a] <- min { T[a - c[i]] + 1 } (using coin i)
T[a] <- 0 (if can't make change)