import re


def html2text(html_text):
    # 删除注释
    text = re.sub(r'<!--.*?-->', '', html_text, flags=re.S)
    # 删除P标签，并加入换行
    text = re.sub(r'<[pP][^>]*?>', '\n\n', text)
    # 删除script代码
    text = re.sub(r'<script[^>]*?>.*?</script>', '', text, flags=re.I | re.S)
    # 删除style代码
    text = re.sub(r'<style[^>]*?>.*?</style>', '', text, flags=re.I | re.S)
    # 删除其他标签
    text = re.sub(r'<[^>]*?>', '', text)
    # 删除只包含空格字符的行
    text = re.sub(r'\n(?:[ \t]+\n)+', '\n', text)
    # 删除多个换行，只保留一个
    text = re.sub(r'\n\n+', '\n\n', text.strip())
    return text


if __name__ == '__main__':
    from urllib.request import urlopen
    url = 'http://www.dust8.com'
    html_text = urlopen(url).read().decode()
    text = html2text(html_text)
    print(text)
