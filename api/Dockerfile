FROM python

WORKDIR /app/api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

WORKDIR /app

ENTRYPOINT [ "python" ]
CMD [ "-m", "api" ]
