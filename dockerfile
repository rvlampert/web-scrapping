FROM python:3.9.0

ADD main.py .

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY config.yaml ./

COPY src/ src/

CMD ["python", "./main.py"] 