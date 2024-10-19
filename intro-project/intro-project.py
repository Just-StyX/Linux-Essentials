#!/usr/bin/env python3

"""
This monitors a csv file and insert changes to database
Requirements:
    pyscopg: import other needed modules
    pyinotify: provide functionality for file monitoring
"""

import psycopg # type: ignore
import pyinotify # type: ignore


FILENAME = "./fatal.csv"

def check_and_notify(file):
    """
    This function monitors the csv file: fatal.csv
    """
    try:
        with psycopg.connect(
            "dbname=database user=user password=password host=host port=port"
        ) as connection:
            with connection.cursor() as record_cursor:

                error_or_fatal = ''
                with open(FILENAME, 'r', newline="", encoding="utf-8") as records:
                    record = records.readlines()[-1].split(",")
                    error_or_fatal = record[1]
                    record_cursor.execute(
                    "INSERT INTO fatal (created_on, error_level,error_message) VALUES (%s, %s, %s)",
                    (record[0], record[1], record[2])
                    )

                alert = 'Email alert: ' + error_or_fatal
                print(alert)

    except FileNotFoundError as e:
        print("Error connecting to my db: ", e)

watch = pyinotify.WatchManager()
watch.add_watch(FILENAME, pyinotify.IN_CLOSE_WRITE, check_and_notify)
notifier = pyinotify.Notifier(watch)
notifier.loop()