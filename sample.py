from web_ace_downloader.web_ace_downloader import web_ace_downloader

url = "https://web-ace.jp/youngaceup/contents/1000069/episode/1228/"


while url:
    jpd = web_ace_downloader(dir="./")
    jpd.auto_list_download(url=url, sleeptime=0, pdfConversion=True)