from scrapy import Request
from scrapy.spiders import Spider
from ..items import ChildItem
from ..items import ParentItem
import json
import re


headers = {
    "Authority": "www.shein.com.mx",
    "Method": "GET",
    "Path": "/Home-Appliances-c-3650.html?ici=mx_tab06navbar10&src_module=topcat&src_tab_page_id=page_home1684430081688&src_identifier=fc%3DHome%60sc%3DELECTRODOM%C3%89STICOS%60tc%3D0%60oc%3D0%60ps%3Dtab06navbar10%60jc%3Dreal_3650&srctype=category&userpath=category-ELECTRODOM%C3%89STICOS&page=2",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,es-MX;q=0.8,es;q=0.7",
    "Cache-Control": "max-age=0",
    "Cookie": "cookieId=70D27F86_7A56_6874_7D08_872E69E3AB0C; _pin_unauth=dWlkPVpHRTBOak16TXprdE1HUmhNUzAwT0RnMUxUazJZVE10Tm1Ga1pEY3lZamN6TnpBMA; _aimtellSubscriberID=b9339dcf-3dd4-ae57-c8f4-193123808c4b; sheindata2015jssdkcross=%7B%22distinct_id%22%3A%22185a1db0c3b1c3-0239bb4fdaeab82-26021151-2073600-185a1db0c3cf53%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22webpush%22%2C%22%24latest_utm_medium%22%3A%22aimtell%22%2C%22%24latest_utm_campaign%22%3A%22MXSALE230217%22%7D%2C%22%24device_id%22%3A%22185a1db0c3b1c3-0239bb4fdaeab82-26021151-2073600-185a1db0c3cf53%22%7D; language=es; _gcl_au=1.1.1302162384.1681238639; country=MX; countryId=137; ssrAbt=cotton_%23%23shipping_typeB%23%23SizeFbEn_type%3DA%23%23SellOutShow_type%3DB%23%23SellingPoint_type%3Dsellingpoint%23%23LocalReviews_type%3DB%23%23sheinclubprice_%23%23CccGoodsdetail_%23%23Fromproducttobody_rule%3D1727_1766_767%3AB%23%23Pricedifference_type%3DA%23%23GoodsdetailToppicOutfit_type%3DB%23%23DetailPageQuickShipShow_%23%23GoodsdetailToppicOutfitNewUser_type%3DA%23%23GoodsdetailToppicOutfitRecommend_is_pde%3D3%26rule_id_120%3Drec_ver%3AS120V3.0%26rule_id_121%3Drec_ver%3AS121M2.4%23%23DetailAddItemsForShipping_%23%23FlashShowedCrowed_Z%23%23UnderPrice_%23%23outlocalsize_newFlag%3A%7B%22range%22%3A%22detail%22%2C%22typel%22%3A%22B%22%7D%23%23ShippingLogisticsTime_newFlag%3A%7B%22LogisticsTime%22%3A%22A%22%7D%23%23SizeTips_newFlag%3A%7B%22SizeTips%22%3A%22B%22%7D%23%23Mall_2; sessionID_shein=s%3AUH5BiP_6r6Hx5wjLVp6vZJqlDTAoihHQ.z029xACr6wQONs11nTnlqSp%2FJ8Ou%2FG95K3E3f1Yf%2FFY; _gid=GA1.3.2039989559.1684174368; WEB_UGID_INIT=1; have_show=1; hideCoupon=1; hideCouponWithRequest=1; _abck=E2849FCF8DD07C43748C1CA720451616~0~YAAQBsX3vSkQog6IAQAAz1bELwlnBugHZvNSScj+ZNgss2HzPhCtiHzIxbBKdb9jfKUXA6DW7sfDnHMgcU3RJWJMg4L/utgD4ZfDuO3RCoxMu+AMPXY2G1npe5UGfOlsE7vB+LaplZK6lkoC5IwX1shkO+K8LJXdXFuSD5hVXZdeiBoaTn6j5WHnddoQ6LNWt5BP4JZzS+RMZ9/2gN4dvpN1n1GhysBe0jZaAB7KkVBVU6wLumX/d9ibgKlznP9a+LTPR6vQEKN56ru4FPCZElQzFR2A104cDBrN6c6sSNN4KUX9rJaGFH40MQbx1IAioZpi5L7zW+KMw0+82RN+/xdFXQwWV5Q0qurCDg18hXhfycArDgySJ2rk5OHnHuju9nTqjIZbkFSNtnpkMKq0Ft+tuo6WPq3YiIE=~-1~-1~-1; bm_sz=3E726993173FE508E808F40F084A0B86~YAAQBsX3vSwQog6IAQAA0FbELxNGBetNfVJ0MDGL6/9TFGipayLZvZ9X9DWJ5kfhpngDOn7fwkHx1xW97d7OZ/v+9Am+HhFYaoRl7K2LZLyR7yrlYb69EubhTPRiqwCJBCCarprjB78FicKnVJUiWoaHCAnhYx3RZhRclNaxGojlDRs0ciqajPvBw1EHvi/eaOEOpVsN56/cf2v73frcIv/JH80+PnU1o7KJb/B2qBThPBDLsRO/pW+1PfXpGHyYfzJJDXlDzyjIMTG4riLtHgUNJbE3uP2nB37rI9ETEtps7XUdtQ==~4604226~3619138; default_currency_expire=1; bm_mi=2EDC641314A3EA13DC5A983CD1485282~YAAQBsX3vRgRog6IAQAA7VzELxNmhQDoNtBQBCi2eblqnmlZ4vctybqz2otvfBcuDfXijFRDPoOIp7qwYC4ty9+U3EhddGHwLBoaEJ+UDzFh/g1wdqX4/SqCypZRR86YvB922D+RixLd9hx+xBl/G9aqAXrmNTRA+9TK2NdRewjXGznZXSeMkctqc4KCwas+PydMxhrXMISWQMAc4QLkn/j19D1LX43Lloxz+wdjB9j0rS0HTDRWxWSXqidJl5Q+ByU5SeJW+IQ/1FJU+pF8g3LPm53UrHDYBnbKwdhY7A8Bk0ZldmGmax8RFxVFT/dsPJ1Wp5EvjFqewb6Nc4POenYX~1; originOtherId=0; bi_session_id=bi_1684428577873_37880; ak_bmsc=F5FB02E1C8980D4F8208D50C30C51F09~000000000000000000000000000000~YAAQBsX3vfARog6IAQAArGLELxOFPmS6ta5QbtqZafavSYuvtBRBbV582lE8NNdeu1DKhs3TCPe8R/ZJ9RBYHahsvC7kFdMoJTm/ebdT/xO0f5SZdp8n13o/ADit4eQNtxaLJhOxkYxYMcL08k66IETxF7Jc8EsYUMen4bATdN9AUBrAo92X4XLOP4jaitJAQ+/0Sj/EBvZ9XgQwim06hGNuXwVOkuWaVc8vGHNXKC68FFRVQYFexxBg1RnvSbVJQCm6tA6lc5sRWXb7pcPnVf+8dX8M6GZnIUIEilwMCq0MDDEJFIUEtFOubcP/5YwuLaMC9hijCNFYDmqR1BbLY7rapve3MmQlvv2fU4ZFy9yRNR9hOzbXN9DfUfEPWTfK/f5iHpz0CuZXNCAaWp5MItWdJuS5ThPpYrOKqapXm4iQrd0KrArAZ1zu8ogsUYckfMl9rjle0+CQhx5DtYfX92XaTnk40ZUPwWOPVzQ0x2kmmuVSwPjhzQdhj3lGIH5K1O8tqzlCYWZQUhXLEztpn5LXa/XsyA==; scarab.visitor=%227B190054980D57F8%22; _csrf=Qqx6lrq9iWrIbMyZRsMHwNRN; ftr_blst_1h=1684428632564; __atuvc=3%7C16%2C3%7C17%2C9%7C18%2C0%7C19%2C16%7C20; REVIEW_LIKE_TIPS=1; cate_channel_type=5; forterToken=1fdbfa1b7cf242c58ae2e1a000eedd87_1684430169608__UDF43-m4_13ck; addressCookie=%7B%22countryId%22%3A%22137%22%2C%22createdTime%22%3A1684430332484%2C%22isUserHandle%22%3A%221%22%2C%22siteUid%22%3A%22mx%22%7D; cto_bundle=OERfGV94VDFCbXhHUmxXMlNRbzFZRWhSWWlxamRnNGs5eVFiTEhPY2o0VVFIcWtUa2lWMXg3OTBqN1FQdVBLanpocGV2bDhEMEZ5QnBHczMwaGowZ3MyWjlrR2FxTHNrMURnNXJ3ZkFLaDhMWHk3dWlRZFZ4M2p4ZTMwZlFBJTJGbWhxVW9tcUNZelN4R25QbWd4akIxcXlzOWg2ZyUzRCUzRA; _ga_SC3MXK8VH1=GS1.1.1684428580.46.1.1684430336.55.0.0; _ga=GA1.1.1066175333.1679441770; _uetsid=19f63720f34c11ed8015bb952c8b4d2a; _uetvid=29e5e5c0c84111edbdd0e5c4e0fd455e; _gat_shein=1; default_currency=MXN; bm_sv=85300926652C2AEDB6FBD00987726914~YAAQDMX3vXlO+yGIAQAAtyzvLxOJXNorhd0GwV8MNmt69buPilDlxWR61EhtWeSEaGJHfqSz5sRs3pIFoWi2/zJkgMqVk5CSFVI3lsjwYBuBUCOJxVeW/db4qmKGMhy0tfLnHhwScdYtPrRldkhUM4CS8AQ7oYpN0Y4l+bow3Zhm0AxnX70HjyCeiBStpyF4/b5r32KsbraQcGZzG5My46jr7rcH/mrnfGFmvG3iJ/Fqfva1S4mS7uNEYvR+sTkNh53+Rw==~1",
    "Referer": "https://www.shein.com.mx",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}


