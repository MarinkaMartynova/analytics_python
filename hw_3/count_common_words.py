# exercise 3
import re
from collections import Counter

text = """
3.2 Logistic Regression
A binary dependent variable—one with just two potential outcomes, like yes or no—and one or more
independent variables are analysed using the statistical technique known as logistic regression. Data
is frequently divided into two or more groups using machine learning and data science techniques.A
probability between 0 and 1 that represents the chance of the dependent variable falling into a certain
category is the output of a logistic regression model. Binary classification issues (where the dependent
variable has two potential outcomes) and multiclass classification problems may both be solved using
logistic regression models (where the dependent variable has more than two possible outcomes).The
logistic function, which converts any input with a real value to a number between 0 and 1, serves as the
foundation for the logistic regression model. Given the values of the independent variables, the logistic
function is used to model the likelihood of the dependent variable. The maximum likelihood estimation
method is used to estimate the parameters of a logistic regression model. The model may be used to
forecast the likelihood that a fresh set of data points will fall within a specific category of the dependent
variable once the parameters have been calculated. For a variety of prediction problems, the machine
learning and data science sectors of finance, healthcare, and marketing frequently employ the popular
and effective method of logistic regression.
Here’s an example of how to implement logistic regression using scikit-learn in Python (Towardsdatascience,
n.d.-a):
In this example the necessary modules from scikit learn are first imported. Next, we define our sample
data. We have an array X that represents the input features and an array y that represents the target variable.
The target variable is binary, with values of 0 or 1. Next, we create a LogisticRegression object
called logreg. This will be our logistic regression model. To train the model, we call the fit() method on
the logreg object, passing in the input features X and the target variable y.
Once the model is trained, we can make predictions on the training data by calling the predict()
method on the logreg object and passing in X. The predicted values are stored in the y_pred array.b. To
evaluate the performance of our model, we calculate the accuracy by comparing the actual target variable
y with the predicted values y_pred. The accuracy is a common metric used to measure the performance
of classification models.
Finally, we visualize the data points and the decision boundary using matplotlib. The scatter() function
is used to plot the actual data points, and the plot() function is used to plot the predicted probabilities
of the positive class. The predicted probabilities are obtained using the predict_proba() method of the
logreg object. We also add labels to the x-axis and y-axis and include a legend for clarity. The resulting
plot will show the data points as blue dots and the decision boundary as a red curve. Running the code
will output the accuracy and display the scatter plot with the actual data points and the decision boundary.
"""

# Приводим текст к нижнему регистру и удаляем все знаки препинания
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)

# Разбиваем текст на слова
words = text.split()

# Подсчитываем количество каждого слова
word_count = Counter(words)

# Выводим 10 самых частых слов
most_common_words = word_count.most_common(10)
print(most_common_words)
