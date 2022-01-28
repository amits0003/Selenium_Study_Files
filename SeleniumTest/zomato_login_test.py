# import the libs
from selenium import webdriver
from time import sleep

# create the initial window
driver = webdriver.Chrome(executable_path="C:\\Users\\amit_pc\\Documents\\Study materials\\python\\Seleium\\chromedriver.exe")

# go to the home page
driver.get('https://www.zomato.com')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# wait for page to load completely
sleep(5)

# click on the sign in tab
driver.find_element_by_xpath("//a[contains(text(),'Log in')]").click()

sleep(5)

# click to log in using Google
driver.find_element_by_xpath("//span[contains(text(),'Continue with Google')]").click()

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

# change the control to signin page
driver.switch_to.window(login_page)

# user input for email and password
print('Enter email id : ', end='')
email = input().strip()
print('Enter password : ', end='')
password = input().strip()

# enter the email
driver.find_element_by_xpath("//div[contains(text(),'Email or phone')]").send_keys(email)
driver.find_element_by_xpath('//*[@id ="u_0_0"]').click()
# enter the password
driver.find_element_by_xpath("//div[contains(text(),'Enter password')]").send_keys(password)

# click the login button
driver.find_element_by_xpath('//*[@id ="u_0_0"]').click()

# change control to main page
driver.switch_to.window(main_page)

sleep(10)
# print user name
name = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/div/span').text
print('Your user name is : {}'.format(name))

# closing the window
#driver.quit()
