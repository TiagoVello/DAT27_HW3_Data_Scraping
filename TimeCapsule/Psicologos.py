import pandas
import requests     
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#regioes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
regioes = ['01']
stop_item = '\nTotal de Registros:'
colunas = ['N° Registro', 'Nome', 'Data', 'Situação', 'Região']
dado = []
registro = []
nome = []
data = []
situacao = []
localizacao = []
data_frame = pandas.DataFrame(columns=colunas)

def add_to_data_frame(dado):
    global data_frame
    for item in range(len(dado)):
        if (item%5 == 0):
            registro.append(dado[item])
        elif (item%5 == 1):
            nome.append(dado[item])
        elif (item%5 == 2):
            data.append(dado[item])
        elif (item%5 == 3):
            situacao.append(dado[item])
        elif (item%5 == 4):
            localizacao.append(dado[item])
    dado_lista = [registro, nome, data, situacao, localizacao]
    pagina_dado = pandas.DataFrame(dict(zip(colunas, dado_lista)))
    data_frame = data_frame.append(pagina_dado, ignore_index=True)
    return

browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(2)

for regiao in regioes:
    browser.get(r'http://cadastro.cfp.org.br/siscafweb/carregaConselho.do?tipoAcesso=4&s=1&tipoConsulta=pf&controle=0&sigla=cfp&ini=1')
    inputbox = browser.find_element_by_xpath(r'//*[@id="regiaoConselho"]')   
    inputbox.send_keys(regioes)
    inputbox.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(r'//*[@id="btnSubmitForm"]').click()
    browser.implicitly_wait(2)
    for page in range(2):
        info = browser.find_elements_by_tag_name('td')
        counter = 0
        for item in info:
            if (stop_item in item.text):
                break
            if (counter > 4):
                dado.append(item.text)
            counter += 1
        add_to_data_frame(dado)
        browser.find_element_by_xpath(r'/html/body/table[4]/tbody/tr/td/table/tbody/tr/td[3]/font/a[1]').click()
        browser.implicitly_wait(2)
browser.close()


        