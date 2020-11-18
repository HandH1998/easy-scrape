import multiprocessing as mp
import time

import aiohttp
from bs4 import BeautifulSoup
import re
import requests
import asyncio


# 定义爬取url功能
async def crawl(url, session):
    try:
        r = await session.get(url)
        html = await r.text()
        await asyncio.sleep(0.1)
        return html
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


async def main(loop):
    pool = mp.Pool(4)
    unseen = set([base_url])
    seen = set()
    count=1
    async with aiohttp.ClientSession() as session:
        while (count <= 100):
            # 使用异步爬取unseen集合中url对应的html
            # 因为正常下载网页，需要有等待时间，异步可以充分利用这个等待时间来做事
            # 所以虽然是单线程，但是也可以加快速度
            print('crawl url...')
            tasks = [loop.create_task(crawl(i, session)) for i in unseen]
            finished, unfinished = await asyncio.wait(tasks)
            htmls = [f.result() for f in finished]
            htmls = [html for html in htmls if html is not None]

            # 使用多进程解析html文档，爬取需要的title、url
            # 因为解析文档等待时间很少，所以用多进程更快
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


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print('total time:', time.time() - t1)
