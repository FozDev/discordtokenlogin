from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

with open('payment.txt', 'r+') as f:
    tokens = f.read().splitlines()

tokens.sort()

for token in tokens:
    driver = webdriver.Chrome()
    driver.get("http://discord.com/login")
    driver.execute_script('''
let token = "''' + token + '''";

function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }

login(token);
    ''')
    input("Done? ")
    driver.close()
