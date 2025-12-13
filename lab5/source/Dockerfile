# stage 1. base iso is taken
FROM python:3.11-slim AS builder
#working directory is creating
WORKDIR /hello
# requirements is being copied
COPY requirements.txt .
#python wheels are being generated in /wheels
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

#stage 2. pure base iso is taken for the second time
FROM python:3.11-slim
WORKDIR /hello
#ready wheels are copied from stage 1
COPY --from=builder /wheels /wheels 
COPY requirements.txt .
# requirements are being installed from wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt
#the main code is copied
COPY hello2.py .

#stage 3. buferisation is disabled
ENV PYTHONUNBUFFERED=1
#the main script starts
CMD ["python", "hello2.py"]
