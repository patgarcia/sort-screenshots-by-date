# screenshots-by-date
Organize screenshots in folders by date 

Given a screenshot file captured in mac `Screen Shot 2022-01-26 at 6.33.16 PM.png` create a new folder using the date, if it doesn't exist, and add the screenshot inside of it save as the time `6.33.16 PM.png`.

## Run

```bash
python sort_screenshots.py
```
- Currently you cannot provide a path (future feature), the `sort_screenshots.py` file needs to be inside the folder where the screenshots image to be organized reside. 
- Currently works only for screen shots with the naming convention `Screen Shot <dash separated date> at <dot separated time>.png`.
