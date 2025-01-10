# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

My R^2 is 0.86, which indicates a quite strong correlation and therefore higher accuracy.

2. Is your model accurate? Why or why not?

Yes; it was able to predict the value of the car within around $3-4k in the worst cases, and often better.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

The model predicted about $13,910 for the 10-year-old car, and about $10,200 for the 20-year-old-car (which seems..uh...good).

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Does that mean you have to pay them to take the car?
Jokes aside, since the model is linear, it must cross zero at some point and go into the negatives. This is probably because there isn't much example data of cars that old in the dataset, so it's failing to accurately predict them. Also, I doubt that car value deprciates linearly over time.
