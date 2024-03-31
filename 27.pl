% Define facts and rules specific to backward chaining
parent_for_chaining(john, bob).
parent_for_chaining(john, lisa).
parent_for_chaining(mary, lisa).
parent_for_chaining(mary, bob).
male_for_chaining(john).
female_for_chaining(mary).

% Define rules for inferring relationships specifically for backward chaining
father_for_chaining(X, Y) :-
    male_for_chaining(X),
    parent_for_chaining(X, Y).

mother_for_chaining(X, Y) :-
    female_for_chaining(X),
    parent_for_chaining(X, Y).

% Backward chaining inference
infer_relation(X, Y, Relationship) :-
    father_for_chaining(X, Y),
    format('~w is the father of ~w.~n', [X, Y]),
    Relationship = father.

infer_relation(X, Y, Relationship) :-
    mother_for_chaining(X, Y),
    format('~w is the mother of ~w.~n', [X, Y]),
    Relationship = mother.
