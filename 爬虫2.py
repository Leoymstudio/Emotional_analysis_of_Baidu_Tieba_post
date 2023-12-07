import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 创建一个数据框
all_data_df = pd.DataFrame(columns=['ip', 'location', 'comment', 'id_name'])

for page in range(0, 19):
    url = f"https://tieba.baidu.com/p/8766137968?pn={page}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, 'html.parser')

    # Get IP location
    ips = [span.text for span in soup.find_all('span', text=re.compile('IP属地'))]

    # Get Time
    timestamp_span_list = [span.text for span in soup.find_all('span', text=re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'))]

    # Get content
    comment_div_list = [span.text for span in soup.find_all('div', class_='d_post_content j_d_post_content')]

    # Get user id
    username_tags = [span.text for span in soup.find_all('a', {'class': ['p_author_name', 'j_user_card']})]

    # 创建一个数据框
    page_data_df = pd.DataFrame({
        'ip': ips,
        'timestamp': timestamp_span_list,
        'comment': comment_div_list,
        'id_name': username_tags
    })

    # 将新数据追加到已有的数据框后
    all_data_df = pd.concat([all_data_df, page_data_df], ignore_index=True)

    print(f'第{page}页爬取完毕')

# 将所有数据写入 Excel 文件
all_data_df.to_excel('all_data2.xlsx', index=False)
print('所有数据保存为 all_data2.xlsx')