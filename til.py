#!/usr/bin/env python3

import os
import sys
import tempfile
import subprocess

from contextlib import contextmanager
from subprocess import call


DIR = '/home/aunger/Dev/til/'
EDITOR = os.environ.get('EDITOR','vim')
initial_message = b"# "


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def main(argv):
    if len(argv) < 2:
        sys.exit('Please provide the folder name and filename.')

    folder = os.path.join(DIR, argv[0])
    os.makedirs(folder, exist_ok=True)

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_message)
        tf.flush()
        call([EDITOR, tf.name])
        tf.seek(0)
        edited_message = tf.read()

        filename = os.path.join(DIR, argv[0], f"{argv[1]}.md")
        myfile = open(filename, 'w')
        myfile.write(edited_message.decode("utf-8"))
        myfile.close()

    with cd(DIR):
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-am", f"\"Added {argv[0]}/{argv[1]}\""])
        subprocess.call(["git", "push", "origin", "main"])

    print(f"Wrote {filename}")
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])  # Skips program name
