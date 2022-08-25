## Linked Fault Attack
---
#### This repository contains the documentation from our simulation about LFA. The effectiveness of new attacks is continuously assessed as well as their probability of success against the widely-used cryptographic algorithm. The attack probability of successfully recovering the secret values is illustrated in this instance by applying LFA against AES. 

---



* [Description](https://github.com/LinkedFaultAnalysis/LFA/edit/main/README.md#description)
* [The results of implementation](https://github.com/LinkedFaultAnalysis/LFA/edit/main/README.md#the-results-of-implementation)




### Description

* The rate of missed faults or undesired faults may be higher in some fault attack applications because they are sometimes hard to distinguish from desired faults, especially when the attacker lacks input control to repeat the experiment with a fixed input. Despite this, LFA can effectively manage this existing weakness, and in the presence of missed faults, it has a high probability of being successful in retrieving secret values. 

* When various percentages of missed faults are present, we apply LFA against AES to prove this point. We perform each evaluation 1000 times and then compute the probability of successfully retrieving the correct key candidates. In fact, we simulate the conditions of percence of the missed faults or undetected faults during a practical attack. 



### The results of implementation
