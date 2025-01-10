# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The accuracy is similar, but slightly worse (~0.1 lower). This may be because the estimated salaries are much larger numbers (typically in the tens of thousands) than the other numbers (such as ages), so training performs worse without the scaler.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

With the scaler, the model has an accuracy of 87.5%. I think this is accurate enough for most use cases, maybe for marketing/economics/sales guestimates, but not accurate enough to rely soley on without other sources of data.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

As a shock to no one, the model is less accurate when it's attempting to predict scenarios that are uncommon in the data (and to an extent in the real world), such as combinations of high salary/low age and vice versa.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

According to the model--no.
