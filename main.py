import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Subdivision_Address(name):

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(
        'F:\\projects\\revenue_stlouisco_com\\chromedriver.exe', options=options)
    driver.maximize_window()
    driver.get("https://revenue.stlouisco.com/IAS/index.htm")
    page_title=driver.title
    wait=WebDriverWait(driver, 50)

    try:
        if page_title=="Real Estate Information":
            print(driver.title)
            Subdivision_Name_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "butFind"))
            )
            address_table =wait.until(
                EC.presence_of_element_located((By.ID, "panelData"))
            )

            print(Subdivision_Name_btn,address_table)
        else:
            print("We are not on Target Yet solve captcha by yourself lol",driver.title)
            time.sleep(50)
            driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='SearchInput']"))
            # SearchInputForm = wait.until(
            #     EC.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='SearchInput']"))
            # )
            rbutSubdivision_radio_element=driver.find_element(By.ID,'rbutSubdivision')

            driver.execute_script("arguments[0].click();", rbutSubdivision_radio_element)

            rbutSubdivision_input_element = driver.find_element(By.ID, 'tboxSubdivision')

            rbutSubdivision_input_element.clear()
            rbutSubdivision_input_element.send_keys(name)

            butFind_input_element = driver.find_element(By.ID, 'butFind')
            driver.execute_script("arguments[0].click();", butFind_input_element)
            driver.switch_to.default_content()
            time.sleep(50)
            driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='SearchResults']"))
            address_trs=driver.find_elements(By.XPATH,'//table[@id="tableData"]/tbody/tr')
            for address in address_trs:

                tds_elements=address.find_elements(By.XPATH,'//td')
                Row_Number=tds_elements[0].text
                Map_link=tds_elements[1].text
                Locator_Number=tds_elements[2].text
                Subdivision_Name=tds_elements[3].text
                Owner_Name=tds_elements[4].text
                print(Row_Number,Map_link,Locator_Number,Subdivision_Name,Owner_Name)
            driver.switch_to.default_content()
            print("Job Done ! HappyCode! LeaderMalang")


            #rbutSubdivision_radio.click()

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Subdivision_Address('mason forest')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
