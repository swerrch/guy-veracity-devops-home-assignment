FROM python:latest

WORKDIR /home
COPY ./ ./
RUN pip install -r requirements.txt
CMD [ "python", "./run_sqls.py" ]