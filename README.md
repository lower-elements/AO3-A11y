# AO3-A11y.  
## Important disclaimer.
This project is under active development. Many features might not yet be present, or some things might not work at all. Please do take this in to account if you wish to test the product, or contribute to it.  
## What is this?  
Whilst hanging out and chatting, we've came up with an idea for a minimal and accessible reader for the Archive Of Our Own fan fiction website, that works with screen readers, is cross platform, and is very easy to use.  
## Design and features.  
This project is written in Python, with WX py used as the prefered UI framework, due to it's versatility, accessibility as well as portability.  
On each OS, it's native UI API will be utilised, thus making everything accessible out of the box.  
For fetching metadata and work content, reading and writing comments, and doing anything else involving connection to the AO3 website, we use [this unofficial API.](https://pypi.org/project/ao3-api/)  
### What we've done already
* A functional login system. In the current state user information is not used for anything, however.
* Loading works and reading them.
### Features in the pipeline
* Browse and read through your favorite fan fiction in an easy to use, clean user interface, designed to work specifically with screen readers.  
* Availability on all major platforms. No matter if you're on your M1 macBook Pro in a train, in front of your Linux workstation, or your Windows school laptop, you will allways be able to take your favorite fan fiction with you, anywhere you want. Mobile support might come in a very distant future once the desktop apps are ready.  
* Give kudos and comment on works.  
* Download works in various formats.  
