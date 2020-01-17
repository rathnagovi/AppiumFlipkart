
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import pytest
import os

class TestLogin():
    @pytest.fixture(scope="class")

    def setup(self):
        app = os.path.abspath("C:\\Users\\Rathnagovi\\Downloadscom.flipkart.android_6.17-1041400_minAPI16(armeabi-v7a)(nodpi)_apkmirror.com.apk",)
        driver = webdriver.Remote("http://localhost:4723/wd/hub",

              desired_capabilities={
              "deviceName": "Android Emulator",
              "platformName": "Android",
              "appPackage": "com.flipkart.android",
              "appWaitActivity": "com.flipkart.android.activity.MSignupActivity",
              "app": "C:\\Users\\Rathnagovi\\Downloadscom.flipkart.android_6.17-1041400_minAPI16(armeabi-v7a)(nodpi)_apkmirror.com.apk",
              "automationName":"uiautomator2",
            })


    def teardown(self):
        self.driver.quit()

    def test_Login(self):
        self.driver.implicitly_wait(30)

        #close the popup
        self.driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

        #Interact with textbox
        self.driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
        self.driver.find_element_by_id("com.flipkart.android.id/search_autoCompleteTextView").send_Keys("iphone")

        #Get the price of the first laptop and verify the price

        self.driver.find_element_by_xpath("//andriod.widget.ImageButton[@content-desc='Drawer']").click()
        self.driver.find_element_by_xpath("//andriod.widget.TextView[@text='Electronics']").click()
        self.driver.find_element_by_xpath("//andriod.widget.TextView[@text='Laptops']").click()
        self.driver.find_element_by_xpath("//andriod.widget.TextView[@bounds='[0,0] [720,48]']").click()
        self.driver.find_element_by_id("com.flipkart.android:id/tv_card_view_holder").click()
        self.driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

        """
        Touch Actions
        """
        def test_touchAct(self):
            touch=TouchAction(self)
            touch.press(x=318, y=972).move_to(x=338, y=476).release().perform()

            for i in range(5):# repeating 5 time(scroll up and down 5 times
                # their is three reusable methods minium scroll,max scroll,long scroll only in android
                touch = TouchAction(self)
                touch.press(x=318, y=972).move_to(x=338, y=476).release().perform()
        time.sleep(5)


        def tes_takescreenshots(self):
            ts =time.strftime("%Y_%m_%d_%H%H%S")
            activityname = self.current_activity
            filename =activityname+ts
            self.driver.save_screenshots("C:\Users\Rathnagovi\PycharmProjects\AppiumSandbox\Screenshots/"+filename+".png")

