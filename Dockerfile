# Define parent image
FROM pytorch/pytorch:latest

# Create directories, set working directory
RUN mkdir /salary
WORKDIR /salary
ADD req.txt /salary/


RUN python -m pip install -r /salary/req.txt

# Execute final tasks and copy relevant files

ADD logger.py /salary/
ADD salary.csv /salary/
ADD test.py /salary/


# RUN chmod +x /quantum-anomaly/circuit.py
RUN chmod +x  /salary/test.py
# Define entry-point
CMD [ "python3", "/salary/test.py" ]
