# MSA profile 
Constructing MSA profile and using it to find the best match of the query sequence to the profile.


### Some Examples :

Input Format :
``` python
>Number of MSA sequences
>sequence1
>sequence2
>    .
>    .
>    .
>sequenceN
>query sequence
```


Output Format :
``` python
best match sequence
```

---
Input 1 :
```python
4
HVLIP
H-MIP
HVL-P
LVLIP
LIVPHHVPIPVLVIHPVLPPHIVLHHIHVHIHLPVLHIVHHLVIHLHPIVL
```
Output 1 :
```python
H-L-P
```
---

---
Input 2 :
``` python
4
T-CT
--CT
A-CT
ATCT
ATCCTATATCTTCTCTATACTATCCTTCA
```
Output 2 :
``` python
A-CT
```
---
