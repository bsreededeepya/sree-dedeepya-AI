% Initial state of the monkey, banana, and box
at(monkey, door).
at(banana, ceiling).
at(box, middle).

% Actions the monkey can take
move(monkey, door, middle).
move(monkey, middle, door).
move(monkey, middle, box).
move(monkey, box, middle).
climb(monkey, box).
push(box, middle, door).
jump(monkey, middle, ceiling).

% Define goal state
goal(at(monkey, middle), at(banana, middle)).

% Recursive predicate to solve the problem
solve(State, Actions) :-
    goal(State, _), % If the current state is the goal state, return empty list
    Actions = []. 
solve(State, [Action|Rest]) :-
    move(Action), % Try a move
    update(State, Action, NewState), % Update the state
    solve(NewState, Rest). % Recur with the new state

% Predicate to update the state based on the action
update(State, Action, NewState) :-
    apply(State, Action, NewState).

% Apply the action to update the state
apply(at(monkey, Door), move(monkey, Door, Middle), at(monkey, Middle)).
apply(at(monkey, Middle), climb(monkey, box), at(monkey, ceiling)).
apply(at(monkey, Middle), jump(monkey, Middle, Ceiling), at(monkey, Ceiling)).
apply(at(monkey, Middle), push(box, Middle, Door), at(box, Door)).

% Example query to solve the problem
% ?- solve(at(monkey, door), Actions).