class SheinSpider(Spider):
    name = 'sheindange'
    #url = "https://www.shein.com.mx"
    url = "https://www.shein.com.mx"
    def start_requests(self):
        
        yield Request(self.url,headers=headers,callback=self.parse_category)



    def parse_category(self,response):

        script = response.xpath("//script[contains(., 'window.gbCccHomeData')]/text()").get()
        json_str = re.search(r'window.gbCccHomeData\s*=\s*(\{.*\})', script).group(1)
        json_data = json.loads(json_str)
        content_data = json_data.get('content')
        # 如果 "content" 存在并且 "cateLinks" 存在，打印 "cateLinks"
        if content_data:
            cate_links = content_data.get('cateLinks')
            if cate_links:
                #print(cate_links)
                for key,value in cate_links.items():
                    #url = str(self.url) + str(value)
                    #print(url)
                        #https://www.shein.com.mx/Home-Decor-c-1954.html
                        #https://www.shein.com.mx/style/Women-Clothing-sc-001121425.html
                        #https://www.shein.com.mx/ListJsonService?_ver=1.1.8&_lang=es&type=entity&routeId=1954&page=1
                        #https://www.shein.com.mx/ListJsonService?_ver=1.1.8&_lang=es&type=selection&routeId=1864&page=2
                    url = "https://www.shein.com.mx/recommend/Beauty-Health-sc-100142086.html"

                    yield Request(url,cookies={
                "cookieId": "70D27F86_7A56_6874_7D08_872E69E3AB0C",
                "_pin_unauth": "dWlkPVpHRTBOak16TXprdE1HUmhNUzAwT0RnMUxUazJZVE10Tm1Ga1pEY3lZamN6TnpBMA",
                "_aimtellSubscriberID": "b9339dcf-3dd4-ae57-c8f4-193123808c4b",
                # 其他的cookie键值对
                # "cookie_name": "cookie_value",
            },callback=self.childcategory)
    

    def childcategory(self,response):
        # 假设response是包含页面内容的Response对象
        routerid  =re.search(r'\d+',response.url).group()



        # 使用XPath定位到包含gbProductListSsrData的script标签
        script_xpath = "//script[contains(., 'var gbProductListSsrData =')]/text()"
        script_content = response.xpath(script_xpath).get()

        # 提取gbProductListSsrData的内容
        start_index = script_content.index('{')
        end_index = script_content.rindex('}') + 1
        gbProductListSsrData_json = script_content[start_index:end_index]

        # 解析json数据
        gbProductListSsrData = json.loads(gbProductListSsrData_json)
        category_parent =  gbProductListSsrData['results']['filterCates']
        #获取父类的json数据并且解析
        for category_child in category_parent['children']:
            item = ParentItem()
            item['catid'] = category_child['cat_id']
            item['display_name'] = category_child['cat_name']
            print("1111111111111111111")
            print(item['catid'])
            print(item['display_name'])
            #获取子类的json数据并且解析
            for category_child in category_child['children']:
               

                item['second_cage_catid']=category_child['cat_id']
                item['second_cage_display_name'] = category_child['cat_name']
                print("22222222")
                print(item['second_cage_catid'])
                print(item['second_cage_display_name'])    
                #获取二级子类的json数据判断是否存在children三级子类，如果有那么继续解析，否则返回yield 通过ListJsonService获取goodid的json数据生成product的url开始进行产品页面的分析
                current_page = 1  # 设置当前页，起始为1
                if "children" in category_child:
                    for category_child in category_child['children']:
                        item['second_cage_catid']=category_child['cat_id']
                        item['second_cage_display_name'] = category_child['cat_name']
                        print("33333333")
                        print(item['second_cage_catid'])
                        print(item['second_cage_display_name'])
                        total_page = gbProductListSsrData['results']['sumForPage']/120
                        while current_page < total_page:
                            current_page += 1
                            #url = str(self.url) + "/ListJsonService?_ver=1.1.8&_lang=es&type=selection&routeId=" + str(routerid) + "page=" + str(current_page) + "&child_cat_id=" + str(item['second_cage_catid'])
                            url = str(response.url) + "?child_cat_id=" + str(item['second_cage_catid']) + "&page=" + str(current_page)
                            yield Request(url,cookies={
                "cookieId": "70D27F86_7A56_6874_7D08_872E69E3AB0C",
                "_pin_unauth": "dWlkPVpHRTBOak16TXprdE1HUmhNUzAwT0RnMUxUazJZVE10Tm1Ga1pEY3lZamN6TnpBMA",
                "_aimtellSubscriberID": "b9339dcf-3dd4-ae57-c8f4-193123808c4b",
                # 其他的cookie键值对
                # "cookie_name": "cookie_value",
            },callback=self.getjson,meta={'item': item})
                else:
                    #https://www.shein.com.mx/ListJsonService?_ver=1.1.8&_lang=es&type=selection&routeId=100142086&page=1&child_cat_id=2265
                    total_page = gbProductListSsrData['results']['sumForPage']/120
                    while current_page < total_page:
                        current_page += 1
                        #url = str(self.url) + "/ListJsonService?_ver=1.1.8&_lang=es&type=selection&routeId=" + str(routerid) + "page=" + str(current_page) + "&child_cat_id=" + str(item['second_cage_catid'])
                        url = str(response.url) + "?child_cat_id=" + str(item['second_cage_catid']) + "&page=" + str(current_page)
                        yield Request(url,cookies={
                "cookieId": "70D27F86_7A56_6874_7D08_872E69E3AB0C",
                "_pin_unauth": "dWlkPVpHRTBOak16TXprdE1HUmhNUzAwT0RnMUxUazJZVE10Tm1Ga1pEY3lZamN6TnpBMA",
                "_aimtellSubscriberID": "b9339dcf-3dd4-ae57-c8f4-193123808c4b",
                # 其他的cookie键值对
                # "cookie_name": "cookie_value",
            },callback=self.getjson,meta={'item': item})
                        
    def getjson(self,response):
        script = response.xpath('//script[contains(., "var gbProductListSsrData")]/text()').get()
        m = re.search('var gbProductListSsrData = ({.*})', script, re.DOTALL)      
        if m:
            json_str = m.group(1)
            product_list = json.loads(json_str)['results']['goods']
            # with open('secendchildcategory.json', 'w') as f:
            #     json.dump(product_list, f)
            # 现在你可以处理data字典了数据格式为secendchildcategory.json
            #product_list = data()['results']['goods']
            for product in product_list:
                item = ChildItem()
                item ['category'] = product['cat_id']
                item ['id'] = product['goods_id']
                url = f"https://www.shein.com.mx/{product['goods_url_name'].replace(' ', '-')}-p-{product['goods_id']}-cat-{product['cat_id']}.html"  
                yield Request(url,callback=self.parse_product)

        else:
            print("子类页面不存在")


    def parse_product(self,response):
        scripts = response.xpath('//script/text()').getall()
        for script in scripts:
  
            match = re.search('window.goodsDetailV3SsrData\s*=\s*(\{.*?"URL_PATH".*?\})', script, re.DOTALL)
            
            if match:
                try:
                    data = json.loads(match.group(1))
                    producto = data['productIntroData']
                    # with open('goodsDetailV3SsrData.json', 'w') as f:
                    #     json.dump(data, f)
                    item = ChildItem()
                    item['id'] = producto['detail']['goods_id']
                    item['url'] = "https://www.shein.com.mx" + str(data['URL_PATH'])
                    item['price'] = producto['detail']['salePrice']['amount']
                    item['image'] = producto['detail']['original_img']
                    item['title'] = producto['detail']['goods_url_name']
                    if producto['commentInfo']:
                        item['like_count'] = producto['commentInfo']['comment_num_str']
                    else:
                        item['like_count'] = 'NULL'
                    item['category'] = producto['currentCat']['cat_name']
                    #父类item['parent_category'] = producto['parentCats']['cat_name']
                    item['tablename'] = 'mexico'
                    yield item

                except json.JSONDecodeError as e:
                    print("解析 JSON 字符串时发生错误:", e)


            




        


