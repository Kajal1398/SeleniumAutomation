from selenium import webdriver

import time
driver = webdriver.Chrome("C:\\Users\\Archana\\Desktop\\Web App with Go\\Testing\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.maximize_window()

print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 1                                   |")
print("|Expected Output : Should Open login page|             |")
driver.get("https://mysterious-shelf-22386.herokuapp.com/")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 2                                   |")
print("|Expected Output : Should Enter user name(archanacmahajan@gmai.com)|")
time.sleep(3)
driver.find_element_by_name("email").send_keys("archanacmahajan@gmai.com")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 3                                   |")
print("|Expected Output : Should Enter Password(archanacmahajan)|")
time.sleep(2)
driver.find_element_by_name("psw").send_keys("archanacmahajan")
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 4                                   |")
print("|Expected Output : Should Click Login Button           |")
time.sleep(2)
driver.find_element_by_name("test").click()
print("|Result          : Pass                                |")
print("|******************************************************|")


print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 5                                   |")
print("|Expected Output : Should Click know more button       |")
time.sleep(8)
driver.find_element_by_xpath("/html/body/form/center/table/tbody/tr[1]/td[2]/input").click()
print("|Result          : Pass                                |")
print("|******************************************************|")

print("|******************************************************|")
print("|                                                      |")
print("|Test ID         : 6                                   |")
print("|Expected Output : Should Close Browser                |")
time.sleep(4)
driver.quit()
print("|Result          : Pass                                |")
print("|******************************************************|")



