import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
# url = "https://kanmeitu1.cc/p/59348.html"
# res = requests.get(url,headers=headers)
# html = res.text
# urls = re.findall(r'src="https.+?.jpg"',html)
# print(urls)
urls = ['src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004p3vz2vzlgdp.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004gmkss2k55tq.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004wu0efqd4oft.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vmdlmlx42sc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120041wcuij0f2cc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004xv1wu5yotck.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120042c5m40xx5lc.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120040ebtfs25uu2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004rm5ii5k1kau.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004ffbatkumiyg.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004nb21jbfeinn.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vazuipmv33l.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004d2isi1b0hlb.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004sa325bwgyrt.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004vlygenblp4d.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004nw33grb0ixa.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004hcisxiqdq5y.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004dggy254lsa5.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004oyvkiotrhe2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004golj0oaaia2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004pkvhq32i3fa.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120045alsy2wc3m2.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004qgqhn2webof.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/20221120043qv2ws1ov3p.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004eoiyd5twbeg.jpg"', 'src="https://kanmeitu.ojbkcdn.com/t32/2022112004/2022112004wibwcdp4umy.jpg"']
for url in urls:
     # s = url.split("\"")
    s = url[url.index("\"")+1:-1]
    print(s)