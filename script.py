import requests
import os
import json
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

domain = str(input())

filePrefix = str(datetime.now())


#   MX Part
mx_api_key = str(os.getenv('MX_API_KEY'))

mx_url = 'https://mxtoolbox.com/api/v1/lookup/mx/' + domain

mx_res = requests.get(url = mx_url, headers={'Authorization': mx_api_key})

mx_data = mx_res.json()

if not mx_data['Failed']:

    print('The MX info is dumped in ' + filePrefix + '_mx.json')

    mx_datas = json.dumps(mx_data)

    file_json = open(filePrefix + '_mx.json', 'w')
    file_json.write(mx_datas)
    file_json.close()

else:
    print('The MX info does not exist for this domain')

#   SPF Part

mx_api_key = str(os.getenv('MX_API_KEY'))

spf_url = 'https://mxtoolbox.com/api/v1/lookup/spf/' + domain

spf_res = requests.get(url = spf_url, headers={'Authorization': mx_api_key})

spf_data = spf_res.json()

if not spf_data['Failed']:

    print('The SPF info is dumped in ' + filePrefix + '_spf.json')

    spf_datas = json.dumps(spf_data)

    file_json = open(filePrefix + '_spf.json', 'w')
    file_json.write(spf_datas)
    file_json.close()

else:
    print('The SPF info does not exist for this domain')


#   WHOis Part

whois_api_key = str(os.getenv('WHOIS_XML_API'))

whois_url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=' + whois_api_key + '&domainName=' + domain + '&outputFormat=JSON'

whois_r =  requests.get(url = whois_url)

whois_data = whois_r.json()


if 'registrant' in whois_data['WhoisRecord'].keys():

    if whois_data['WhoisRecord']['registrant']['organization'] == "Whois Privacy Service":

        print('The WHOis Data is not Public, more info in the dumped file ' + filePrefix + '_whois.json')

    else:

        print('The WHOis Data is public, it is available in ' + filePrefix + '_whois.json')
    
    whois_datas = json.dumps(whois_data)
    file_json = open(filePrefix + '_whois.json', 'w')
    file_json.write(whois_datas)
    file_json.close()

else:

    print('The WHOis Data for this domain may not exist')



#   Age of domain:  %b %d %Y %I:%M%p    Jun 12 2013 5:30PM 

if 'dataError' in whois_data['WhoisRecord']:
    
    print('No date info, due to absence of any WHOis Data')

else:

    date = whois_data['WhoisRecord']['createdDate'][:10]

    age = datetime.strptime(date, '%Y-%m-%d')

    print(age, datetime.now())

    diff = 12*(datetime.now().year - age.year) + (datetime.now().month - age.month)

    if diff < 2:
        print('The domain is quite new, please refrain from sending email campaigns!')

    else:
        print('The domain is sufficiently aged, send away!')


#   RBL Check

rbl_api_key = str(os.getenv('RBL_API_KEY'))

rbl_url = 'https://api.hetrixtools.com/v2/' + rbl_api_key + '/blacklist-check/domain/' + domain + '/'

rbl_r = requests.get(url = rbl_url)

rbl_data = rbl_r.json()

rbl_datas = json.dumps(rbl_data)

print('The RBL info is dumped in ' + filePrefix + '_rbl.json')

file_json = open(filePrefix + '_rbl.json', 'w')
file_json.write(rbl_datas)
file_json.close()