# Endorse the Skills of All People in Your Contacts
A Python Selenium bot to automate endorsing the skills of people in Your contacts on LinkedIn

<b>Do a good deed, endorse them all and all their skills!</b>

<b>30 August 2023 major upgrades:</b> 

  •  added `user agent`, `cookies` and `local storage` support to keep the login information from the last session and to reduce LinkedIn automation detection.

  • improved logic of getting profiles who's skills to endorse: since there is a weekly limit of profiles to get in the search panel, the script searches only up to those still unendorsed (endorsed contacts are stored inside `endorsed.txt`, as always have been).

  • improved algorithm for clicking "Endorse" buttons, speed increased 10&#8209;20 times.

## How To Use

Screen resolution and width is rather important when it comes to LinkedIn.
<br> The script is tested on 1280px and 1366px screen width resolutions.  It is working!

### Change:
  
  •  Your browser information You usually use to browse LinkedIn (to reduce automation detection) `user_agent`
   
You can find your current browser's user-agent by searching ***"What's my user-agent?"*** in any search engine, it is just a string.

  •  The email to login on LinkedIn `username`
  
  •  Your password `password`
    
### Install Python:

  •  https://www.python.org/downloads/

### Install PIP If it Has Not been Installed With Python Automatically:

  •  https://pip.pypa.io/en/stable/installation/

### Install Libraries (please open the command line interface):

  •  Selenium `pip install selenium`

### Endorse Them All!

  •  double-click on `start.bat`

### Imporant Notes

  •  To be able to skip the endorsed connections, the links of people endorsed are stored in `endorsed.txt`
  
The fresh version is always here: https://github.com/nakigoe/linkedin-endorse-bot
<br> Please write if You would like programming lessons: nakigoetenshi@gmail.com
<br> $60 per hour lessons

<h2 style="margin: 0 auto" align="center">Put stars on GitHub and share!!!</h2>
<br>
<p style="margin: 0 auto" align="center">Please cast an eye on my website:</p>
<h1><a href="https://nakigoe.org/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>

<p style="margin: 0 auto" align="center">© NAKIGOE.ORG</p> 

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars to the repositories!</p>