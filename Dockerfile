FROM kalilinux/kali-rolling

# Updates
RUN apt-get update

# Utilities and Libs
RUN apt-get install -y neovim python3-pip python3-dev ruby ruby-dev exiftool binwalk zip netcat

# PIP
RUN pip3 install --upgrade pip

RUN pip install requests