FROM python:3.10-bullseye

WORKDIR /telegram-report-bot-ua

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["python3", "./report_channels.py"]