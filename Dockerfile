FROM python:2
RUN mkdir -p /flask_demo_app
WORKDIR /flask_demo_app
COPY ./flask_app ./
RUN pip install -r /flask_demo_app/requirements.txt
RUN python manager.py setup_db

EXPOSE 80
EXPOSE 5000

ENTRYPOINT 	["python", "/flask_demo_app/manager.py", "server"]
