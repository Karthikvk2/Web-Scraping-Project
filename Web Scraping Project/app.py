import requests
from  bs4 import  BeautifulSoup

products_to_track = [
    {
        "product_url":"https://www.amazon.in/gp/aw/d/B0CHX7V9TY/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=5bc1a1e28680e3e55bb6326fc5b8503a&hsa_cr_id=0&qid=1721239253&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_mcd_asin_0_img&pd_rd_w=JJFDw&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_p=df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_r=ER7JKPK6CD1QK7RN75TS&pd_rd_wg=x6IMp&pd_rd_r=3821ec26-9c7b-4a21-9849-e8871b5d137b",
        "name":"iphone 15 pro",
        "target_price": 120000
    },
    {
        "product_url":"https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN/ref=sr_1_1_sspa?crid=3J5FS290ZRHWY&dib=eyJ2IjoiMSJ9.jM0UAYMi7q1fek-SAA4DuzW3Dj-oHo_jABdcLIpErVXorvB92Z8Nx1ckmaFd26qe_grgq8wZqOGUD8WGrFsQhdrEJxDn3PlrTbp8fcZIEE2QkFOZE_eNXkKsAj9oxhO7iYJpfeJ5RZr1DQeXAcBNa4lDKr9boStKY_nysm8v43vKnBDZcCFwtvTbuxk1LWpjw24cS4kULxgE4vjsLLXmzywBW8fznjAQCFTSziJp59d4dVSJ_ffuj9lhCXWqAZ4ixxgavMCBqmiWnY0E7p1eUr7mEYYcpmlpPoaaeu1K1UQ.JE58InGwzzFWPocZdxMr-haa4a6Ql37MaavjKR8bi2o&dib_tag=se&keywords=samsung&qid=1721242248&s=electronics&sprefix=samsung%2Celectronics%2C238&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1",
        "name":"Samsung s24 Ultra",
        "target_price": 120000
    },
    {
        "product_url":"https://www.amazon.in/Redmi-Note-Iceberg-256GB-Storage/dp/B0BRVJ54ZP/ref=sr_1_2_sspa?crid=3J5FS290ZRHWY&dib=eyJ2IjoiMSJ9.jM0UAYMi7q1fek-SAA4DuzW3Dj-oHo_jABdcLIpErVXorvB92Z8Nx1ckmaFd26qe_grgq8wZqOGUD8WGrFsQhdrEJxDn3PlrTbp8fcZIEE2QkFOZE_eNXkKsAj9oxhO7iYJpfeJ5RZr1DQeXAcBNa4lDKr9boStKY_nysm8v43vKnBDZcCFwtvTbuxk1LWpjw24cS4kULxgE4vjsLLXmzywBW8fznjAQCFTSziJp59d4dVSJ_ffuj9lhCXWqAZ4ixxgavMCBqmiWnY0E7p1eUr7mEYYcpmlpPoaaeu1K1UQ.JE58InGwzzFWPocZdxMr-haa4a6Ql37MaavjKR8bi2o&dib_tag=se&keywords=samsung&qid=1721242248&s=electronics&sprefix=samsung%2Celectronics%2C238&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "name":"Redmi Note 12 pro",
        "target_price": 27000
    },
    {
        "product_url":"https://www.amazon.in/SAMSUNG-Galaxy-S23-Mint-Storage/dp/B0CJXPYJC3/ref=sr_1_11?crid=3J5FS290ZRHWY&dib=eyJ2IjoiMSJ9.jM0UAYMi7q1fek-SAA4DuzW3Dj-oHo_jABdcLIpErVXorvB92Z8Nx1ckmaFd26qe_grgq8wZqOGUD8WGrFsQhdrEJxDn3PlrTbp8fcZIEE2QkFOZE_eNXkKsAj9oxhO7iYJpfeJ5RZr1DQeXAcBNa4lDKr9boStKY_nysm8v43vKnBDZcCFwtvTbuxk1LWpjw24cS4kULxgE4vjsLLXmzywBW8fznjAQCFTSziJp59d4dVSJ_ffuj9lhCXWqAZ4ixxgavMCBqmiWnY0E7p1eUr7mEYYcpmlpPoaaeu1K1UQ.JE58InGwzzFWPocZdxMr-haa4a6Ql37MaavjKR8bi2o&dib_tag=se&keywords=samsung&qid=1721242248&s=electronics&sprefix=samsung%2Celectronics%2C238&sr=1-11",
        "name":"Samsung s23 FE",
        "target_price": 38000
    },
    {
        "product_url":"https://www.amazon.in/OnePlus-Iron-Gray-128GB-Storage/dp/B0CQYMMP94/ref=sr_1_4?crid=2BP4WT9CLWN8O&dib=eyJ2IjoiMSJ9.Hw9fBNe8oMIfK0XIQncnxHiXCYmuF96RG30uAgerSkVE739HqD7uIyfP9Gj-oat9uigZ6MUkizSgGsyHfTkGG17APacTVfkKLWlOAPPaVwLUjW-dkA1C-CADK-c7w3KjWLwu-hqAaj57i5KSzzH3Y-lt5Pd7rBh2ulwGiKEsLlv1lC4yhNf2k0WCKVqRuup37rb53iqy84iyC-sbPK5FLfB47CW1tOYVm0guSfxKaPQ.ryeohO-batAWpxiUWicN2thNMS2G9I52bBOW7apFw_s&dib_tag=se&keywords=oneplus+11r&qid=1721245862&sprefix=oneplus%2Caps%2C246&sr=8-4",
        "name":"Oneplus 12R",
        "target_price": 38000
    },
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(class_="a-price-whole")
    if (product_price == None):
        product_price = soup.find(class_="priceblock_ourprice")
    return product_price.getText()

result_file = open('my_result_file.txt','w')
try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " " + every_product.get("name"))

        my_product_price = product_price_returned[0:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + '-\t' + 'Available at target price ' + ' current price - ' + str(my_product_price)+'\n')
        else:
            print("Still At current price")

finally:
    result_file.close()



