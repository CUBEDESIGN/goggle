from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://forms.gle/vWVmojtWdfFvEj8V6')

time.sleep(1)

datas = [
    ['Mary D Joiner', 'MaryDJoiner@gmail.com', '4079025063', '2474 McDonald Avenue, Maitland', 'NA'],
    ['Karen B Johnson', 'KarenBJohnson@gmail.com', '3153437575', '2143 Oak Street, GRAND ISLE', 'NA']
]

textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
textareaboxes = driver.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")

for data in datas:
    count = 0
    for value in textboxes:
        value.send_keys(data[count])
        count += 1

    for value in textareaboxes:
        value.send_keys(data[count])
        count += 1

submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
submit.click()     

driver.quit()
