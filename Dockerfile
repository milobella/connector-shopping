FROM python:3.6

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install .


CMD ["shoppinglist_launcher"]
