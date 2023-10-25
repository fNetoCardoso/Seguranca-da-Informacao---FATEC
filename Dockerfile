FROM python:3.10
COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python","-u","api.py"]
