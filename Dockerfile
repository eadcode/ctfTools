# ---------- UBUNTU ----------
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Updates
RUN apt-get update

# Utilities and Libs
RUN apt-get install -y python3-pip python3-dev ruby ruby-dev exiftool binwalk zip netcat curl software-properties-common npm

# --- PYTHON ---
RUN cd /usr/local/bin \
    && ln -s /usr/bin/python3 python

# PIP
RUN pip3 install --upgrade pip

COPY tools/requirements.txt /home/ctf/
RUN pip install -r /home/ctf/requirements.txt

# --- NODE ---
RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest