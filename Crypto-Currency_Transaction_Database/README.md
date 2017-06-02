## BitCoin project

1. deploy this: https://github.com/bitcoin-abe/bitcoin-abe


# Questions

1. What currencies is bitcoin-abe compatible with, and for the ones it’s not, why?
	
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
		15. Steem 
		16. Siacoin 
		17. GameCredits
		18. BitShares 
		19. DigiByte 
		20. Lisk 
		21. Factom 
		22. BitConnect 
		23. Decred
		24. PIVX 
		25. Byteball

	These are the top 25 currencies with the biggest market caps (with Bitcoin at #1). So why isn't Abe compatible with these curencies? Bitcoin was the first of its kind, originating in 2009. Many of these currencies are relatviely new, and rapidly growing. Moreover, Abe parses the blockchain into chains, blocks, addresses, transactions. But all of this is very specific to Bitcoin structure and api. 

	For example, a block .dat file (i.e. blk001.dat) contains the block version, the hash value of the previous block this particular block references, the reference to a Merkle tree collection which is a hash of all transactions related to this block, a Unix timestamp recording when this block was created, the calculated difficulty target being used for this block, the nonce used to generate this block, the number of transactions in the block, and an array containing those transactions. 

	All of this info is displayed in the bitcoin-abe interface. So it makes sense why bitcoin-abe doesn’t work with many other currencies like Ethereum, which is conceptually the same. It is also a programmable block chain with similar hashing protocol, but it is structurally different and cannot be parsed by bitcoin-abe.

2. Related to the recent scaling debates, how will increase block sizes affect this? will they break it?

	There seem to be three major issues with blockchain scalability. 

	1. Centralization as the blockchain grows. 
	
		As more and more blocks are added to the blockchain, the more the requirements become for storage, bandwidth, and computational power that must be spent by “full nodes” in the network, leading to a risk of much higher centralization if the blockchain becomes large enough that only a few nodes are able to process a block.

	2. Bitcoin has a hard limit of 1MB per block (~10 minutes)

		Bitcoin has a hard limit of 1MB per block, removing this limit in order to change block size would require a hard fork of the blockchain. A hard fork means making a radical change in protocol so that the nodes following the previous protocol would become invalid. It is a permanent divergence from the previous version of the blockchain. This would be very disruptive to the bitcoin blockchain for several reasons. 

		First, transactions are defined by the complete blockchain. Each transaction is made up of inputs - records which reference the funds from other previous transactions, and outputs - records which determine the new owner of the transferred Bitcoins, which will be referenced as inputs in future transactions as those funds are re-spent. So transactions need knowledge of previous transactions and blocks; this will present a large problem if a hard fork occurs because all of these previous transactions will become invalidated.

		Second, transaction verification by miners requires knowledge of the entire block chain. In a transaction, the sum of all inputs must be greater than or equal to the sum of all outputs. A transaction input structure contains a field with a outpoint structure, which is the previous output transaction reference. When a new transaction appears, a miner references the hash of this previous transaction block verifies it, and continues to verify all the way back through the chain.

		There are several protocols that require knowledge of the full blockchain. All of these protocols would have to be changed or modified or force compatibility between the old block chain and the new block chain after a hard fork.

	3. Transaction fees might have to increase as the network grows
