FROM nikolaik/python-nodejs:latest


WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r llm_processing/requirements.txt

RUN npm install $PACKAGENAME

RUN chmod +x /start.sh

CMD ["./start.sh"]
