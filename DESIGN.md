# Design Document
This file should discuss how you implemented your project and why you made the design decisions you did, both technical and ethical. Your design document as a whole should be at least several paragraphs in length. Whereas your README.md is meant to be a user’s manual, consider your DESIGN.md your opportunity to give the staff a tour of your project underneath its hood.

## Technical Decisions
### In this section, share and justify the technical decisions you made.
I decided early on to stick to the technologies we were taught in class as I knew that I would struggle to learn something new on my own. I chose to use the "finance" problem set as the inspiration to my project as I found it very useful to real-world applications. Not necessarily stock picks but the overall technologies it used. HTML, CSS, Javascript, Python, Jinja, Flask, SQLITE and add-on's like Bootstrap made sense to me and I felt they were tools I could utilize and make progress with. Since I did my Final Project solo, I knew I would have very little help.

I ran into multiple design challenges. First and foremost, I knew that I would need to pull this project out of github codespace and deploy it in some manner. This was always in the back of my mind as I had only used the "online" virtual studio available to use through CS50 github codespaces. My first real challenge was to install Virtual Studio on my laptop and configure it for python, sql, and flask. I then had to configure a virtual environment so that I could run flask on my local http://127.0.0.1:5000. I was able to connect virtual studio to my own repository on github as well. This allowed me to start developing my application.

Overall I found developing this application straight-forward using the tools mentioned above. There were several challenges that I had to overcome. The first, I struggled creating a modal (popup html form) that would allow me to let users


You don't need to respond to all questions, but you might find some of the following helpful:
* What design challenge(s) did you run into while completing your project? How did you choose to address them and why?
* Was there a feature in your project you could have implemented in multiple ways? Which way did you choose, and why?
* If you used a new technology, what did you learn about this new technology? Did this technology prove to be the right tool?



## Ethical Decisions
### What motivated you to complete this project? What features did you want to create and why?
We have a need to organize lab projects. At the moment, the lab (technnical team) receives multiple requests per day from sales. This is accomplished in varying ways - phone, email, email a word document, etc. It is up to the lab to maintain a prioritization list. Sometimes there is a breakdown in communication between these two teams. For example, the technical team may not have understood that sales is placing an extremely high priority on "project A" so they continue to work on "project B." - ignoring "project A" for the time being. This causes much frustration from both parties. I decided to create this application to help eliminate this tension point. I wanted to create an application that would easily allow sales to submit requests, assign a priority, add notes, and, in real-time, show this priority list to the technical people to prioritize their work day. Both groups will always know which projects are at the top of the list. A sales person can see the same real-time list as the technical person who could be 1000 miles away.


### Who are the intended users of your project? What do they want, need, or value?
You should consider your project's users to be those who interact _directly_ with your project, as well as those who might interact with it _indirectly_, through others' use of your project.

The users intended to use my application are my sales and technical teams. The primary users are sales and technical. Secondary users are managers. 
Sales team wants: Sales wants development projects and sample requests completed as fast as possible. They want to be able to respond to their customers quickly with custom color matches as well as standard color samples. 

Sales team needs: Sales needs to have their requests addressed accurately. It is important that information be conveyed and received without error. For example, if a sales person needs a sample to be FDA compliant (for example a medical application), they cannot have the technical personnel develop and deliver a sample to a customer that is NOT FDA compliant.

Sales team values: Sales values speed. They do not have time to fill out and email word documents. They need to be able to quickly determine where their requests stand with the technical request backlog. 

Technical team wants: A method to reduce data entry. This database will eliminate copying information from a word document (sent in by sales) to an excel spreadsheet.

Technical team needs: A method to organize requests based on sales teams priorities. Since resources in the lab are limited, they need to work on the most important requests first. This application will assist them in letting sale teams easily prioritize their requests and provide real-time information to assist in prioritization.

Technical team values: Collabation with sales to ensure everyone is on the same page. They value making sure their projects are done right the first time rather than having to redo a project due to lack of provided information.


### How does your project's impact on users change as the project scales up? 
You might choose one of the following questions to reflect on:
* How could one of your project's features be misused?
There is always tension between the two groups of users in question. Sales wants everything immediately and technical needs time to develop. A famous quote used by our lab is "you can't schedule an invention." The project could be misused by our sales team in that they could still prioritize every request as "high priority." They will need to be mindful that not everything can be a high priority and they MUST learn to develop criteria for lower levels of priority. 

* Are there any types of users who might have difficulty using your project?
* If your project becomes widely adopted, are there social concerns you might anticipate?


