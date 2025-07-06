import requests
import json
from urllib.parse import urljoin
# proxies={'http': 'http://{}'.format('8.129.28.247:8888'),
#         'https': 'https://{}'.format('8.129.28.247:8888')}
BASE_URL = "http://www.xinfadi.com.cn"  # 替换为实际网站URL
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'

}


def get_price_data(page=1, limit=10):
    url = urljoin(BASE_URL, "/getPriceData.html")
    data = {
        'current': page,
        'limit': limit,
    }

    response = requests.post(url, headers=HEADERS,data=data)
    if response.status_code == 200:
        return response.json()
    return None


def crawl_all_pages():
    # 先获取第一页数据确定总页数
    first_page = get_price_data()
    print(first_page)
    if not first_page:
        print("获取数据失败")
        return

    total = int(first_page['count'])
    limit = int(first_page['limit'])
    total_pages = (total + limit - 1) // limit  # 计算总页数
    # total_pages=3
    all_data = []
    all_data.extend(first_page['list'])

    for page in range(2, total_pages + 1):
        print(f"正在爬取第{page}页，共{total_pages}页")
        page_data = get_price_data(page, limit)
        if page_data:
            all_data.extend(page_data['list'])
        # 避免请求过快被封
        time.sleep(1)

    return all_data


# 使用示例
if __name__ == "__main__":
    import time

    all_data = crawl_all_pages()
    print(f"共爬取{len(all_data)}条数据")
    # 保存数据
    with open('price_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)