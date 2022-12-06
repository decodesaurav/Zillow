from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL='https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.55541331640626%2C%22east%22%3A-80.13243968359376%2C%22south%22%3A25.539568676836492%2C%22north%22%3A25.866244471247178%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=4'

def cookie_parser():
   cookie_string = 'zguid=24|%2463b1c644-cf2b-4fca-bedf-48f55a9fc525; _ga=GA1.2.502483070.1669352892; zjs_user_id=null; zg_anonymous_id=%22c32c50f6-2bed-49ed-9972-88d4935c9977%22; zjs_anonymous_id=%2263b1c644-cf2b-4fca-bedf-48f55a9fc525%22; _pxvid=2d20c7d7-6c7f-11ed-963d-69544a634652; _gcl_au=1.1.988528589.1669354244; __gads=ID=e0ad0868fb3bdfcd:T=1669354242:S=ALNI_MZ6vnyISZJ_v-V3McthJlTGOryy8g; __pdst=b6fb72aeb18c460da816fb5bfc4b1a52; _fbp=fb.1.1669354245733.887651527; _pin_unauth=dWlkPU5HTmtOR015TVdJdFpUTm1ZaTAwWkdZMkxUbGlZemN0WW1abU9URmlZbVF3Wm1aaQ; _cs_c=0; zgsession=1|04b46e16-9f97-42de-859d-f30d07fb08cd; _gid=GA1.2.236191634.1670141428; KruxPixel=true; DoubleClickSession=true; pxcts=1de21048-73ab-11ed-b5d0-524f684e7065; KruxAddition=true; g_state={"i_p":1670317985761,"i_l":2}; _clck=1cav66b|1|f76|0; _hp2_id.1215457233=%7B%22userId%22%3A%223816144571865251%22%2C%22pageviewId%22%3A%222495080456921203%22%2C%22sessionId%22%3A%221860381498151812%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.1215457233=%7B%22ts%22%3A1670290212996%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _cs_id=8f1dbc89-2e87-ac44-d3a3-10b87bbb7c29.1669877619.7.1670290221.1670290221.1.1704041619080; _cs_s=1.5.0.1670292023505; utag_main=v_id:0184ad444f5500570c821bae90500506f001d0670086e$_sn:5$_se:1$_ss:1$_st:1670292012157$dc_visit:4$ses_id:1670290212157%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:ap-east-1%3Bexp-session$ttd_uuid:e4282f4b-0be3-4bd2-af32-6441b3b8f712%3Bexp-session; JSESSIONID=21E13526A27ECCBD6AE43BC7BF23D972; _px3=b65d5b5b576e71656d8ac11d9c90b26b826c22d2aed22ef8ee595bde63dfedfd:lsMZAWyTh9TUz18jh/eVmaMYQNEgvE+52H2OCrXpvgah2oF7UFJSUlVtW89KkwYWI72dAi1XuHqMVBRFBRZXlA==:1000:WxUB0tHbaemVlonxx77T5POrrP6i4BCNzf2BiwR/K/AASCh3AqmEV1+xxMTFIN72lJyAJ5zGP6+bDBECK3PxogePmc4qsTfnHqapwoYNa7Gsob2qFdbGMAjpOw7RTXyGyG7/NEXp8HxBsTM9dMviInIx7emimXS1iEWYtSrBG26mWBfObFhxEpSZwJt/U91ptbggl+9BbPJaSuNiqSJPxA==; _uetsid=227f99c073ab11eda32fd36f0b21d7b9; _uetvid=4f91d5006c8211edbad8338656bd000c; __gpi=UID=00000b832d8d2666:T=1669354242:RT=1670290418:S=ALNI_Ma07YTTF79qaImqDUWNHs7PT-Cxog; _derived_epik=dj0yJnU9Qzc1N21HenJwaTFUWEE4X2xfQW03SnczS1pCM1VCSUombj03WmpNWlA3OEk4YVNKOF8xbkVlNXNRJm09ZiZ0PUFBQUFBR09PbV9NJnJtPWYmcnQ9QUFBQUFHT09tX00mc3A9Mg; AWSALB=GLE9KMlR0su4Ez/ZY9jIk+bssW8YllM8C0n1VfT5pmdIL9XuDe86zklSc4MvMbilG4e1l/V6+V4hIkk30/v+m6IVghs0zx6LioWPTvYmO949RjJvS/NGgEqBBFim; AWSALBCORS=GLE9KMlR0su4Ez/ZY9jIk+bssW8YllM8C0n1VfT5pmdIL9XuDe86zklSc4MvMbilG4e1l/V6+V4hIkk30/v+m6IVghs0zx6LioWPTvYmO949RjJvS/NGgEqBBFim; search=6|1672882442513%7Crect%3D25.866244471247178%252C-80.13243968359376%252C25.539568676836492%252C-80.55541331640626%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0912700%09%09%09%09%09%09; _clsk=1bg7kup|1670290479834|2|0|l.clarity.ms/collect; _gat=1'
   cookie = SimpleCookie() #instance of SimpleCookie
   cookie.load(cookie_string)

   cookies = {}

   for key, morsel in cookie.items():
      cookies[key] = morsel.value
    
   return cookies

def parse_new_url(url, next_page_number):
   url_parsed = urlparse(url)
   query_string = parse_qs(url_parsed.query)
   search_query_state = json.loads(query_string.get('searchQueryState')[0])
   search_query_state['pagination'] = {"currentPage": next_page_number}
   query_string.get('searchQueryState')[0] = search_query_state
   encoded_query_string = urlencode(query_string, doseq=1)

   new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_query_string}"

   return new_url

