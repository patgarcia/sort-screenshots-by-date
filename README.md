# sort-screenshots-by-date
Sort screenshots captured in mac 

Given a screenshot file captured in mac, `Screen Shot 2022-01-26 at 6.33.16 PM.png`, create a new folder using the date portion of the filename, if it doesn't exist; Then move the screenshot inside of said folder, using the time `6.33.16 PM.png` portion as its new filename.

## Run

```bash
python sort_screenshots.py
```
- Currently you cannot provide a path to run the script in (future feature). The `sort_screenshots.py` script file needs to be inside the folder where the unsorted screenshots reside. 
- It works only for screen shots with the naming convention `Screen Shot <dash separated date> at <dot separated time>.png`.
