import multiprocessing as mp
import time
from bs4 import BeautifulSoup
import re
import requests


# 定义爬取url功能
def crawl(url):
    try:
        return requests.get(url).text
    except Exception as e:
        print(e)
        print('error:', url)


# 定义解析html功能
def parse(html):
    soup = BeautifulSoup(html, features='lxml')
    urls = soup.find_all('a', {'href': re.compile(r'^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    url = soup.find('meta', {'property': "og:url"}).get('content')
    page_urls = set([base_url + url.get('href') for url in urls])
    return title, url, page_urls

base_url = 'https://mofanpy.com'
if __name__ == '__main__':
    unseen = set([base_url])
    seen = set()
    count, t1 = 1, time.time()

    pool = mp.Pool(4)
    while (count <= 100):
        # 使用多进程爬取unseen集合中url对应的html...
        print('crawl url...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [i.get() for i in crawl_jobs]
        htmls = [html for html in htmls if html is not None]
        # 使用多进程解析html文档，爬取需要的title、url
        print('parse html...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [i.get() for i in parse_jobs]
        # 更新已经爬取过的url集合seen，同时清空未爬取的url集合unseen
        seen.update(unseen)
        unseen.clear()
        # 打印信息，同时更新unseen
        for title, url, page_urls in results:
            print(count, ' title:', title, ' url:', url)
            count += 1
            # 需要和seen中的url比较，避免重复爬取
            unseen.update(page_urls - seen)
        # for i in seen:
        #     print('seen:', i)
        # print()
        # for i in unseen:
        #     print('unseen:', i)

    print('total time:', time.time() - t1)
