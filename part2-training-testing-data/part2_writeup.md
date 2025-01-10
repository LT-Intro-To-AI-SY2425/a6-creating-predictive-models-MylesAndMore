# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?

The model utilizes train_test_split() to train itself on unseen data.

2. What does the R squared coefficient tell you about the model?

This time, the R^2 is 0.47, which is quite a bit lower than last time and signifies that the model is less accurate.

3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

Considering the previous model wasn't amazingly accurate to begin with and this new model is even worse--no, the model is definetly not accurate. There's just not enough data for the train_test_split() to be effective as some data has to be taken from it anyway to test, which means even fewer training points to go off.
