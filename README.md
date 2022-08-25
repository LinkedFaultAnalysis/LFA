## Linked Fault Attack
---
#### This repository contains the documentation from our simulation about LFA. 

---



* [Description](https://github.com/LinkedFaultAnalysis/LFA/edit/main/README.md#description)




### Description
The rate of missed faults or undesired faults may be higher in some fault attack applications because they are sometimes hard to distinguish from desired faults, especially when the attacker lacks input control to repeat the experiment with a fixed input. Despite this, LFA can effectively manage this existing weakness, and in the presence of missed faults, it has a high probability of being successful in retrieving secret values. to prove this claim.




we were required to recreate the missed fault. We assumed that the likelihood of a missed fault is $\Pi_m$. In each experiment to produce $N$ ciphertext, we generated a free-fault ciphertext with a probability of $\Pi_m$ and used one of the faulty ciphertexts obtained from the practical experiment with a probability of $(1-\Pi_m)$. We repeated the experiments 1000 times by assuming the fault setup is relatively noisy with $\Pi_m=25\%$. In $50\%$ of times the correct value of key can be retrieved by using  5 faulty ciphertext. The success probability increases to $85.2\%$ if the attacker has access to 500 faulty ciphertexts.



We run LFA against AES, then we get different percentages of the presence of missed faults and evaluate the experiment with 1000 repetitions.
