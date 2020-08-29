from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import unidecode

urls =[ "https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674",
"https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br",
"https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br",
"https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br",
"https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br",
"https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br",
"https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br" ]


for url in urls :

    driver = webdriver.Chrome(executable_path=  "C://Program Files//chromedriver//chromedriver.exe")
    driver.get(url)
    time.sleep(1)

    section = driver.find_elements_by_tag_name('section')
    element_html = section[0].get_attribute("outerHTML")
    soup = BeautifulSoup(element_html, 'html.parser')

    h1 = driver.find_elements_by_tag_name('h1')
    second_element = h1[0].get_attribute("outerHTML")
    title = BeautifulSoup(second_element, 'html.parser').getText()

    three_element = driver.find_elements_by_tag_name('section')
    second_element = h1[0].get_attribute("outerHTML")

    corpo = driver.find_element_by_tag_name('body')
    element = corpo.get_attribute("outerHTML")
    corpo_soup = BeautifulSoup(element, 'html.parser')
    autor = corpo_soup.find("div", {'class': 'f:.9 m-b:.4 m-t:.5 d:i-b'}).getText()

    text = []
    for div in soup.find_all("div", {"class": "Grid"}):
        div_text = div.find("div", {"class": "flx-s:1"})
        for a in div_text.find_all("a"):
            text.append(a.getText())
        text.append('\n')

    text_final = " ".join(text)

    with open('ted'+str(urls.index(url))+'.json', 'w') as f:
        json.dump({"author": autor, "body": text_final,"title": title,   "type": "video", "url": url}, f)

    driver.quit()

