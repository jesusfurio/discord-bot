FROM python

COPY src /www/app 

WORKDIR /www/app

COPY requirements.txt requirements.txt

RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends \
        ffmpeg 

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "main.py"]