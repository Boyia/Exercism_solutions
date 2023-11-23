FROM python:3.6

# Create app directory
WORKDIR /

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt



ENTRYPOINT [ "python3", "print.py" ]