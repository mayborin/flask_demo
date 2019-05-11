FROM amazonlinux
RUN mkdir -p /flask_demo_app/
COPY ./flask_demo_app /flask_demo_app
RUN pip -r /flask_demo_app/requirements.txt
RUN python /flask_demo_app/manager.py setup_db
EXPOSE 5000

ENTRYPOINT 	["python", "/flask_demo_app/manager.py", "server"]
