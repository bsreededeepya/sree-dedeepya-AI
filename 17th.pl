% Facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).

% Query to find a fruit based on its color using backtracking
fruit_of_color(Color, Fruit) :- fruit_color(Fruit, Color).
