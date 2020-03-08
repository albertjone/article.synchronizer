import requests

headers = {
    'authority': 'www.dawncreat.com',
    'accept': '*/*',
    'origin': 'https://www.dawncreat.com',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.dawncreat.com/admin-index.do',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cookie': '__cfduid=da34f2d1eb6da5546c4b5f2bbde009e5b1573807787; __cfduid=da34f2d1eb6da5546c4b5f2bbde009e5b1573807787; LATKE_SESSION_ID=UHQi8UCJ2TMquZ5Q; skin=Pinghsu; visited=%5B%22%2F%22%2C%22%2Fhello-solo%22%2C%22%2Ftags.html%22%5D; solo=840f4b29da8635aaf8dab7f44e19c40fd9751771ed3568a71489ddfe0ee928dca80e12abab93ab7c8f8708935317c1410d2e0a870bca5b445ba6502a99d4091c',
}

data = '{
    "article": {
        "articleTitle": "test\u6807\u9898",
        "articleContent": "test\u6B63\u6587\\n",
        "articleAbstract": "test\u6458\u8981\\n",
        "articleTags": "test\u6807\u7B7E",
        "articlePermalink": "",
        "articleStatus": 0,
        "articleSignId": "1",
        "postToCommunity": false,
        "articleCommentable": true,
        "articleViewPwd": ""
    }
}'

response = requests.post('https://www.dawncreat.com/console/article/', headers=headers, data=data)
