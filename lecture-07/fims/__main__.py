import hashlib
import time
import shelve
import os
from . import helpers, TITLE, monitor, DATABASE
from .monit import getFiles


def main():
    helpers.hello(TITLE)

    # Test paths
    # for x in monitor:
    #     if not os.path.exists(x["path"]):
    #         print(f"Path does not exist: {x['path']}")
    #     else:
    #         print(f"Path exists: {x['path']}")

    files = {}

    while True:
        for file in getFiles(monitor):
            hash = hashlib.sha256()

            try:
                with open(file, "rb") as f:
                    for chunk in iter(lambda: f.read(2048), b""):
                        hash.update(chunk)
                    sha256 = hash.hexdigest()

                    # print(f"Computed hash for {file}: {sha256}")

                    if file in files and sha256 != files[file]:
                        print(
                            f'{file} has been changed! {time.strftime("%Y-%m-%d %H:%M:%S")}'
                        )

                    files[file] = sha256
                    with shelve.open(DATABASE) as s:
                        s[file] = files[file]
            except FileNotFoundError:
                print(f"{file} not found. It may have been deleted.")
            except PermissionError:
                print(f"Permission denied for {file}.")

        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        helpers.bye(TITLE)
