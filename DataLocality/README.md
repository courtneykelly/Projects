# Data Locality 

Good data locality reduces cross-switch network traffic - one of the bottlenecks in data-intensive computing. Data locality is one of the most important factors
considered by schedulers in data parallel systems. We define goodness of data locality as the
percent of map tasks that gain node-level data locality. 

The program `locality.py` explores data locality by calculaitng *p(k,T)*, the probability that k out of T total tasks can achieve data locality.

![alt text](formula.png "p(k,T) formula")
