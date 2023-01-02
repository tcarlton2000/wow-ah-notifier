FROM python:3

RUN python3 -m pip install --upgrade pip
RUN pip install requests

CMD ["python3", "./main.py"]
