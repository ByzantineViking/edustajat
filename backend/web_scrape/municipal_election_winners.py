from bs4 import BeautifulSoup


content = '<div>hello world</div>'
soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
tags = soup.find_all('div')
