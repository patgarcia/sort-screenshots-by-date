import os, re


def main():
    # assuming screenshot are in this dir
    screenshots = [
        file for file in os.listdir(os.getcwd()) if file.startswith("Screen")
    ]

    # regex to capture time with file extension from
    # 'Screen Shot 2021-11-23 at 12.24.31 PM.png'
    screen_shot_regex = re.compile(r"^(?:.*?)(?P<date>[\d-]*?)(?:\sat\s)(?P<time>.*)")

    while screenshots:
        # os walk generator returns (dirpath, dirnames, filenames).
        dirs = next(os.walk("."))[1]
        screenshot = screenshots.pop()
        match = screen_shot_regex.match(screenshot)
        file_name = match.group("time")
        folder_name = match.group("date")
        if not folder_name in dirs:
            os.mkdir(folder_name)
        destination = os.path.join(folder_name, file_name)
        os.rename(screenshot, destination)


if __name__ == "__main__":
    main()
