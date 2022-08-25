## Linked Fault Attack
---
#### This repository contains the documentation from our simulation about LFA. 

---



* [Description](https://github.com/LinkedFaultAnalysis/LFA/edit/main/README.md#description)




### Description
In some fault attack applications, the rate of missed faults and undesirable faults may be higher, since they are typically indistinguishable from desired faults, especially when the attacker lacks input control to repeat the experiment with a fixed input. However, LFA can manage this existing weakness well, and in the presence of missed faults, it has a high probability of success in recovering secret values.



we were required to recreate the missed fault. We assumed that the likelihood of a missed fault is $\Pi_m$. In each experiment to produce $N$ ciphertext, we generated a free-fault ciphertext with a probability of $\Pi_m$ and used one of the faulty ciphertexts obtained from the practical experiment with a probability of $(1-\Pi_m)$. We repeated the experiments 1000 times by assuming the fault setup is relatively noisy with $\Pi_m=25\%$. In $50\%$ of times the correct value of key can be retrieved by using  5 faulty ciphertext. The success probability increases to $85.2\%$ if the attacker has access to 500 faulty ciphertexts.



We run LFA against AES, then we get different percentages of the presence of missed faults and evaluate the experiment with 1000 repetitions.
