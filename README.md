# domain-health

There are many factors on which the deliverability of an email depends, including but not limited to the presence of MX and SPF information, the public nature of WHOis information, the age of the domain and the listing of the domain on RBLs.

These are grave problems in Sales position where the mere placement of an engagement email can mean the difference between closing a deal and losing it. Thus, this tool helps you determine the "health" of your domain with respect to these factors.

## This a command line utility for the following tasks

* Querying domain MX information using `mxtoolbox` API

* Querying domain SPF information using `mxtoolbox` API

* Checking if the WHOis information exists or if it's private or not using `WHOisXML` API

* Checking the age of the domain using the information obtained from the above API

* Checking if the domain is listed on over 160+ blacklists `hetrixtools` API
