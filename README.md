# SalaryPrediction_SimpleLinearRegression_Model

To run the model

docker run -it salary python3 /salary/test.py  --years 22 --res './'

To get to see the contents of the container like saved model etc use the below two commands

docker commit 217e723179c8 user/test_image

docker run -ti --entrypoint=sh user/test_image


