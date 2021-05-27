FROM python:3.9

WORKDIR /geostore

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "./run.py"]