from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familar with')
unskill=input('>')
print(f"Filtering out {unskill}")
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=PYHTON&txtLocation=').text
    soup =BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            links=job.header.h2.a['href']
            if unskill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name : {company_name.strip()}\n")
                    f.write(f"Required Skills : {skills.strip()}\n")
                    f.write(f"Link : {links.strip()}")
                print(f'file saved: {index}')
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=1
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)
        