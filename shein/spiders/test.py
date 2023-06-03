import scrapy
from scrapy.http import Headers

class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = ["http://httpbin.org/get"]

    def start_requests(self):
        headers = {
            "Authority": "www.shein.com.mx",
            "Method": "GET",
            "Path": "/Home-Appliances-c-3650.html?ici=mx_tab06navbar10&src_module=topcat&src_tab_page_id=page_home1684430081688&src_identifier=fc%3DHome%60sc%3DELECTRODOM%C3%89STICOS%60tc%3D0%60oc%3D0%60ps%3Dtab06navbar10%60jc%3Dreal_3650&srctype=category&userpath=category-ELECTRODOM%C3%89STICOS&page=2",
            "Scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,es-MX;q=0.8,es;q=0.7",
            "Cache-Control": "max-age=0",
            "Referer": "https://www.shein.com.mx/home?ici=mx_tab06",
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
        cookies = {
            "cookieId": "70D27F86_7A56_6874_7D08_872E69E3AB0C",
            "_pin_unauth": "dWlkPVpHRTBOak16TXprdE1HUmhNUzAwT0RnMUxUazJZVE10Tm1Ga1pEY3lZamN6TnpBMA",
            "_aimtellSubscriberID": "b9339dcf-3dd4-ae57-c8f4-193123808c4b",
            "sheindata2015jssdkcross": "%7B%22distinct_id%22%3A%22185a1db0c3b1c3-0239bb4fdaeab82-26021151-2073600-185a1db0c3cf53%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22webpush%22%2C%22%24latest_utm_medium%22%3A%22aimtell%22%2C%22%24latest_utm_campaign%22%3A%22MXSALE230217%22%7D%2C%22%24device_id%22%3A%22185a1db0c3b1c3-0239bb4fdaeab82-26021151-2073600-185a1db0c3cf53%22%7D",
            "language": "es",
            "_gcl_au": "1.1.1302162384.1681238639",
            "country": "MX",
            "countryId": "137",
            "ssrAbt": "cotton_%23%23shipping_typeB%23%23SizeFbEn_type%3DA%23%23SellOutShow_type%3DB%23%23SellingPoint_type%3Dsellingpoint%23%23LocalReviews_type%3DB%23%23sheinclubprice_%23%23CccGoodsdetail_%23%23Fromproducttobody_rule%3D1727_1766_767%3AB%23%23Pricedifference_type%3DA%23%23GoodsdetailToppicOutfit_type%3DB%23%23DetailPageQuickShipShow_%23%23GoodsdetailToppicOutfitNewUser_type%3DA%23%23GoodsdetailToppicOutfitRecommend_is_pde%3D3%26rule_id_120%3Drec_ver%3AS120V3.0%26rule_id_121%3Drec_ver%3AS121M2.4%23%23DetailAddItemsForShipping_%23%23FlashShowedCrowed_Z%23%23UnderPrice_%23%23outlocalsize_newFlag%3A%7B%22range%22%3A%22detail%22%2C%22typel%22%3A%22B%22%7D%23%23ShippingLogisticsTime_newFlag%3A%7B%22LogisticsTime%22%3A%22A%22%7D%23%23SizeTips_newFlag%3A%7B%22SizeTips%22%3A%22B%22%7D%23%23Mall_2",
            "sessionID_shein": "s%3AUH5BiP_6r6Hx5wjLVp6vZJqlDTAoihHQ.z029xACr6wQONs11nTnlqSp%2FJ8Ou%2FG95K3E3f1Yf%2FFY",
            "_gid": "GA1.3.2039989559.1684174368",
            "_abck": "E2849FCF8DD07C43748C1CA720451616~0~YAAQBsX3vSkQog6IAQAAz1bELwlnBugHZvNSScj+ZNgss2HzPhCtiHzIxbBKdb9jfKUXA6DW7sfDnHMgcU3RJWJMg4L/utgD4ZfDuO3RCoxMu+AMPXY2G1npe5UGfOlsE7vB+LaplZK6lkoC5IwX1shkO+K8LJXdXFuSD5hVXZdeiBoaTn6j5WHnddoQ6LNWt5BP4JZzS+RMZ9/2gN4dvpN1n1GhysBe0jZaAB7KkVBVU6wLumX/d9ibgKlznP9a+LTPR6vQEKN56ru4FPCZElQzFR2A104cDBrN6c6sSNN4KUX9rJaGFH40MQbx1IAioZpi5L7zW+KMw0+82RN+/xdFXQwWV5Q0qurCDg18hXhfycArDgySJ2rk5OHnHuju9nTqjIZbkFSNtnpkMKq0Ft+tuo6WPq3YiIE=~-1~-1~-1",
            "bm_sz": "3E726993173FE508E808F40F084A0B86~YAAQBsX3vSwQog6IAQAA0FbELxNGBetNfVJ0MDGL6/9TFGipayLZvZ9X9DWJ5kfhpngDOn7fwkHx1xW97d7OZ/v+9Am+HhFYaoRl7K2LZLyR7yrlYb69EubhTPRiqwCJBCCarprjB78FicKnVJUiWoaHCAnhYx3RZhRclNaxGojlDRs0ciqajPvBw1EHvi/eaOEOpVsN56/cf2v73frcIv/JH80+PnU1o7KJb/B2qBThPBDLsRO/pW+1PfXpGHyYfzJJDXlDzyjIMTG4riLtHgUNJbE3uP2nB37rI9ETEtps7XUdtQ==~4604226~3619138",
            "_ga_SC3MXK8VH1": "GS1.1.1684428580.46.1.1684432284.55.0.0",
            "_ga": "GA1.1.1066175333.1679441770",
            "_uetsid": "19f63720f34c11ed8015bb952c8b4d2a",
            "_uetvid": "29e5e5c0c84111edbdd0e5c4e0fd455e",
            "ak_bmsc": "CE07524AB71852BF4918E04B67DE0FEE~000000000000000000000000000000~YAAQDMX3vVrPByKIAQAAlLU2MBO3i1byanXTph8uYECoRqWznAVn4CZoyKQsoIvzogUZK+5BtXkcyNJZObcuUPMkiDBdkSRpNNklKNpBFD52ZwsAXVKr18rBuMKlz/uP4k8P5dxyBVMe67Rw1QgRA6+FgRSubQ+JdSgPumfMkt7+uKi+fC4FWYZpJLWQf/H74gojkwlGuhv328Rc2RrcthdguA8PQDE7yaE7cG/CvrPGflqAiC0JUBbssC2pw3nd35njiH5YQ+1yhYvOrpVMnGwckO7h6gcNsCZNLQuYUhdfdNNvFG49p2is1taAWUB1vKxaq19uFlxfveDDSezsPmsv4ssQXabViU0e1pPQ7SAxYVjmOApGRXMsUPUuJHorIOlRP+r//Be+QoJmvQ==",
            "default_currency": "MXN",
            "bm_sv": "50B6B249C0C2DF4332828255CE5FDC08~YAAQDMX3vU0EFSKIAQAA8wCBMBPC3OdzLfGMvoDOkTDp1L0bZJ2ov6qNcOZaxnNjkpUGnl03TVtCN6VNzupg4nt9RAFDqk8feuMMiI7+gn949RwoSakvtH7MhCepEXb/MIXKW8nPFfy3QCe/EbmiRqutfMkcxbKLChW9VksXYuO1WzX+n4PJtkqIUtm8kznms4U4OD8xZfFIHKM+ZGhslldmIyzw94loGoMXsAV35KkYyNWg8ZIZ35CtsZ/35/BmlRc=~1",
            "bi_session_id": "bi_1684441477556_89164"
        }
        headers_with_cookie = Headers(headers)
        headers_with_cookie.update(cookies)

        yield scrapy.Request(self.start_urls[0], headers=headers_with_cookie, callback=self.parse)

    def parse(self, response):
        headers = response.request.headers
        print(headers)