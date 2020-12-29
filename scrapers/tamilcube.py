import os
import pandas as pd

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

output_filename = os.path.join("name_lists", "tamilcube_scraped_names.csv")


def save_names(names_dict):
    df = pd.DataFrame.from_dict(names_dict)
    with open(output_filename, "a") as csvfile:
        df.to_csv(csvfile, header=False)


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive.
    https://stackoverflow.com/a/7001371/940217
    """
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


langs = [
    "Tamil",
    "Malayalam",
    "Sanskrit",
    "Telugu",
    "Muslim",
    "Bengali",
    "Marathi",
    "Punjabi"
]
gender_switch = [{"gender": "Boy", "url_parameter": ""},
                 {"gender": "Girl", "url_parameter": "baby=g&"}]


def scrape():
    name_output = []
    driver = webdriver.Firefox()
    for l in langs:
        language = l
        for letter in char_range('A', 'Z'):
            for gender in gender_switch:
                gender_parameter = gender["url_parameter"]
                site_url = f"http://tamilcube.com/babynames/{language.lower()}-baby-names.aspx?{gender_parameter}term={letter}"
                print(f"scraping site: {site_url}")
                driver.get(site_url)
                assert language in driver.title
                paging = True
                number_of_pages = 1
                number_of_names = 0
                while paging:
                    names_found = True
                    name_index = 0
                    while names_found:
                        try:
                            name_elem = driver.find_element_by_id(f"ListView1_Label1_{name_index}")
                            name_meaning_elem = driver.find_element_by_id(f"ListView1_Label2_{name_index}")
                            name_output.append({
                                "name": name_elem.text,
                                "gender": gender['gender'],
                                "language": language,
                                "meaning": name_meaning_elem.text
                            })
                            name_index = name_index + 1
                        except NoSuchElementException as nse:
                            print(nse)
                            print(
                                f"No more names found on this page for {language} and letter {letter}, found {name_index} names")
                            names_found = False

                    try:
                        # next_btn = driver.find_element_by_xpath("//a[@class=\"btn btn-primary btn-md\" and text()=' > ']")
                        paging_button_wrapper = driver.find_element_by_id("DataPager2")
                        next_btn = paging_button_wrapper.find_element_by_xpath(".//a[text()=' > ']")
                        save_names(name_output)
                        number_of_names = number_of_names + len(name_output)
                        name_output = []
                        if 'aspNetDisabled' in next_btn.get_attribute("class").split(" "):
                            paging = False
                            break
                        next_btn.click()
                        number_of_pages = number_of_pages + 1
                    except NoSuchElementException:
                        paging = False
                print(f"reached end of the list for this page, saw {number_of_pages} pages and {number_of_names} names")

    driver.close()
    return name_output


def main():
    print("beginning scrape of tamilcube.com")
    scrape()


if __name__ == "__main__":
    main()
