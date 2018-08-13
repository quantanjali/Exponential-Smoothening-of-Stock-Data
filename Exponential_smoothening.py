#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 03:25:13 2018

@author: kumarianjali

Exponential Smoothing. 

Comiler/Interpreter : Python 3.6.3 64bits, Qt 5.6.2, PyQt5 5.6 on Darwin 
Environment Version : Spyder 3.2.6 
Framework           : Anaconda Navigator 1.8.3
OS Platform         : MacOS High Sierra 10.13.2

DISCLAIMER : Runs on MS Window/Unix/Linux but may not run on earlier version of Python

ERROR HANDLING : 
1. Please check your internet for connection.
2. This program has been coded to run with internet connection.
3. Ensure to install QUANDL API to download data and run this program. 

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl                           # Used for downloading data from quandl.com
# Since there is API issues for Yahoo, Google & NASDAQ, I am using quandl.com for NASDAQ data
# Please install Quandl API for Python if its not there in your system
# You can install this package by using the pip tool on Python Command Prompt:
# $ pip install quandl
# To install on Spyder ( Anaconda), please use following command on terminal instead of pip
# conda install -c anaconda quandl


###############################################################################
# Preperation of Library to use and reuse in main program
###############################################################################

def estimate_coefficient(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()
 

###############################################################################
# Blank Print functions have been used many times for perfect OUTPUT format
###############################################################################
print() # blank print has been used for OUTPUT decoration & space management
print()
print("================================================================")
print("PYTHON  : EXPONENTIAL SMOOTHING                                 ")
print("================================================================")
print("Developer : Kumari Anjali, Quant Finance, National Institute of Securities Markets")
print()


#################################################################################
# Pulling information from part 1 to performs exponential smoothing. 
#################################################################################

#################################################
#  CODE FOR DOWNLOADING STOCK DATA FROM QUANDL
#################################################

# To request specific data from Quandl.com:
dataset = quandl.get("WIKI/AAPL.4", start_date="2017-08-15", end_date="2018-04-15", collapse="monthly", authtoken="CzibtKpDF8ssxxmSK3RD")
Apple_Stock = dataset['Close']

# For Exponentiel Smoothing Formula, Apple Stock price taken as value of Y \
# And Time Period has been taken as X

Y = np.array(Apple_Stock)
print()
print()
print("EXPONENTIAL SMOOTHING - DATA COLLECTION PROJECT:PART-01")
print()
print("==============================================================")
print("ACTUAL DATA : AAPL(NASDAQ) STOCK PRICE FOR 8 MONTHS")
print("==============================================================")
print()
print("---------------")
print("X","   ","Y")
print("---------------")

# Displaying Period & Actual Price data and arranging it in List

period = []
actual_price = []
count = 1
for i in Y:
    print(count,"  ",i)
    period.append(count)
    actual_price.append(i)
    count = count+1
print("---------------")    
print()
print()
                
#################################################
#   CODE TO DISPLAY PLOT OF ACTUAL STOCK DATA 
#################################################

print("---------------------------------------------------------")
print("Plot of Actual Stock Price vs Time Period")
print("---------------------------------------------------------")
print()
plt.plot(Y)
plt.axis(xmin = 0, xmax = 8)
plt.title('Plot 1 : Actual Stock Price movement')
plt.xlabel('Period')
plt.ylabel('Actual Stock Price')
plt.show()
print()
print("=========================================================")
print("WHY I CHOSE THIS NASDAQ LISTED COMPANY & TIME PERIOD ?")
print("=========================================================")
print()
print("Aaple Inc stock price has been taken from September 2017 \n\
to April 2018 in sequentiel order, preferebly close to \n\
the first day of a month. These sequentiel price shows \n\
great spike w.r.t.time. In the beginning of selected time\n\
frame, it has gone drastically down and then up and then \n\
down again.The high spikes in Time Series data makes it \n\
perfect for Exponential Smoothing for stable prediction.")
print()
print()

###############################################################
# CODE GENERATING EXCEL FILE & DISPLAY ACTUAL STOCK PRICE'''
###############################################################

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Y': Y})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('AAPL.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
print("=========================================================")
print("DOWNLOADED AAPL STOCK DATA IN EXCEL FOR DISPLAY")
print("=========================================================")
print()
print("AAPL.xlsx named Excel file has been created with data. \nPlease check working folder to view this file")
print()
print("=========================================================")
print("               PART 01 OF CODE : THE END                 ")
print("=========================================================")
print()
print("EXPONENTIAL SMOOTHING MODEL - PROJECT PART 02")
print()
input("To start Exponential Smoothing, Press ENTER to continue ! ")


####################################################################################
# ENTERING VALUE OF ALPHA WITH VALIDATION CHECK TO BE BETWEEN 0 & 1 :
####################################################################################

count = 'n'
while count == 'n' : 
    try:
        alpha = eval(input('Enter Alpha (value must be between 0 and 1. To EXIT press Integer Value > 1): '))
        if 0 <= alpha <= 1 :
            print("You have entered a VALID ALPHA value", alpha)
            print("Aplpha Validity Check Passed !! \nWe are now ready for EXPONENTIAL SMOOTHING")
            #wait = input("Press ENTER/RETURN to continue !")
            print()
            #############################################################
            # EXPONENTIAL SMOOTHING AUTOMATION : 
            # Formula used : Ft1 = alpha*Yt + (1 – alpha)*Ft  
            # Where first actual and forecast price are equal,  F1 =  Y1
            #############################################################
            print("==================================================")
            print("DISPLAYING ACTUAL AND EXPONENTIALLY SMOOTHED DATA ")
            print("==================================================")
            print("--------------------------------------------------")
            print("Time_Period", "Actual_Price", "Forecast_Price")
            print("--------------------------------------------------")
            
            X = []
            Y = []
            F = []
            Forecast_Price = actual_price[0]
            Time_Period = 0
            for i in actual_price:
                Time_Period = Time_Period + 1
                X.append(Time_Period)
                Y.append(i)
                F.append(Forecast_Price)
                print("  %d         %.2f       %.2f" %(Time_Period, i, Forecast_Price))
                Forecast_Price = alpha*i + (1-alpha)*Forecast_Price
            
            print("=================================================")
            print()
            print()
            #############################################################################
            # Display the graph of the original data and the “smoothed data” 
            #############################################################################
            print("==============================================")
            print("DISPLAYING THE GRAPH ORIGINAL & SMOOTHED DATA")
            print("==============================================")
            print("Alpha value : %.1f" %(alpha))
            print("For above Aplha value, Actual and exponentially smoothed Forecasted price is as below :")  
            plt.plot(Y, label='Original')
            plt.plot(F, label='Smoothed')
            plt.legend()
            plt.title('Graph for Original vs. Smoothed Data')
            plt.xlabel('Period')
            plt.ylabel('Price')
            plt.show()         
            print()
            print() 
            #############################################################
            # Verify if this model is appropriate? Or Loop
            #############################################################
            print("==============================================")
            print("MODEL IS APPROPRIATE OR NOT :  VALIDITY CHECK ")
            print("==============================================")
            print()
            Model_Validity = input("Is this model appropriate ? Press y/n to process or other key to EXIT :")
            if Model_Validity.lower() == 'y':
                print("Good ! That you like this Exponential Smoothing model")
                print()        
                #####################################################################
                # Using Exponential smoothing model to predict time period 9 (x = 9).  
                # Exponential smoothing provides price prediction for the 
                # next month based on the previous month's actual & forecasted price.
                #####################################################################
                print("Now, we are using Exponential smoothing model to predict price of time period 9 (x = 9)")  
                print()
                print("=======================================================")
                print("Price prediction for 9th period is = : %.2f" %(Forecast_Price))
                print("=======================================================")
                print()
                Time_Period = Time_Period + 1  
                X.append(Time_Period)
                Actual_Price = 'NA'
                Y.append(Actual_Price)
                F.append(Forecast_Price)
                print("======================================================")
                print("ALL VALUE FROM 1ST TO 9TH MONTH PERIOD ARE AS FOLLOWS:")
                print("======================================================")
                print("Value of Time Period(X) including 9th month is : ", X)
                print()
                print("Value of Actual Price (Y) for 9th month is (NA) : ", Y)
                print()
                print("Value of Forecasted Price (F) is 1st to 9th Month : ", F)
                print("=======================================================")
                print()
                print()
                print("=======================================================")
                print("DISPLAYING GRAPH FOR FORECASTED PRICE FOR 9th MONTH ")
                print("=======================================================")               
                plt.plot(X,F)
                plt.title(' Forecasted Price movement till 9th Months')
                plt.xlabel('Period')
                plt.ylabel('Price')
                plt.show()
                print()
                print("======================================================")
                print("             PART 02 OF PROJECT : THE END             ")
                print("======================================================")
                print()
                count = 'y'               
            elif Model_Validity.lower() == 'n':
                print("No Problem ! You can change value to APLHA to change this model !")
                count = 'n'                 
            else:
                print("Unrecognised Value ! Program EXIT ")
                count = 'y'
        else:
            print("PROGRAM EXITS. Thanks !")
            count = 'y'  # Value 'n' will NOT EXIT while 'y' will EXIT the program. This is just to stop the execution.
    except NameError: 
        print("Oops!  That was not valid Character.  Try again...")  
    except SyntaxError :
        print("Oops!  That was not valid Character.  Try again...")

#################################################################################
# LINEAR REGRESSION MODEL & CORRELATION CO-EFFICIENT 
#################################################################################
        
def main():
    # Observations taken from Part 01 of code
    x = np.array(period)
    y = np.array(actual_price)
    
    input("Linear Regression Model starts here. Press ENTER to continue ! ")
    
    # Calculating Correlation coefficients using Numpy
    cr = np.corrcoef(x, y)[0, 1]
    print()
    print("LINEAR REGRESSION MODEL")
    print()
    print("============================================================")
    print("Correlation Coefficient :", cr)
    print("============================================================")
    print()
       
    # estimating coefficients
    b = estimate_coefficient(x, y)
    print("============================================================")
    print("Estimated Regrssion Coefficients given below :")
    print("------------------------------------------------------------")
    print("Y-Intercept:Beta0 = {} \nSlope:Beta1 = {}".format(b[0], b[1]))
    print("============================================================")
    print()
    print()
    print("                 GRAPH OF REGRESSION LINE                  ")
    print("                 ========================                  ")
    
    # plotting regression line
    plot_regression_line(x, y, b)
    print()
    print("============================================================")
    print("                PART 03 OF CODE : THE END                ")
    print("============================================================")
    print()
    print("Developed by : Kumari Anjali @ NISM, MUMBAI, INDIA          ")
    print("============================================================")
    print()
    print("-------------------")
    print("THE END OF PROJECT ")
    print("-------------------")
    print()
 
if __name__ == "__main__":
    main()

###################################################################
# THE END 
###################################################################                            
