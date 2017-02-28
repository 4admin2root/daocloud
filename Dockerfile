#FROM nginx
#RUN echo "Happy Programming!" > /usr/share/nginx/html/index.html
FROM ubuntu:14.04
# Update packages
RUN apt-get update -y
# Install Python Setuptools
RUN apt-get install -y python-setuptools git telnet curl
# Install pip
RUN easy_install pip
# Bundle app source
295
ADD . /src
WORKDIR /src
# Add and install Python modules
RUN pip install Flask
# Expose
EXPOSE 5000
# Run
CMD ["python", "entry.py"]
