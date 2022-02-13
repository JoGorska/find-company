# Company list
## 1. Data from Cylex
Inspected source code on Cylex website. There are two possible places to get company name from:
- url, where company details are:
```
https://birmingham.cylex-uk.co.uk/company/birchfield-cleaning-centre-14236240.html
```
- company name:
slug-like name between the word '/company/' and a 8 digit number. This would require cleaning up to get rid of the '-'
```
<meta itemprop="url" content="https://sinfin.cylex-uk.co.uk/company/blue-elephant-19890236.html"
```
second source of company name - this would give me a clean name with spaces

```
<meta property="og:title" content="Jay C Security Ltd" />
```
third source of company name - clean again, but unsure if all companies will have twitter account
```
<meta name="twitter:title" content="Valerie Ann Newton" 
```
## 2. Error 403 from Cylex

After several attempts I was unable to get company list from cylex. When I run spider I am getting 403 error. For more details check cylex-spider branch.
![error 403](find_company/static/01-error-403.PNG)
 Tried to resolve (and failed):
- uncommented 'USER_AGENT' in settings to see if it works, it didn't
- add a random user-agent found as a solution to this error on stack overflow
- commented out crawl spider and add scrapy spider and have it investigate one page, where I know where company details are
- investigated with chrome dev tools what user agent cylex accept. found this one in Request Headers section:
```
Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36
```
- changed spider completly to wikipedia - to check if spider can get into any other website - the wikipedia didn't return 403 error
- installed library 'scrapy-user-agents==0.1.1' to have user agents randomly changed and add to settings:
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
```
- add 'DOWNLOAD_DELAY = 5' in attempt to imitate human behaviour more
- add headers to spider:
```
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36',
    #     'cookie': 'your cookie',
    # }
    # response = requests.get('https://corby.cylex-uk.co.uk/company/alexs-15659626.html', headers=headers)
```
- and different version to add headers to spider request:
```
    # req = Request('https://corby.cylex-uk.co.uk/company/alexs-15659626.html', headers={'User-Agent': 'Mozilla/5.0'})
    # response = urlopen(req).read()
```
- changed settings 'ROBOTSTXT_OBEY' to False, to test if this was blocking, although the robots.txt file didn't indicate any potential problems, solution didn't work anyway, changed back to True
- set various different settings with cookies:
```
COOKIES_ENABLED = True
COOKIES_DEBUG = True
```

- further area to investigate Proxies
- further to investigate for crawl spider - sometimes when you click onto the company details you get advert pop up, which needs to be closed, before accessing the page

## 3. Yell as alternative to Cylex

Attempt to reaserch another popular website that would give me a lots of record of companies - Found Yell
### Example data:
- example of company that has profile on both trustpilot and Yell: 

Corby Tyre and Exhaust- Yell link [here](https://www.yell.com/biz/corby-tyre-and-exhaust-corby-6915600/)
Corbytyre - Trustpilot link [here](https://uk.trustpilot.com/review/www.corbytyres.co.uk)

#### Issues:
- the names are different - corby tyre and exhaust on Yell, but corbytyres on trustpilot - this might be due this one being unclaimed profile at trustpilot
- common ground: they both reffer to the same website of the company link [here](www.corbytyres.co.uk)
- need to be aware that not all companies will have website on both sites
- I tested that trustpilot allows to reaserch by company name OR partial of the website address. It is worth to harvest both data from Yell to get more hits in Trustpilot

#### Source of data in Yell:
- exact url where data is:
```
https://www.yell.com/biz/corby-tyre-and-exhaust-corby-6915600/
```

- company name
```
<h1 itemprop="name" class="text-h1 businessCard--businessName" >Corby Tyre and Exhaust</h1>
```

- company website link, this will require cleaning to get just the domain 'corbytyres':
```
<a itemprop="url" rel="nofollow noopener" href="http://www.corbytyres.co.uk" data-tracking="AP:CN:WL:FLE" target="_blank" class="btn btn-big btn-yellow businessCard--callToAction" >
```
