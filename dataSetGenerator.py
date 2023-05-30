from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
 
# What you enter here will be searched for in
# Google Images
query = "dogs"
 
# Creating a webdriver instance
driver = webdriver.Chrome('./chromedriver_win32_new/chromedriver.exe')
 
# Maximize the screen
driver.maximize_window()
 
# Open Google Images in the browser
driver.get('https://images.google.com/')
 
# Finding the search box
driver.maximize_window() 
#driver.implicitly_wait(20)
box = driver.find_element("xpath",'//*[@id="APjFqb"]')
 
# Type the search query in the search box
box.send_keys(query)
 
# Pressing enter
box.send_keys(Keys.ENTER)
 

html = driver.find_element(By.TAG_NAME, 'html')

# Function for scrolling to the bottom of Google
# Images results

#//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[24]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[29]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[35]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[36]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[43]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[42]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[51]/div[1]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[51]/div[2]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[51]/div[46]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[51]/div[48]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[52]/div[48]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[52]/div[51]/a[1]/div[1]/img

#//*[@id="islrg"]/div[1]/div[52]/div[91]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[53]/div[2]/a[1]/div[1]/img

#//*[@id="islrg"]/div[1]/div[52]/div[102]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[52]/div[104]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[53]/div[1]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[54]/div[92]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[54]/div[98]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[54]/div[103]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[55]/div[1]/a[1]/div[1]/img
#//*[@id="islrg"]/div[1]/div[55]/div[45]/a[1]/div[1]/img


def screenshotImages(imageCount):
    print("image count is: ", imageCount)
    for i in range(imageCount, imageCount+30):
    # range(1, 50) will capture images 1 to 49 of the search results
    # You can change the range as per your need.
        imagePath = ''
        if i < 51:
            imagePath = '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img'
        elif i >= 51 and i < 104:
            j = i - 50
            imagePath = '//*[@id="islrg"]/div[1]/div[51]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 104 and i < 208:
            j = i - 103
            imagePath = '//*[@id="islrg"]/div[1]/div[52]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 208 and i < 312:
            j = i - 207
            imagePath = '//*[@id="islrg"]/div[1]/div[53]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 312 and i < 416:
            j = i - 311
            imagePath = '//*[@id="islrg"]/div[1]/div[54]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 416 and i < 520:
            j = i - 415
            imagePath = '//*[@id="islrg"]/div[1]/div[55]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 520 and i < 624:
            j = i - 519
            imagePath = '//*[@id="islrg"]/div[1]/div[56]/div['+str(j)+']/a[1]/div[1]/img'
        elif i >= 624 and i < 728:
            j = i - 623
            imagePath = '//*[@id="islrg"]/div[1]/div[57]/div['+str(j)+']/a[1]/div[1]/img'

        try:
            # XPath of each image
            img = driver.find_element("xpath", imagePath)
            driver.execute_script("window.scrollTo(0,0)") 
            a = img.location
            driver.execute_script("window.scrollTo(0,"+str((a['y'])-50)+")") 
            driver.execute_script("window.scrollTo(0,"+str(a['y'])+")") 
            #time.sleep(0.3)
            #print(img)
            # Enter the location of folder in which
            # the images will be saved
            img.screenshot('TestImages' + 
                        query + ' (' + str(i) + ').png')
            
            # Each new screenshot will automatically
            # have its name updated
    
            # Just to avoid unwanted errors
            time.sleep(0.2)
 
        except:
            # if we can't find the XPath of an image,
            # we skip to the next image
            continue
        print(imagePath)

def takeScreenShots(imageCount):
    for i in range(0, 24):
        screenshotImages(imageCount)
        imageCount+=30


def scroll_to_bottom():

    last_height = driver.execute_script('\
    return document.body.scrollHeight')
 
    while True:
        driver.execute_script('\
        window.scrollTo(0,document.body.scrollHeight)')
 
        # waiting for the results to load
        # Increase the sleep time if your internet is slow
        time.sleep(3)
 
        new_height = driver.execute_script('\
        return document.body.scrollHeight')


        # click on "Show more results" (if exists)
        try:

            driver.find_element("xpath", '//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input').click()
 
            # waiting for the results to load
            # Increase the sleep time if your internet is slow
            time.sleep(3)
 
        except:
            print("didnt work!")
            pass
 
        # checking if we have reached the bottom of the page
        if new_height == last_height:
            break
 
        last_height = new_height
 
 
# Calling the function
 
# NOTE: If you only want to capture a few images,
# there is no need to use the scroll_to_bottom() function.
scroll_to_bottom()
# Loop to capture and save each image
imageCount = 1
takeScreenShots(imageCount)

# Finally, we close the driver
driver.close()