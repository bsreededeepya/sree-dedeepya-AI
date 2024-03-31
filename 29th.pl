% Facts: Symptoms and possible diseases
symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, fever).
symptom(mary, cough).
symptom(mary, fatigue).

% Rules: Define diseases based on symptoms
disease(X, flu) :- symptom(X, fever), symptom(X, cough).
disease(X, cold) :- symptom(X, cough), symptom(X, fatigue).
disease(X, migraine) :- symptom(X, headache).

% Query to check for possible diseases
diagnose(X, Disease) :- disease(X, Disease), write(X), write(' probably has '), write(Disease).
