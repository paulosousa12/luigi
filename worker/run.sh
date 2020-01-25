#!/usr/bin/env bash
cd /worker/tasks
/usr/local/bin/python3 -m luigi --module crontask CronTask
