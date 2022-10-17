# load dataset

import pandas 
import logger

db=pandas.read_csv("salary.csv")
print("Dataset Loaded Sucessfully.")

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--years', type=int , help='years')
parser.add_argument('--res', type=str , help='directory') # will be accesible with args.OPT

args = parser.parse_args()


logger.setup_logger(args)
# Creating features and target.
#x = feature/independant variable
#y = target / dependant variable
x=db["YearsExperience"]
y=db["Salary"]

# loading LinearRegression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x = db["YearsExperience"].values.reshape(30,1)
model.fit(x,y)
print("Model created Sucessfully.")
logger.print_and_log("Model created Sucessfully.")

# Saving trained model
import joblib
joblib.dump(model,'salary_model.pkl')
print("MODEL SAVED SUCCESSFULLY.")
logger.print_and_log("MODEL SAVED SUCCESSFULLY.")

model = joblib.load("salary_model.pkl")

#predict
# years=int(input("Enter years of experience: "))
predict=model.predict([[args.years]])
print("Your salary as per your year of experience is :",round(predict[0],2)," INR")
logger.print_and_log("Your salary as per your year of experience is :"+str(round(predict[0],2))+" INR")

