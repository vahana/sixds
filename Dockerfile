FROM python:3.7.6

WORKDIR /sixds

COPY . .

RUN pip install --no-deps -r requirements.txt

EXPOSE 6543

CMD ["pserve", "./development.ini"]

