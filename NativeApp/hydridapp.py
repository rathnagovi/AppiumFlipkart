from appium import webdriver

desired_cap ={
    "deviceName":"Andriod Emulator",
     "platformName":"Android",
    "appPackage":"com.google.android.apps.nexuslauncher",
    "appWaitActivity":"com.google.android.apps.nexuslauncher.NexusLauncherActivity" ,
     "avd": "NexusEmu",
     "avdLaunchTimeout": 150000,


}
driver =webdriver.Remote(("http://localhost:4723/wd/hub",desired_cap))
driver.find_element_by_id("com.google.android.apps.nexuslauncher:id/icon").click()
driver.find_element_by_id("com.google.android.googlequicksearchbox:id/search_box").send_keys("https://www.Amazon.com")
#driver.find_element_by_id("com.google.android.sumbit").click()
print(driver.page_source)


