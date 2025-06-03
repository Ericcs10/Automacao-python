from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    rodar_automacao(filepath)
    return 'Automação finalizada com sucesso!'

def rodar_automacao(filepath):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    time.sleep(2)

    # Login
    driver.find_element(By.NAME, 'email').send_keys('pythonimpressionador@gmail.com')
    driver.find_element(By.NAME, 'senha').send_keys('sua senha')
    driver.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)

    # Cadastrar produtos
    tabela = pd.read_csv(filepath)
    for i, row in tabela.iterrows():
        driver.find_element(By.NAME, 'codigo').send_keys(str(row['codigo']))
        driver.find_element(By.NAME, 'marca').send_keys(str(row['marca']))
        driver.find_element(By.NAME, 'tipo').send_keys(str(row['tipo']))
        driver.find_element(By.NAME, 'categoria').send_keys(str(row['categoria']))
        driver.find_element(By.NAME, 'preco_unitario').send_keys(str(row['preco_unitario']))
        driver.find_element(By.NAME, 'custo').send_keys(str(row['custo']))
        if not pd.isna(row['obs']):
            driver.find_element(By.NAME, 'obs').send_keys(str(row['obs']))
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(1)

    driver.quit()

if __name__ == '__main__':
    app.run(debug=True)
