import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LinkedInBot:
    def __init__(self,username,password,users,message):
        self.username = username
        self.password = password
        self.users = users
        self.message = message
        self.bot = webdriver.Chrome()

        self.login()

    def login(self):
        #Get login url
        self.bot.get('https://www.linkedin.com/login')

        #Enter username and password
        username_field = WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.ID,'username')))
        username_field.send_keys(self.username)

        password_field = WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.ID,'password')))
        time.sleep(5)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

        #Wait for 5 seconds

        time.sleep(5)

        self.send_message()

    def send_message(self):
        for user in self.users:
            #Get user profile
            self.bot.get(user)

            try:
                message_btn = WebDriverWait(self.bot,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[1]')))
                message_btn.click()

                time.sleep(2)

                message_box = WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.msg-form__contenteditable')))

                #Remove pre entered message
                message_box.send_keys(Keys.BACKSPACE)
                #Type a message
                message_box.send_keys(self.message)

                #Press send button to send message
                send_btn = WebDriverWait(self.bot,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.msg-form__send-button')))
                send_btn.click()

                time.sleep(2)
                print(f'Message successfully sent to {user}')

            except Exception as e:
                print(f'Failed to send message to {user} : {str(e)}')

def main():
    username ='abc@gmail.com'
    password ='abc@123'

    users =['https://www.linkedin.com/in/user-1','https://www.linkedin.com/in/user-1']

    message = 'Hi there! 👋 How are you ? I hope you’re doing well. Its been long since we connected \n Note: This is a testing message sent by LinkBot🤖'

    bot = LinkedInBot(username,password,users,message)

if __name__ == '__main__':
    main()

