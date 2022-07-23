from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def gen_html(html):
    driver = webdriver.Chrome(executable_path=".\\chromedriver.exe")
    driver.maximize_window()
    driver.get(html)
    # identify elements with tagname <a>
    conta =1

    try:
        links = open('links.txt', 'w')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "wc-endpoint")))
        lnks = driver.find_elements_by_tag_name("a")

        for lnk in lnks:
            if 'index=' + str(conta) in str(lnk.get_attribute('href')):
                # get_attribute() to get all href
                conta = conta + 1
                links.write(lnk.get_attribute('href') + '\n')
        links.close()
        driver.quit()
    finally:

        driver.quit()
