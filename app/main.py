import time

from fastapi import FastAPI, File, UploadFile
from amazoncaptcha import AmazonCaptcha
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

app = FastAPI()


@app.get("/")
async def root():
    return "小老弟！你好"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/captcha/link")
async def captcha(link: str):
    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()
    return {
        "success": True,
        "data": solution
    }
@app.post("/captcha/image")
async def captcha(file: UploadFile = File):
    captcha = AmazonCaptcha(file)
    solution = captcha.solve()
    return solution

@app.get("/captcha/local_image_link")
async def captcha(link: str):
    print(link)
    captcha = AmazonCaptcha.fromlink(link)
    solution = captcha.solve()
    return {
        "success": True,
        "data": solution
    }

# @app.get("/amazon/product")
# async def captcha(link: str):
#     co=Options()
#     co.add_argument('--headless')
#     co.add_argument('--no-sandbox')
#     co.add_argument('--disable-gpu')
#     #brower = webdriver.Chrome(chrome_options=co,executable_path = '/usr/bin/chromedriver')
#     productInto = {}
#     try:
#         brower = webdriver.Remote(command_executor='http://ytd-local.com:4444')
#         brower.get(link)
#         time.sleep(2)
#         try:
#             centerColWebElement = brower.find_element_by_css_selector('#centerCol')
#             productTitleWebElement = centerColWebElement.find_element_by_css_selector('#productTitle')
#             productInto['productName'] = productTitleWebElement.text
#         except:
#             print('产品名未取到')
#         try:
#             priceByClassNameWebElement = brower.find_elements_by_class_name('a-text-price')
#             for priceWebElement in  priceByClassNameWebElement:
#                 text = priceWebElement.text
#                 priceStr = text.replace('$','').replace('\n','.')
#                 productInto['price'] = priceStr
#                 if priceStr:
#                     break
#         except:
#             print('价格未取到')
#         try:
#             storeWebElement = brower.find_element_by_id('sellerProfileTriggerId')
#             productInto['store'] = storeWebElement.text
#         except:
#             print('店铺未取到')
#         try:
#             brandTableWebElement = brower.find_element_by_css_selector('#productOverview_feature_div')
#             tableRowWebElement = brandTableWebElement.find_element_by_class_name("po-brand")
#             tdWebElements = tableRowWebElement.find_elements_by_tag_name('td')
#             productInto['brand'] = tdWebElements[1].text
#         except:
#             print('品牌未取到')
#         try:
#             listingWebElement = centerColWebElement.find_element_by_css_selector('#feature-bullets')
#             productInto['listing'] = listingWebElement.text
#         except:
#             print('listing未取到')
#         try:
#             imagesWebElement = brower.find_element_by_css_selector('#imageBlock')
#             imagesWebElementElement = imagesWebElement.find_element_by_css_selector('#altImages')
#             imgWebElements = imagesWebElementElement.find_elements_by_tag_name('img')
#             imgs = []
#             for imgWebElement in imgWebElements:
#                 src = imgWebElement.get_attribute('src')
#                 if src.find('media'):
#                     imgs.append(src)
#             productInto['productImageLink'] = imgs
#         except:
#             print('产品图片未取到')
#         brower.quit()
#         return {
#             "success": True,
#             "data": productInto
#         }
#     except :
#         brower.quit()
#         return {
#             "success": False,
#             "data": '打开浏览器错误！'
#         }


