from unittest import result
from webbrowser import get
import requests
from bs4 import BeautifulSoup

#https://id.indeed.com/lowongan-kerja?q=data%20scientist&l=Indonesia&vjk=5a2f8363e0aa34ed
#https://www.jobstreet.co.id/id/job-search/data-science-jobs-in-jakarta-raya/
#jcs-JobTitle css-jspxzf eu4oa1w0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62 '
}

def getdata(url):
    r = requests.get(url)
    return r.text

def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata,'html.parser')
    return(soup)

def job_data(soup):
    data_str = ""
    for item in soup.find_all("a", class_="sx2jih0"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return(result_1)

def company_data(soup):
    data_str = ""
    result = ""
    for item in soup.find_all("a", class_="sx2jih0 sx2jihf QytTO"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return(result_1)

def location_data(soup):
    data_str = ""
    result = ""
    for item in soup.find_all("span", class_="sx2jih0 zcydq84u zcydq80 iwjz4h0"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return(result_1)

    #     print(data_str)
    # result_1 = data_str.split("\n")

    # res = []
    # for i in range (1, len(result_1)):
    #     if len(result_1[i]):
    #         res.append(result_1[i])
    # return(res)

if __name__ == "__main__":
    job = "digital-marketing"
    Location = "Jakarta-Raya"
    #url = "https://id.indeed.com/lowongan-kerja?q="+job+"&l="+Location+"&vjk=5a2f8363e0aa34ed"
    url = "https://www.jobstreet.co.id/id/job-search/"+job+"-jobs-in-"+Location+"/"
    print(getdata(url))
    # soup = html_code(url)

    # job_res = job_data(soup)
    # com_res = company_data(soup)
    # loc_res = location_data(soup)

    # temp = 0
    # for i in range(1, len(job_res)):
    #     j = temp
    #     for j in range(temp, 2+temp):
    #         print("Company Name : " + com_res[j])
    #         print("Location : " +loc_res[j])

    #     temp = j
    #     print("Job : " + job_res[i])
    #     print("-------------------------")