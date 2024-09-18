FROM python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 1616
CMD ["python", "app.py"]