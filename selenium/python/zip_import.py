import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import datetime

class Importing(unittest.TestCase):
    '''
    This test...
      * Creates a module called "Selenium Test Page" plus the date and time
      * imports a zip file
      * publishes the module

    '''


    def setUp(self):
        self.driver = webdriver.Firefox()
        # chrome driver option
        #self.driver = webdriver.Chrome('/home/ew2/PycharmProjects/chromedriver')
        propfile = open('properties.ini')
        items = [line.rstrip('\n') for line in propfile]
        self.authkey = items[0]
        self.pw = items[1]
        self.url = items[2]
        self.zip = items[3]

    def tearDown(self):
        #self.driver.save_screenshot('publishing-test.png')
        self.driver.quit()

    def test_importing(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(300)
        #login
        authKey = self.driver.find_element_by_id('__ac_name')
        authKey.send_keys(self.authkey)
        pw = self.driver.find_element_by_id('__ac_password')
        pw.send_keys(self.pw)
        signin = self.driver.find_element_by_name('submit')
        signin.click()
        self.driver.implicitly_wait(300)
        #create module
        create_link = self.driver.find_element_by_link_text('Create a new module')
        create_link.click()
        checkbox = self.driver.find_element_by_name('agree')
        checkbox.click()
        next = self.driver.find_element_by_name('form.button.next')
        next.click()
        name = self.driver.find_element_by_name('title')
        name.clear()
        name.send_keys('Selenium Test Page ' + str(datetime.datetime.now()))
        try:
            next = self.driver.find_element_by_name('form.button.next')
            next.click()
            self.driver.implicitly_wait(300)
        except WebDriverException:
            #getting popup error everytime so this is a workaround
            pass

        #get to import zip page
        zip_import = self.driver.find_element_by_name('format')
        for option in zip_import.find_elements_by_tag_name('option'):
            if option.text == 'Zip File':
                option.click()
                break
        import_button = self.driver.find_element_by_name('import')
        import_button.click()
        #upload zip file
        upload_zip = self.driver.find_element_by_name('importFile')
        #upload_zip.click()
        upload_zip.send_keys(self.zip)
        upload_button = self.driver.find_element_by_name('submit')
        upload_button.click()
        #publish
        publish_link = self.driver.find_element_by_css_selector('#portlet-logaction > dd.portletItem.even > ul > li > a')
        publish_link.click()
        publish_button = self.driver.find_element_by_name('form.button.publish')
        publish_button.click()
        confirm = self.driver.find_element_by_name('publish')
        confirm.click()


if __name__ == "__main__":
    unittest.main()
