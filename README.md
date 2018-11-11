## UnifyID Challenge - Fraud Friction

Assume you have a file with the user's past record of login attempts: 

   FRAUD 8.8.8.8 
   LOGIN 22.4.62.188 
   ... 

This file is a list of IP addresses from which a login was attempted.  The list may contain hundreds or thousands of entries with some IP addresses appearing many times if the user frequently logs in from the same place.  FRAUD means that this IP was used for a known fraudulent login attempt, and LOGIN means this login attempt was not known to be fraudulent.   

Given this file, score a new login attempt using the following criteria: 
Let the "distance" between two IP addresses be the physical distance between the IP’s latitude/longitude coordinates. You can use IPinfo.io for latitude/longitude location information, and you may use the latitude/longitude distance formula of your choice. 
The score will be the mile distance between the new login IP and the closest IP found in the input list. 
If the closest previous IP was marked as FRAUD, you should double the score before returning your final answer. 

### Requirements
* API access to IPinfo.io with access token generated 
* Python libraries required:
  * Numpy
  * ipinfo

### Guide on how-to build the project
Run this on terminal:
* python Fraud_ip_detection.py --filepath=<file that conatins the lsit of IP's> --acessToken=<access token to access IPinfo.io>

### Follow Up Questions
#### 1.What circumstances may lead to false positives or false negatives when using solely this score?
* The current assumption is that higher the score, higher the probability that it is a fraudulant IP. According to this statement "If the closest previous IP was marked as FRAUD, you should double the score before returning your final answer" we blindly consider any IP closer to a fraudulant IP is also fraudulant. This assumption should be backed up by various other factors(other than latitude/longitude), else would lead to false positives or false negatives.
* If there is an oulier IP, far from any known IP locations, then it's distance to the nearest IP is not a good factor to measure if it's fraudulant or not.

#### 2.What challenges are there with computing distances based on latitude/longitude? 
As the number of new users's increases computing distances will linearly increase the time complexity. Hence, we should impart some sort of filtering algorithm to reduce the number of distance calculations.

### Further Considerations
* Fetching IP details like coordinates for a list of IPs using IPinfo.io python API is currently not supported. Hence, building a solution to fetch this information at once would save us a lot of time.
* Caching the IP information would also reduce the execution time. 
* Saving the fetched IP information into a local database would save us IPinfo.io API calls. This will be an efficient way of managing the IP details.
* Currently I have used Euclidean distance to calculate distance between 2 coordinates. But, providing an option of various distance functions would be another improvement.
