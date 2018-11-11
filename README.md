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
* Python PIP package
* API access to IPinfo.io with access token generated 
* Python libraries required:
  * Numpy
  * ipinfo

### Guide on how-to build the project
* 

### Follow Up Questions
#### 1.What circumstances may lead to false positives or false negatives when using solely this score? 

#### 2.What challenges are there with computing distances based on latitude/longitude? 

### Further Considerations
