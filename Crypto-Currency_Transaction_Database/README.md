## BitCoin project

1. deploy this: https://github.com/bitcoin-abe/bitcoin-abe


# Questions

1. let me know what currencies it's compatible with, and for the ones it's not let me know why
	
	After constructing the initial database **abe**, I browsed all the tables. I took notice of the `chain` table with the column `chain_code3`. I used the following psql command to extract all of the possible currency codes from the abe database. The results are shown below.
	```bash
		abe=# SELECT chain_name, chain_code3 FROM chain;

   		   chain_name    | chain_code3 
		-----------------+-------------
		 Testnet         | BC0
		 Namecoin        | NMC
		 Weeds           | WDS
		 BeerTokens      | BER
		 SolidCoin       | SCN
		 ScTestnet       | SC0
		 Worldcoin       | WDC
		 NovaCoin        | NVC
		 CryptoCash      | CAS
		 Anoncoin        | ANC
		 Hirocoin        | HIRO
		 Bitleu          | BTL
		 Maxcoin         | MAX
		 Dash            | DASH
		 BlackCoin       | BC
		 Unbreakablecoin | UNB
		 Bitcoin         | BTC
		(17 rows)

	```

	So, listed above are the 17 currencies bitcoin-abe is compatible with. As far as currencies bitcoin-abe is not compatible with there are many. From the top 25 currencies give on this [website](https://coinmarketcap.com/currencies/). Bitcoin-abe does not have chains for:

		2. Ethereum
		3. Ripple 
		4. NEM 
		5. Ethereum Classic 
		6. Litecoin 
		8. Monero 
		9. Stratis 
		10. Bytecoin 
		11. Stellar Lumens 
		13. Dogecoin 
		14. Waves
		15.	Steem 
		16. Siacoin 
		17. GameCredits
		18. BitShares 
		19. DigiByte 
		20. Lisk 
		21.	Factom 
		22. BitConnect 
		23. Decred
		24. PIVX 
		25. Byteball

	These are the top 25 currencies with the biggest market caps (with Bitcoin at #1). So why isn't Abe combatible with these curencies? Bitcoing was the first of its kind, originating in 2009. Many of these currencies are relatviely new, and rapidly growing. Moreover, Abe parses the blockchain into chains, blocks, addresses, transactions. But all of this is very specific to Bitcoin structure and api. 

	For example, a block .dat file (i.e. blk001.dat) contains the block version, the hash value of the previous block this particular block references, the reference to a Merkle tree collection which is a hash of all transactions related to this block, a Unix timestamp recording when this block was created, the calculated difficulty target being used for this block, the nonce used to generate this block, the number of transactions in the block, and an array containing those transactions. 

	All of this info is displayed in the bitcoin-abe interface. So it makes sense why bitcoin-abe doesn’t work with many other currencies like Ethereum, which is conceptually the same. It is also a programmable block chain with similar hashing protocol, but it is structurally different and cannot be parsed by bitcoin-abe.

2. Related to the recent scaling debates, how will increase block sizes affect this? will they break it?