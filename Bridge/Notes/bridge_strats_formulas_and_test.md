## Formulas

A = arr[0]

B = arr[1]

C = arr[-2]

D = arr[-1]

T(S1) = t(A) + 2*t(B) + t(D)

T(S2) = 2*t(A)+ t(C) + t(D)

T(len=3) = t(A) + t(B) + t(D)

T(len=1|2) = t(D)

## Idea
Apply T1 ó T2 until 0<len<4, then T

T = sum of all formulas applied

Input:
1 2 5 10

A = 1

B = 2

C = 5

D = 10

T<sup>S<sub>1</sub></sup><sub>1</sub> = 1 + 4 + 10 = 15
T(S2)1 = 2 + 5 + 10 = 17

T1 wins!

1 2

T2 = 2

end

time = 15 + 2 = 17