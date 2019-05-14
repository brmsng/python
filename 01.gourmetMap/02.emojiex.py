from lxml import html
import requests

resp = requests.get('https://www.webpagefx.com/tools/emoji-cheat-sheet/')
page = html.document_fromstring(resp.content)

body = page.find('body')
top_header = body.find('h2')


print(top_header.text)

headers_and_lists = [sib for sib in top_header.itersiblings()]

print(headers_and_lists)


