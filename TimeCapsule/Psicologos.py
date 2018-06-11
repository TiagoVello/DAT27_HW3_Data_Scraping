

import pandas    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys    

browser = webdriver.Chrome('chromedriver.exe')
browser.implicitly_wait(0.5)

def add_to_data_frame(dado):
    global data_frame
    global colunas
    registro = []
    nome = []
    data = []
    situacao = []
    localizacao = []
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

# Retorna o índice da ultima pagina de cada localização
def last_page_index():
    global browser
    index = browser.find_element_by_xpath(r'/html/body/table[4]/tbody/tr/td/table/tbody/tr/td[3]/font/a[2]').get_attribute('href')[-16:-11]
    index = index.replace('a','')
    index = index.replace('n','')
    index = int(index.replace('=',''))
    return index

# Retorna uma base de dados com todos os Psicólogos do Brasil
def data(): 
    
    regioes = [ '06', '02', '03', '04', '05', '07', '08', '09', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21','22', '23']
    stop_item = '\nTotal de Registros:'
    colunas = ['N° Registro', 'Nome', 'Data', 'Situação', 'Região']
    

    data_frame = pandas.DataFrame(columns=colunas)

    for regiao in regioes:
        
        # Entra no site raiz e faz uma busca por região
        browser.get(r'http://cadastro.cfp.org.br/siscafweb/carregaConselho.do?tipoAcesso=4&s=1&tipoConsulta=pf&controle=0&sigla=cfp&ini=1')
        browser.implicitly_wait(0.5)
        inputbox = browser.find_element_by_xpath(r'//*[@id="regiaoConselho"]')   
        inputbox.send_keys(regiao)
        inputbox.send_keys(Keys.ENTER)
        browser.find_element_by_xpath(r'//*[@id="btnSubmitForm"]').click()
        
        # busca os dados, formata eles e monta uma tabela
        last_page = last_page_index() - 1
        for page in range(last_page):
            info = browser.find_elements_by_tag_name('td')
            counter = 0
            dado = []
            for item in info:
                if (stop_item in item.text):
                    break
                if (counter > 4):
                    dado.append(item.text)
                counter += 1
            add_to_data_frame(dado)
            if (page != last_page_index):
                browser.find_element_by_xpath(r'/html/body/table[4]/tbody/tr/td/table/tbody/tr/td[3]/font/a[1]').click()
                
    browser.close()
    return data_frame

        