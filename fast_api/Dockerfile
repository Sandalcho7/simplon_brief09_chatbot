FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV EDEN_AI_KEY ${{ secrets.EDEN_AI_KEY }}

EXPOSE 8000

CMD ["python", "main.py"]