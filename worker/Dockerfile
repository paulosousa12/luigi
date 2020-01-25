FROM python:slim

ADD worker/ /worker/
WORKDIR /worker/

# Set execution permissions
RUN chmod a+x run.sh

# Instal project dependencies
RUN pip install -r requirements.txt

#Install cron
RUN apt-get -qq update && apt-get -qq -y install cron

# Copy the crontab config
COPY worker/crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Copy basic config for Luigi worker
COPY worker/config/luigi.cfg /etc/luigi/luigi.cfg

# Setup PYTHONPATH
ENV PYTHONPATH /worker

# Start cron
CMD ["cron", "-f"]
