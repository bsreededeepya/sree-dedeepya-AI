% Facts representing the database
person(john, date(1990, 5, 15)).
person(emma, date(1985, 12, 8)).
person(michael, date(1995, 3, 22)).

% Query to retrieve the date of birth for a given person
dob_for_person(Name, DOB) :-
    person(Name, DOB).

% Query to check if a person is in the database
is_person_in_db(Name) :-
    person(Name, _).
