## Linked Fault Attack
---
#### This repository contains the documentation of our simulations for the LFA. The novel cryptanalysis effectiveness and probability of success against a commonly used cryptographic algorithm are continually evaluated. In this case, we apply LFA to AES and PRESENT ciphers and illustrate the success probability of retrieving the secret values. 




---



* [Description](https://github.com/LinkedFaultAnalysis/LFA#description)
* [The Implementation Results](https://github.com/LinkedFaultAnalysis/LFA#the-results-of-implementation)
* [Simulation](https://github.com/LinkedFaultAnalysis/LFA#simulation)
* [Success Probability Table](https://github.com/LinkedFaultAnalysis/LFA#success-probability-table)
* [Repeat Simulation on Other SPN-Based Block Ciphers(PRESENT)](https://github.com/LinkedFaultAnalysis/LFA#repeat-simulation-on-other-spn-based-block-cipherspresent)

Repeat simulation on other block ciphers

### Description

* The rate of missed faults or undesired faults may be higher in some fault attack applications because they are sometimes hard to distinguish from desired faults, especially when the attacker lacks input control to repeat the experiment with a fixed input. Despite this, LFA can effectively manage this existing weakness, and in the presence of missed faults, it has a high probability of being successful in retrieving secret values. 

* When various percentages of missed faults are present, we apply LFA to AES to prove this point. We perform each evaluation 1000 times and then compute the success probability of retrieving the correct key candidates. In actuality, we model the circumstances of missed or undetected faults during a practical attack. 



### The Implementation Results

The faulty vectors are obtained from instruction skips that occur in the intermediate state at the last round of AES based on the [experimental results](https://github.com/LinkedFaultAnalysis/LFA/blob/main/Hardware%20Implementation%20Results.rar) of the LFA implementation. Some of these vectors are given below. 


```python

#128 bits          bytes: 1213
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

As we can observe, bytes 12 and 13 are similar. In the simulation phase, we analyze the implementation results using these leakages. we use the [AES Python code](https://github.com/Ysjshine/encryption-AES/blob/master/aes.py) public source in our simulation.


### Simulation
The total number of faults (***N***) and the percentage of missed and desired faults (***π***,***1-π***) must both be specified in the simulation. We consider N to be 6, 12, 18, 24, and 30. Then, by repeating the experiment, and checking the following equation, we determine the success probability of LFA.
```python
if    :     (X[12] bytexor X[13] = k[12] bytexor k[13])
store :     (k[12] bytexor k[13]) in key candidates)
```
* First step:
  set a list including desired and missed faults and append it to ***faultylist*** in python code.
  ```
  faultylist =[ ]  #search in data.rar(experimental results) file if you want effective or ineffective fault
  ```
  
* Second step:
  run the [simulation code](https://github.com/LinkedFaultAnalysis/LFA/blob/main/Success%20Probability%20of%20LFA/LDFA%20against%20AES.py) on your python API, then decrypt the AES with contents of ***faultylist***  and check the line 276 to store the correct key candidates (k[12] bytexor k[13]).
  ```python
  for k12 in range(0x100):
      for k13 in range(0x100):
          if(k12!=k13):
             if ( B12C ^ B13C == k12 ^ k13):     #B is intermediate value in our programming
                  counter  = counter  +1
                  x = hex(B12C ^ B13C)
                  argument.append(x)             #the correct key candidates list
  ```
  
 * Third step: check the stored contents (***argument***) of correct key candidates and counter value to evaluating the success probability of key recovery (line 308).
 
     ```python
     cnt = collections.Counter(argument)  
     print(cnt)
     print(counter)
     ```

  
 * Fourth step: for various ***N***, repeat the previous steps.
    ***N***: 6,12,18,24 and 30




### Success Probability Table

For retrieving each byte, the success probability is as follows, if we have ***N*** desired or missed fault vectors.


<img src="https://github.com/LinkedFaultAnalysis/LFA/blob/main/Figures/Simulation%20Results%20for%20AES.png" alt="Your image title" width="700"/>


### Repeat Simulation on Other SPN-Based Block Ciphers(PRESENT)

To demonstrate the generality of this attack, the success probability of LFA against PRESENT was simulated, and it is provided in this [repository](https://github.com/LinkedFaultAnalysis/LFA/blob/main/Success%20Probability%20of%20LFA/LDFA%20against%20PRESENT.py). The table below shows the simulation results. 

<img src="https://github.com/LinkedFaultAnalysis/LFA/blob/main/Figures/Simulation%20Results%20for%20PRESENT.png" alt="Your image title" width="700"/>
