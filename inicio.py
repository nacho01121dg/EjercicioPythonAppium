from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:app": "D:\\Mely\\Descargas\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.swaglabsmobileapp",
  "appium:appActivity": "com.swaglabsmobileapp.MainActivity"
}

url = "http://localhost:4723/wd/hub"
usuario = 'standard_user'
password = 'secret_sauce'
espera = 30

driver = webdriver.Remote(url, desired_cap)
driver.implicitly_wait(espera)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Usuario').send_keys(usuario)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Contraseña').send_keys(password)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()

driver.quit()
