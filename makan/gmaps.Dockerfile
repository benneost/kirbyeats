FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN pip install --no-cache-dir -r http.reqs.txt
COPY ./gmaps.py ./gmaps.js ./
CMD [ "python", "./gmaps.py" ]
