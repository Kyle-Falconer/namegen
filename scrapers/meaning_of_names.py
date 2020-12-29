# scraper for http://www.meaning-of-names.com/


import csv
import os

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, \
    NoSuchWindowException

from file_utils import save_names_raw, count_lines

scraper_tmp_dir = os.path.join("name_lists", "scraper_temp")

merged_output_filename = os.path.join("name_lists", "meaning_of_names_scraped_names.csv")

# the output of the first pass of name scraping
initial_scraped_filename = os.path.join(scraper_tmp_dir, "meaning_of_names_initial_scraped_names.csv")

# The file created as a result of the main scrape operation
rescrape_list_filename = os.path.join(scraper_tmp_dir, "meaning_of_names_rescrapable_names.csv")

# these are two temp files for the deep scrape
rescraped_filename = os.path.join(scraper_tmp_dir, "meaning_of_names_rescraped_names.csv")
rescraped_remaining_filename = os.path.join(scraper_tmp_dir, "meaning_of_names_rescrapable_names_remaining.csv")


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive.
    https://stackoverflow.com/a/7001371/940217
    """
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def scrape():
    name_output = []
    names_to_rescrape = []
    driver = webdriver.Firefox()
    for letter in char_range('a', 'z'):
        site_url = f"http://www.meaning-of-names.com/names/{letter}-names-1.asp"
        print(f"scraping site: {site_url}")
        driver.get(site_url)
        paging = True
        number_of_pages = 1
        number_of_names = 0
        while paging:
            name_index = 0
            name_row = driver.find_elements_by_class_name("name-table-body-row")
            for row in name_row:
                name_elem = row.find_element_by_class_name("name-col")
                gender_elem = row.find_element_by_class_name("gender-col")
                # name_meaning_elem = row.find_element_by_xpath(".following-sibling::div")
                name_meaning_elem = driver.execute_script("""
                    return arguments[0].nextSibling
                """, gender_elem)
                origin_elem = row.find_element_by_class_name("origin-col")

                name_text = name_elem.text
                meaning_text = ""
                if "..." in name_meaning_elem.text:
                    print(f"warning: meaning is truncated for \"{name_text}\"")
                    names_to_rescrape.append({
                        "name": name_text,
                        "url": row.find_element_by_link_text(name_text).get_attribute("href"),
                        "meaning": None
                    })
                else:
                    meaning_text = name_meaning_elem.text

                name_output.append({
                    "name": name_text,
                    "gender": gender_elem.text,
                    "origin": origin_elem.text,
                    "url": row.find_element_by_link_text(name_text).get_attribute("href"),
                    "meaning": meaning_text
                })
                name_index = name_index + 1

            try:
                # next_btn = driver.find_element_by_xpath("//a[@class=\"btn btn-primary btn-md\" and text()=' > ']")
                paging_button_wrapper = driver.find_element_by_class_name("pagination-wrapper")
                next_btn = paging_button_wrapper.find_element_by_xpath(".//a[text()='>']")
                save_names_raw(initial_scraped_filename, name_output)
                save_names_raw(rescrape_list_filename, names_to_rescrape)
                number_of_names = number_of_names + len(name_output)
                names_to_rescrape = []
                name_output = []
                next_btn.click()
                number_of_pages = number_of_pages + 1
            except NoSuchElementException:
                paging = False
        print(f"reached end of the list for this page, saw {number_of_pages} pages and {number_of_names} names")
    driver.close()


def deep_scrape():
    scrapables = []
    rescrape_temp_file = rescrape_list_filename
    if os.path.isfile(rescraped_remaining_filename):
        print(f"Resuming deep scrape from temp file.")
        rescrape_temp_file = rescraped_remaining_filename
    else:
        print(f"No restore point found. Starting from the top of the list.")

    with open(rescrape_temp_file) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if not row['meaning']:
                scrapables.append({'name': row['name'], 'url': row['url']})
    name_output = []
    print(f"starting deep scrape for {len(scrapables)} names")
    page_timeout_in_seconds = 20
    driver = webdriver.Firefox()
    for scrapable in scrapables:
        print(f"scraping site: {scrapable['url']}")
        retry_count = 0
        page_loaded = False
        try:
            while not page_loaded and retry_count < 5:
                try:
                    driver.get(scrapable['url'])
                    driver.set_page_load_timeout(page_timeout_in_seconds)
                    page_loaded = True
                except WebDriverException or TimeoutException as load_error:
                    retry_count = retry_count + 1
                    print(f"errored out, retry #{retry_count}; {load_error.msg}")
                    driver.close()
                    driver = webdriver.Firefox()
                    driver.get(scrapable['url'])
                    driver.set_page_load_timeout(page_timeout_in_seconds)

            meaning_elem = driver.find_element_by_css_selector(".p402_premium .p402_hide:nth-child(1)")

            name_text = scrapable['name']
            meaning_text = meaning_elem.text

            name_output.append({
                "name": name_text,
                "meaning": meaning_text,
                "url": scrapable['url']
            })
            scrapable['meaning'] = meaning_text
            if len(name_output) > 20:
                print(f"saving progress, from name {name_output[0]['name']} to {name_output[-1]['name']}")
                save_names_raw(rescraped_filename, name_output)
                save_names_raw(rescraped_remaining_filename, scrapables, overwrite=True)
                name_output = []
        except NoSuchWindowException or WebDriverException:
            print(f"window was closed. continuing on the next one")
            driver = webdriver.Firefox()

    driver.close()


def remove_duplicate_rescrapables():
    names = {}
    with open(rescrape_list_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        number_skipped = 0
        for row in csvreader:
            if row['url'] in names and names[row['url']] is not None:
                number_skipped = number_skipped + 1
            else:
                names[row['url']] = row
        print(f"removed {number_skipped} duplicates")
    return list(names.values())


def remove_duplicate_scraped():
    names = {}
    with open(initial_scraped_filename) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        number_skipped = 0
        for row in csvreader:
            key = f"{row['name']}_{row['origin']}"
            if key in names and names[key] is not None:
                number_skipped = number_skipped + 1
            else:
                names[key] = row
        print(f"removed {number_skipped} duplicates")
    return list(names.values())


def merge_meanings():
    names_without_meaning = []
    names_result = []
    with open(initial_scraped_filename, mode='r') as scraped:
        csvreader = csv.DictReader(scraped, delimiter=',', quotechar='"')
        for row in csvreader:
            name = row['name']
            if row['meaning'].strip() is '':
                names_without_meaning.append({'name': name,
                                 'gender': row['gender'],
                                 'origin': row['origin'],
                                 'url': row['url']})
            else:
                names_result.append({'name': name,
                                 'gender': row['gender'],
                                 'origin': row['origin'],
                                 'meaning': row['meaning'],
                                 'url': row['url']})

    with open(rescraped_filename, mode='r') as rescraped_file:
        csvreader = csv.DictReader(rescraped_file, delimiter=',', quotechar='"')
        for row in csvreader:
            # find the first entry with the same name with an empty meaning
            for name in names_without_meaning:
                if name['name'] == row['name']:
                    # add the meaning and URL
                    name['meaning'] = row['meaning']
                    name['url'] = row['url']
                    names_result.append(name)
                    names_without_meaning.remove(name)
                    break
    return names_result


def main():
    # scrape()

    # recrapables = remove_duplicate_rescrapables()
    # recrapables_df = pd.DataFrame(recrapables, columns=['name', 'url'])
    # save_names_raw(rescrape_list_filename, recrapables_df, overwrite=True)
    #
    # scraped = remove_duplicate_scraped()
    # scraped_df = pd.DataFrame(scraped, columns=['name','gender','origin','meaning'])
    # save_names_raw(output_filename, scraped_df, overwrite=True)
    #
    # saved_count = count_lines(output_filename)
    # rescrapables_count = count_lines(rescrape_list_filename)
    # print(f"Saved {saved_count} names from meaning-of-names.com, {rescrapables_count} need deep scraping")

    # deep_scrape()
    merged_names = merge_meanings()
    merged_df = pd.DataFrame(merged_names, columns=['name', 'gender', 'origin', 'meaning', 'url'])
    save_names_raw(merged_output_filename, merged_df, overwrite=True)
    total_name_count = count_lines(merged_output_filename)
    print(f"Got a total of {total_name_count} names from meaning-of-names.com")


if __name__ == "__main__":
    main()
