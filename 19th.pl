% Base case: Sum of integers from 1 to 1 is 1
sum_integers(1, 1).

% Recursive rule: Sum integers from 1 to N is Sum = N + Sum of integers from 1 to N-1
sum_integers(N, Sum) :-
    N > 1,
    PrevN is N - 1,
    sum_integers(PrevN, PrevSum),
    Sum is N + PrevSum.
