INTRODUCTION :
In this project I wrote  a program that will use the exponential smoothing to help you predict a value in the future.
In addition, your program should come up with the linear regression equation to predict the same value as was done in
exponential smoothing.

PROBLEM STATEMENT
Many time series values give spiked results. This is difficult to develop a forecast on due to the erratic nature. Exponential
smoothing can smooth this out so predictions are more stable: What do you believe will happen if alpha is equal to 1?

Formula for Exponential Modeling:
Ft+1 = αYt + (1 –α)Ft
Where,
Ft+1 = forecast for time period t + 1
Yt = time series value
α = smoothing constant (between 0 and 1)
Ft = forecast for time period t
Note : F1 = Y1

PART 01 :
Obtain the stock price inform from www.nasdaq.com. In this part, go to www.nasdaq.com, choose a company to analyze,
click the “historical quotes” link on the left side after picking a company.

Pick the stock prices for at least 8 months picking one data point out of each month as close to the first of the month as
possible. The x values will be from 1 to 8 (where 1 indicates the first month looked at) while the y values will be the stock
price.

SOLUTION:
Data Collection Criteria : I have tried to download data from www.nasdaq.com, but this
site is under maintenance from last few months, hence, Nasdaq data has been downloaded from Yahoo Finance.
Company Identification and Choice Explanation:
Company Name : Apple Inc, NASDAQ Ticker : AAPL
Time Frame : 1st September 2017 to 1st April 2018 (8 months)

I have chosen “Aaple Inc” stock price from Nasdaq because its stock price value from September 2017 has shown great
spikes. In the beginning of my selected time frame, it has gone down drastically and then it started spiking up and again down.
The high turbulence and spike in its curve make it very difficult to develop a forecast due to the erratic nature. Hence,
exponential smoothing can perfectly be applied here in this case to smooth this out so predictions are more stable. Hence,
exponential smoothing model based on the Aaple stock price value from September 2017 onwards due to its erratic nature
so that exponential smoothing can make sense.

Time Frame for Data : Each data value obtained here has been taken from first entry for the month chosen. I have chosen
“Aaple Inc” stock price for 8 months from 1st April 2018 to 01st September 2017.

Data has been collect from sequential months. Value of “X” has been taken from 1 to 8 while value of “Y” has been
taken as stock price. X = 1 is September 2017 while X=8 is April 2018. From X = 1(September 2017) month, X value has been taken sequentially till April 2018.

Data has been delivered in an Excel spreadsheet in Python_Data sheet.
The final Excel data is given as follows:
X   1       2      3      4      5     6      7      8
Y 164.00 154.12 169.04 171.85 169.23 167.43 178.12 168.34

PART 02 :
• Write a Python program that asks the user for the information from part 1 and performs exponential
smoothing based on it.
• The perfect program will allow the user to input alpha.
• Display the graph of the original data and the “smoothed data”
• Have the user verify if this model is appropriate? If it is not, then it should loop asking for new entries for alpha
until the user indicates the model is appropriate.
• At this point, it should use the exponential smoothing model to predict time period 9 (x = 9).
• Read the explanation above closely to understand what exponential smoothing provides for the next month based on the previous month.

SOLUTION:
Exponential Smoothing Logic : I have used standard general formula to find forecasted price :
Forecast_Price(i+1) = alpha*actual_price(i) + (1-alpha)*Forecast_Price(i)
Where Forecast_Price(1) = actual_price(1)
Program asks user to ENTER value of ALPHA with validation range of 0 to 1. Due exception handling and data validation checking has been done in this program to handle invalid data
given by the user. In all possible data input case, it either takes any value between 0 to 1. To EXIT the program, I have coded
input value to be any number above 1. This is planned EXIT code in the programme.

The next code verifies if this model is appropriate or not ? User can choose (y/n) as input value. In case user enters capital or
small y/n, it’s accepted and program proceeds for next activity. Here I have coded second EXIT in this code, if user enters any
other character from keyboard other than ‘y/n’. Using Exponential smoothing model, I have coded to predict time period 9 (x = 9). Using exponential smoothing technique,
price prediction for the next month based on the previous month's actual & forecasted price has been done.

PART 03:
Regression Logic:
Linear regression is a statistical approach for modelling relationship between a dependent variable with a given set of
independent variables. Simple linear regression is most basic version of linear regression. Simple linear regression is an approach for
predicting a response using a single feature. It is assumed that the two variables are linearly related. Hence, I try to find a
linear function that predicts the response value(y) as accurately as possible as a function of the feature or independent variable(x).

The equation of regression line is represented as:
F(Xi) = Beta0 + Beta1 * Xi
Where:
Yi represents the predicted response value for ith observation. Beta0 and Beta1 are regression coefficients and represent yintercept
and slope of regression line respectively.
To create my model, I have estimated the values of regression coefficients Beta0 and Beta1 and used these coefficients in the model to predict value for period 9.
I have used the Least Squares technique to minimize the total residual error. The calculation result has been found as below :
Correlation Coefficient: 0.6084266287339625
Y-Intercept: Beta0 = -6.15804945054947
Slope: Beta1 = 38.64984432234433 Since Correlation Coefficient is 0.6084266287339625, it shows very positive relationship between X and Y i.e. time period and price of stock. 

Structure and Design Criteria:
• The appropriate flow mechanism has been used in the program (while loop, etc.) for ease of use of the user.
• Code has been made as “function” to be put in library for re-use. Separate library has not been created to avoid multiple files, but it can be easily done by placing all functions in programs in separate file with file_name.py and by import it using “import file_name” in main program.
• Code has been documented where appropriate.
• Code has been made “readable” with appropriate variable names and structured programming techniques used.
