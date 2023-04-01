#!/usr/bin/python3
"""Write out solutions waiting on mentoring."""

import datetime
import os
import pathlib
import time

import dotenv
from . import exercism


def dump_solutions_to_mentor():
    """Fetch solutions waiting for mentoring and write to file."""
    ex = exercism.Exercism()
    notifications = bool(ex.notifications()["meta"]["unread_count"])

    out = []
    out.append("<head><title>Solutions</title></head>")
    out.append(f"Generated: {datetime.datetime.now().replace(microsecond=0)}<hr>")

    if notifications:
        out.append("<h1><a href='https://exercism.org/mentoring/inbox'>Notifications</a></h1><hr>")
    for track in ("awk", "jq", "bash", "python"):
        out.append(f"<h2>{track}</h2>")
        out.append("<ul>")
        mentor_requests = ex.mentor_requests(track)
        for request in mentor_requests:
            out.append(
                "<li><a href='https://exercism.org/mentoring/queue?track_slug="
                f"{track}&exercise_slug={request['exercise_title'].lower().replace(' ', '-')}'>"
                f"{request['exercise_title']}</a></li>"
            )
        out.append("</ul><hr>")

    out.append("<ul>")
    out.append("<li><a href='https://exercism-team.slack.com/'>Slack</a></li>")
    out.append(
        "<li><a href='https://github.com/IsaacG/exercism/blob/master/mentoring/python.md'>"
        "Python Notes</a></li>"
    )
    out.append("</ul>")

    pathlib.Path(os.getenv("html_path")).write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    dotenv.load_dotenv()
    while True:
        dump_solutions_to_mentor()
        time.sleep(3*60)
