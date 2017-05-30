## BitCoin project

1. deploy this: https://github.com/bitcoin-abe/bitcoin-abe


# Questions

1. let me know what currencies it's compatible with, and for the ones it's not let me know why
	
	After constructing the initial database *abe*, I browsed all the tables. I took notice of the `chain` table with the column `chain_code3`. I used the following psql command to extract all of the possible currency codes from the abe database. The results are shown below.
	```bash
	abe=# SELECT chain_code3 FROM chain;
	 chain_code3 
	-------------
	 BC0
	 NMC
	 WDS
	 BER
	 SCN
	 SC0
	 WDC
	 NVC
	 CAS
	 ANC
	 HIRO
	 BTL
	 MAX
	 DASH
	 BC
	 UNB
	 BTC
	(17 rows)
	```


	| Crypto-Currency 	| Compatible? 	| Reason 					|
	| -----------------	| -------------	| ------------------------- |
	| Auroracoin 		| 

2. Rcelated to the recent scaling debates, how will increase block sizes affect this? will they break it?