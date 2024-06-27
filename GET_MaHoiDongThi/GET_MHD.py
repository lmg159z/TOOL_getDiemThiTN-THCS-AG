import requests
from bs4 import BeautifulSoup
import decimal, time,re

with open("mahoidong.csv", "a") as f:
  link = "https://baoangiang.com.vn/tra-cuu-diem-thi-vao-lop-10.html?tensbd="
  def res_data(mhd, start):
    res = requests.get(link+mhd+start)
    if res.status_code == 200:
      html_content = res.text
      data =  html_content[html_content.find("""<table class="table table-striped">""") +416 : html_content.find("""</table>""")].split("""</tr>""")
      handle_data(data)
    else:
      print(f"Failed to retrieve HTML. Status code: {response.status_code}")
    # sử lý data 
  def handle_data(array_data):
    soup = BeautifulSoup("".join(array_data), 'html.parser')
    td_tags = soup.find_all('td')
    content_list = []
    for td in td_tags:
     content = td.get_text().replace(',', '.')
     content_list.append(content)
    if content_list != []:
      new_array = []
      new_array.append("'" + content_list[0][0:4])
      new_array.append(content_list[4])
      result_string = ', '.join(new_array)
     
      print(result_string)
      f.write(result_string + "\n")
     # data_diemso += result_string + "\n"
  #  else:
      #print("Sbd ko hop le")
      
      
  bd  = 1  
  start = 100
  while bd <= 5000:
   if len(str(start)) == 3:
     go = "0" + str(start)
     res_data(go, "0001")
   if len(str(start)) == 4:
     go = str(start)
     res_data(go, "0001")
   bd += 1
   start += 1