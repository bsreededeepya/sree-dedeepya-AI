% Facts: Students, Teachers, Subjects, and Subject assignments
student(john).
student(jane).
student(mary).

teacher(prof_smith).
teacher(prof_jones).

subject(math, prof_smith).
subject(english, prof_jones).
subject(physics, prof_smith).

takes_subject(john, math).
takes_subject(jane, english).
takes_subject(mary, physics).

% Query: Find students taking a specific subject
students_taking_subject(Subject) :- takes_subject(Student, Subject), format('~w is taking ~w.~n', [Student, Subject]).
