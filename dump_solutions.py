#!/usr/bin/python3

import datetime
import os
import pathlib
import time

import dotenv
import exercism


def DumpSolutionsToMentor():
    ex = exercism.Exercism()
    notifications = bool(ex.notifications()["meta"]["unread_count"])

    out = []
    out.append("<head><title>Solutions</title></head>")
    out.append(f"Generated: {datetime.datetime.now().replace(microsecond=0)}<hr>")

    if notifications:
        out.append("<h1><a href='https://exercism.org/mentoring/inbox'>Notifications</a></h1><hr>")
    for track in ("awk", "jq", "bash", "python"):
        out.append(f"<h2>{track}</h2>")
        out.append(f"<ul>")
        mentor_requests = ex.mentor_requests(track)
        for request in mentor_requests:
            out.append(f"<li><a href='https://exercism.org/mentoring/queue?track_slug={track}&exercise_slug={request['exercise_title'].lower().replace(' ', '-')}'>{request['exercise_title']}</a></li>")
        out.append("</ul><hr>")

    out.append("<ul>")
    out.append("<li><a href='https://exercism-team.slack.com/'>Slack</a></li>")
    out.append("<li><a href='https://github.com/IsaacG/exercism/blob/master/mentoring/python.md'>Python Notes</a></li>")
    out.append("</ul>")

    pathlib.Path(os.getenv("html_path")).write_text("\n".join(out))


if __name__ == "__main__":
    dotenv.load_dotenv()
    while True:
        DumpSolutionsToMentor()
        time.sleep(3*60)
