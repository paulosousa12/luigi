FROM python:slim

ADD scheduler/ /scheduler/
WORKDIR /scheduler/

# Set execution permissions
RUN chmod a+x run.sh wait-for-postgres.sh

# Instal project dependencies
RUN pip install -r requirements.txt

#Install cron
RUN apt-get -qq update && apt-get -qq -y install postgresql-client libpq-dev

# Start cron
CMD ["run.sh"]
