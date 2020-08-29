from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import unidecode

urls =["https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972",
"https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786",
"https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772",
"https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683"
]

for url in urls:

    driver = webdriver.Chrome(
        executable_path="C:/Program Files/chromedriver/chromedriver.exe")
    driver.get(url)
    time.sleep(1)

    body = driver.find_element_by_tag_name('body')
    body = body.get_attribute('outerHTML')

    soup = BeautifulSoup(body, 'html.parser')

    # Title
    title = soup.find('h1', { 'class': 'mat-tit' }).getText()

    # Autor
    autor = soup.find('span', { 'class': 'meta-item meta-aut' }).getText()

    # Corpo
    div_text = soup.find('div', { 'class': 'mat-txt' })

    text = []
    for p in div_text.findAll('p'):
        text.append(f'{p.getText()}\n')

    text_final = " ".join(text)

    with open('olhar_digital'+str(urls.index(url))+'.json', 'w') as file:
        json.dump({"author": autor, "body": text_final, "title": title, "type": "article", "url": url}, file)

    driver.quit()