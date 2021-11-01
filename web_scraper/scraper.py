import requests
from bs4 import BeautifulSoup

domain = "https://en.wikipedia.org"
wikipedia_url = f"{domain}/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    """
    get_citations_needed takes in a url and returns an integer
    """
    response = requests.get(wikipedia_url)
    html_test = response.text
    soup = BeautifulSoup(html_test,"html.parser")
    
    citations_count = soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    return len(citations_count)
# print(get_citations_needed_count(wikipedia_url))

def get_citations_needed_report(url):
    """
    get_citations_needed_report takes in a url and returns a string
    the string should be formatted with each citation needed on own line, in order found.
    """
    report = ""
    response = requests.get(wikipedia_url)
    html_test = response.text
    
    soup = BeautifulSoup(html_test,"html.parser")
   
    citations = soup.find_all("sup",class_="noprint Inline-Template Template-Fact") 
    for i in citations:
        report += f"{(i.parent.text)}\n"
    # with open("report.html","w") as file:
    #     file.write(report)
    

    return report
print(get_citations_needed_report(wikipedia_url))