# Polynomial Regression
# Data Preprocessing

# Importing the Dataset

dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# Splitting the dataset into tne Training set and test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio = 2/3)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)


# Feature Scaling
# training_set[ ,2:3] = scale(training_set[ ,2:3])
# test_set[ ,2:3] = scale(test_set[ ,2:3])

# Fitting Linear regression to the dataset
lin_reg = lm(formula = Salary ~ ., data = dataset)

# Fitting Polynomial regression to the dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ ., data = dataset)

# Visualising the Simple Linear Regression Result
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Truth OR Bluff (Linear Regression)') + 
  xlab('Position Level') + 
  ylab('Salary')

# Used for higher resolution and smoother curve
# x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)

# Visualising the Polynomial Regression Result
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Truth OR Bluff (Polynomial Regression)') + 
  xlab('Position Level') + 
  ylab('Salary')

# Predicting a new result with Simple Linear Regression
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))

# Predicting a new result with Polynomial Regression
y_pred = predict(poly_reg, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5^2,
                                                Level3 = 6.5^3,
                                                Level4 = 6.5^4 ))



