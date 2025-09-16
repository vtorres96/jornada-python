from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# abrir o navegador
driver = webdriver.Chrome()
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# login
driver.find_element(By.ID, "email").send_keys("pythonimpressionador@gmail.com")
driver.find_element(By.ID, "password").send_keys("sua senha")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# esperar a página carregar
time.sleep(3)

# importar tabela
tabela = pd.read_csv("produtos.csv")

# loop para cadastrar
for _, linha in tabela.iterrows():
    driver.find_element(By.ID, "codigo").send_keys(str(linha["codigo"]))
    driver.find_element(By.ID, "marca").send_keys(str(linha["marca"]))
    driver.find_element(By.ID, "tipo").send_keys(str(linha["tipo"]))
    driver.find_element(By.ID, "categoria").send_keys(str(linha["categoria"]))
    driver.find_element(By.ID, "preco_unitario").send_keys(str(linha["preco_unitario"]))
    driver.find_element(By.ID, "custo").send_keys(str(linha["custo"]))
    
    if not pd.isna(linha["obs"]):
        driver.find_element(By.ID, "obs").send_keys(str(linha["obs"]))

    # submeter
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)
