"""[https://dgplug.org/irclogs/2017/](https://dgplug.org/irclogs/2017/)
Pass the above URL to a function, it will find and download all the log files from there. Use `BeautifulSoup4` and `requests` module for this.
"""

def get_logs_and_info(url):
    import requests
    from bs4 import BeautifulSoup
    import pprint

    words_spoken = {}
    logs_page = requests.get(url).text
    soup = BeautifulSoup(logs_page, "lxml")
    log_links = [url+link.get('href') for link in soup.find_all('a') if link.text.startswith('Logs')]

    for link in log_links:
        with open(link.split('/')[-1] , 'w') as log_file:
            log = requests.get(link).text
            log_file.write(log)

            log = log.split('\n')[1:-1]
            for line in log:
                tokens = line.split()
                name = tokens[1].strip('<>')
                if name in words_spoken:
                    words_spoken[name] += len(tokens)-2
                else:
                    words_spoken[name] = len(tokens)-2
    pprint.pprint(words_spoken)


get_logs_and_info('https://dgplug.org/irclogs/2017/')
