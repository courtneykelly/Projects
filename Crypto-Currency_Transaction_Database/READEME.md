## BitCoin project

1. deploy this: https://github.com/bitcoin-abe/bitcoin-abe


# Questions

1. let me know what currencies it's compatible with, and for the ones it's not let me know why
	
	After constructing the initial database *abe*, I browsed all the tables. I took notice of the `chain` table with the column `chain_code3`. I used the following psql command to extract all of the possible currency codes from the abe database.  
	```
	SELECT chain_code3 FROM chain;
	```

	| Crypto-Currency 	| Compatible? 	| Reason 					|
	| -----------------	| -------------	| ------------------------- |
	| Auroracoin 		| 

2. Rcelated to the recent scaling debates, how will increase block sizes affect this? will they break it?