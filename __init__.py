import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
for page in range(0,30):
    url = "https://tieba.baidu.com/p/8767638517?pn={page}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)

    """
    ----------------------------------------------------------------
    """
    # file_path = 'TTBT.txt'
    # with open(file_path, 'r', encoding='utf-8') as file:
    #     # 读取文件内容并存储到变量中
    #     html_content = file.read()
    # soup = BeautifulSoup(html_content, 'html.parser')


    # Get IP location
    ips = []
    for span in soup.find_all('span', text=re.compile('IP属地')):
        ips.append(span.text)
    # print(ips)

    # Get Time
    timestamp_span_list = [span.text for span in soup.find_all('span', text=re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'))]
    # print(timestamp_span_list)

    # Get content
    comment_div_list = [span.text for span in soup.find_all('div', class_='d_post_content j_d_post_content')]
    # print(comment_div_list)

    # # Get user id
    username_tags = [span.text for span in soup.find_all('a', {'class': ['p_author_name', 'j_user_card']})]
    # print(username_tags)

    # 创建一个数据框
    print(len(ips),len(timestamp_span_list),len(comment_div_list),len(username_tags))
    df = pd.DataFrame({
        'ip': ips,
        'location': timestamp_span_list,
        'comment': comment_div_list,
        'id_name': username_tags
    })

    # 将数据框写入 Excel 文件
    df.to_excel('data.xlsx', index=False)
    print(f'第{page}页爬取完毕')