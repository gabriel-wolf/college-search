
sitemit='https://www.niche.com/colleges/massachusetts-institute-of-technology/'

def inputget():
    uinput=input("Enter College: ")

    if uinput == "mit":
        uinput = 'massachusetts institute of technology'
    if uinput == "brown":
        uinput = 'brown university'
    elif uinput == "STOP":
        exit(0)

    uinput = uinput.replace(' ','-')

    site='https://www.niche.com/colleges/' + uinput + '/'

    print(site)
    return site




import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.PhantomJS(executable_path='C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.set_window_size(1120, 550)



while True:
    browser.get(inputget())
    browser.save_screenshot('college-page.png')

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')


    # print(soup.prettify)

    print("\n\n")

    title = soup.find(class_="postcard__title").get_text()
    print(title)

    badge = soup.find(class_="postcard__badge").get_text()
    print(badge)

    print("Location: " + str(browser.find_element_by_xpath(
        "/html/body/div/div/section/main/div/div[1]/header/header/div/div[2]/div[1]/ul/li[3]"
    ).text))

    print("Overall Grade: " + str(browser.find_element_by_xpath(
        "/html/body/div/div/section/main/div/div[1]/header/header/div/div[2]/div[1]/ul/li[1]/div/div"
    ).text))

    attrib = soup.find(class_="postcard__attrs").get_text()
    # print(attrib)

    print("Acceptance rate: " + str(browser.find_element_by_xpath("/html/body/div/div/section/main/div/div[2]/div/div[2]/section[5]/div[2]/div[1]/div/div/div/div[2]/span").text))

    print("SAT: " + str(browser.find_element_by_xpath("/html/body/div/div/section/main/div/div[2]/div/div[2]/section[5]/div[2]/div[3]/div/div/div[1]/div[2]/span").text))
    print("Cost per year: " + str(browser.find_element_by_xpath("/html/body/div/div/section/main/div/div[2]/div/div[2]/section[7]/div[2]/div[1]/div/div[1]/div[2]/span[1]").text))

    print("Most popular major: " + str(browser.find_element_by_xpath(
        "/html/body/div/div/section/main/div/div[2]/div/div[2]/section[9]/div[2]/div[1]/div/div/div/div[2]/ul/li[1]/div/h6"
    ).text))







    # print(soup.find_element_by_xpath('/html/body/div/div/section/main/div/div[1]/header/header/div/div[2]/div[1]/div[2]/a').get_text())


    # tagline = browser.find_element_by_xpath("/html/body/div/div/section/main/div/div[1]/header/header/div/div[2]/div[1]/div[2]/a")
    # print(tagline)


    # location = soup.find(class_="vk_gy vk_h")
    # print(location.get_text())
    # browser.find_element_by_xpath("/html/body/div[3]/span/span/span/div/div/div/ul/li[2]/span/a").click()
