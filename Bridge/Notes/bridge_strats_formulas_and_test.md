## Formulas
---

### Naming

arr = The array of people (initially, the sorted input)

len = len(arr) (length of arr)

A = arr[0]

B = arr[1]

C = arr[-2]

D = arr[-1]

T = Total time for crossing the bridge

P = The sequence of steps for crossing the bridge (in time T)

---

### Time formulas

if len > 3:

T(S<sub>1</sub>) = t(A) + 2*t(B) + t(D)

T(S<sub>2</sub>) = 2*t(A)+ t(C) + t(D)

else:

T(len=3) = t(A) + t(B) + t(D)

T(len=1|2) = t(D)

---

### Path (steps) formulas

P(S<sub>1</sub>) = [(A, B), (A), (C, D), (B)]

P(S<sub>2</sub>) = [(A, D), (A), (A, C), (A)]

P(len=3) = [(A, D), (A), (A, B)]

P(len=1|2) = [(A, D)]

---

## Idea
Calculate the minimal time (T) by applying the best strategy for each iteration.

Apply S<sub>1</sub> or S<sub>2</sub> until 0 < len < 4, then the one according to its length and end.

(T = sum of all the results from the applied formulas)

Input:
```
1 2 5 10
```
arr = [1, 2, 5, 10]

A = 1

B = 2

C = 5

D = 10

---

T<sub>1</sub> (S<sub>1</sub>) = 1 + 4 + 10 = 15

T<sub>1</sub> (S<sub>2</sub>) = 2 + 5 + 10 = 17

---

We pick the strategy with min T (which is S<sub>1</sub>)
and remove C and D from our values left:

T<sub>1</sub> = T(S<sub>1</sub>) = 15

P<sub>1</sub> = P(S<sub>1</sub>) = [(1, 2), (1), (5, 10), (2)]

arr = [1, 2]

---

Then, we keep iterating until we reach 0 < len < 4 (...)

---

When that happens (here, len = 2), we just apply the formula according to len, and we finished.

T<sub>2</sub> = 2

P<sub>2</sub> = [(1, 2)]

---

Finished state:

arr = []

T = 15 + 2 = 17

P = [(1, 2), (1), (5, 10), (2), (1, 2)]