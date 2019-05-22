# WTI RESTful - Get CSV Temperature.

This is Python3 script that talks to WTI devices with RESTful calls and gets the current temperature and date/time of the device and outputs the data in CSV format, looping
every minute, to exit the loop press ^C.

This `Get CSV Temperature` Python3 script will work on any modern WTI device, the temperature RESTful call is universal on all WTI OOB and PDU type devices making it the perfect starting point to start learning and experimenting with the RESTful interface.

# To Configure Python Script:
By default, WTI has setup a unit that everyone can try. The default BASE_PATH and USERNAME and PASSWORD can be used to query the WTI device without physically having one and get the general look and feel of the calls.

If you have your own WTI device, in the Python script you need to change:
- BASE_PATH to the address of your WTI device
- USERNAME and PASSWORD to the correct values for your WTI device.

On the WTI device itself you need to make sure that the user you are logging on has "Service Access" to run RESTful API calls. If you need help with this, you can get details at this link. http://wtiknows.com/2018/06/29/restful-user-service-access/


# To Run:
`python tempcomma.py`

The current temperature, degree units and the timestamp of the device will display on the screen in CSV format.

# RESTful API Documentation:

The HTML, RAML OR OpenAPI/Swagger file relating to the RESTful API calls can be found here:

https://www.wti.com/t-wti-restful-api-download.aspx

# Contact US
If you have any questions, comments or suggestions you can email us at kenp@wti.com

# About Us
WTI - Western Telematic, Inc.
5 Sterling, Irvine, California 92618

Western Telematic Inc. was founded in 1964 and is an industry leader in designing and manufacturing power management and remote console management solutions for data centers and global network locations.
Our extensive product line includes Intelligent PDUs for remote power distribution, metering, reporting and control, Serial Console Servers, RJ45 A/B Fallback Switches and Automatic Power Transfer Switches.
