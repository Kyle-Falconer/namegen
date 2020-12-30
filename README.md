
## Name List Creation
For the name lists:
1. Scrape
2. Preprocess
3. Merge
4. Filter

## Name Lists
The name_lists folder contains these sources
* [ssa-baby-names.csv](name_lists/ssa-baby-names.csv): American names that originally came from the [Social Security Administration site](https://www.ssa.gov/OACT/babynames/), via the [US Baby Names GitHub project](https://github.com/hadley/data-baby-names)
* [tamilcube_scraped_names.csv](name_lists/tamilcube_scraped_names.csv): Indian names scraped from [tamilcube.com](http://tamilcube.com/).
* [meaning_of_names_scraped_names.csv](name_lists/scraper_temp/meaning_of_names_initial_scraped_names.csv) Multilingual name meanings scraped from [meaning-of-names.com](https://meaning-of-names.com/).
* [pantheon.tsv](name_lists/pantheon.tsv) comes from the Harvard dataset: [A Manually Verified Dataset of Globally Famous Biographies](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28201)
* [star_trek.csv](name_lists/star_trek.csv) contains star trek character names, adapted from [Wikipedia](https://en.wikipedia.org/wiki/List_of_Star_Trek_characters)
* [stripper_names.txt](name_lists/stripper_names.txt): a list of stripper names
* [people_we_know.txt](name_lists/people_we_know.txt): a list of people you know. Customize this list to suit, include alternate spellings.
* [names_merged.json](name_lists/names_merged.json): the merged and deduplicated result of all the above name lists in JSON format

## Development
This project is developed for Python 3.x and works well in the PyCharm IDE. It's recommended to use Anaconda or some other virtual environment for developing.

Tests in the [./tests](./tests`) folder are written for the pytest framework.

**Important: before committing changes to the `names_merged.json`, delete the contents of the `people_we_know.txt` list and re-run the merge script.**