FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV LANG C.UTF-8
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
#COPY ./chromedriver_linux64.zip /code/chromedriver_linux64.zip
#COPY ./google-chrome-stable_current_x86_64.rpm /code/google-chrome-stable_current_x86_64.rpm
#RUN apt-get update
#RUN apt-get install wget
#RUN apt-get install yum
#RUN rpm -ivh google-chrome-stable_current_x86_64.rpm
#COPY ./chromedriver  /usr/bin
RUN pip install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
