import time

from .webdriver import Chrome

class PhoneNumber:
    google_url = 'https://google.com/'
    
    def serchPhoneNum(self, contents, target_row, other_write_row):
        resolt_contents = []
        
        ch = Chrome()
        with ch.driver as driver:
            
            for content in contents:
                serach_word = content[target_row] + ' 電話番号'
                driver.get(self.google_url)
                serach_form = driver.find_element_by_name('q')
                serach_form.send_keys(serach_word)
                serach_form.submit()
                try:
                    phone_number = driver.find_element_by_class_name('mw31Ze').text
                except Exception:
                    # phone_number = None
                    phone_number = ''
                finally:
                    resolt_content = []
                    for row in other_write_row:
                        resolt_content.append(content[row])
                    resolt_content.append(phone_number)
                    
                    resolt_contents.append(resolt_content)
                    time.sleep(1)
            
        return resolt_contents
    

class Address:
    google_url = 'https://google.com/'
    
    def serchAddress(self, contents, target_row, other_write_row):
        resolt_contents = []
        
        ch = Chrome()
        with ch.driver as driver:
            
            for content in contents:
                serach_word = content[target_row] + ' 住所'
                driver.get(self.google_url)
                serach_form = driver.find_element_by_name('q')
                serach_form.send_keys(serach_word)
                serach_form.submit()
                try:
                    address = driver.find_element_by_class_name('MWXBS').text
                except Exception:
                    try:
                        address = driver.find_element_by_class_name('FgU48e').text
                    except Exception:
                        # address = None
                        address = ''
                finally:
                    resolt_content = []
                    for row in other_write_row:
                        resolt_content.append(content[row])
                    resolt_content.append(address)
                    
                    resolt_contents.append(resolt_content)
                    time.sleep(1)
            
        return resolt_contents