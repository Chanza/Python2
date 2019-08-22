
'''Opening Browser
import webbrowser
new = 2
url = "https://www.youtube.com"
webbrowser.open(url,new=new)
True'''


from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.youtube.com')


try:
    # find text
    eleml = driver.find_element_by_link_text("Trending")
    eleml.click()

    eleml2 = driver.find_element_by_link_text("Music")
    eleml2.click()

except Exception as e:
    print('Exception',format(e))
    print('Text or Link not found')


















