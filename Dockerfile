FROM python

COPY src /www/app

WORKDIR /www/app

RUN apt-get update -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends \
        ffmpeg 

RUN pip3 install requests
RUN pip3 install BeautifulSoup4
RUN pip3 install discord
RUN pip3 install youtube_dl
RUN pip3 install PyNaCl

CMD ["python3", "-u", "main.py"]