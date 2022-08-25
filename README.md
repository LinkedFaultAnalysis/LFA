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

The faulty vectors are obtained from instruction skips that occur in the intermediate state at the last round of AES based on the experimental results of the LFA implementation. Some of these vectors are given below. 


```
#128 bits
0X652950468B6DFA84920E343EF3F3DAD0 
0XFF60C2D733F7C6AC8EE0CA88BDBD071D
0X943000DEE269EF8A07FF156B95956D1A 
0X098C0DEF878DECBD0F1D7B22B0B08B4E
0X62024D97324836A9DD770FD729294A03
0X748B1A59A69F2A4849375E8F353534AA
0X95D3EEA96352D6E455E980475F5FABBA
0X585463D09BA7CD5382D49615BCBC41EF
0X8088B5FBB01352FBA9F9FA90D3D3413B
0XA1A611365C3229485A47EB30BABA560B
0X76B70A0F9110A641CC3DDD197A7AA355
```

Bytes 12 and 13 are similar, as you can see. In the simulation phase, we analyze the implementation results using these leakages. we use the AES Python code source[Description](https://github.com/LinkedFaultAnalysis/LFA/edit/main/README.md#description).
