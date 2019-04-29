# Project SightVisit: Collaboration Between New Light Technologies and General Assembly's Team StreetView

## Table of Contents
* [Team Introduction](#user-content-team-introduction)
* [Problem Statement](#user-content-problem-statement)
* [Executive Summary](#user-content-executive-summary)
* [Use Case Scenario](#user-content-use-case-scenario)
* [Data Acquisition and Processing](#user-content-data-acquisition-and-processing)
* [Required Libraries](#user-content-required-libraries)
* [Sight Visit App](#user-content-sightvisit-app)
* [Opportunities for Further Improvements](#user-content-opportunities-for-further-improvements)

### Team Introduction

[New Light Technologies](https://www.newlight.com) is a small, award-winning organization based in Washington, D.C. that provides solutions to government, commercial, and non-profit clients. NLT is a team of dedicated technologists, scientists, engineers, designers, and strategists working on some of the most interesting, challenging, and important assignments in the world, ranging from disaster response to enabling growing telecommunications networks to providing healthcare to Americans. Some of the organizations they work with include FEMA (the Federal Emergency Management Agency), USAID (the United States Agency for International Development), the U.S. Census Bureau, and The World Bank.

[Ran Goldblatt, Ph.D.](https://newlighttechnologies.com/staff/ran-goldblatt/) our contact with NLT, is a Chief Scientist and a Senior Consultant at New Light Technologies. He is a remote sensing scientist, with extensive experience in geospatial analysis and image processing. Ran’s work supports disaster response through the development of innovative methods for data fusion, image processing, management and consolidation of multi-sources imagery, at FEMA, as well as other NLT clients.

Team StreetView is composed of full-time data science immersive students at [General Assembly (GA)](https://generalassemb.ly). We draw our experiences from a diversity of backgrounds and industry experiences and are collaborating with NLT on a specific task of interest for which we have created a framework and concept for the SightVisit application.

Our team is [Stevie DiSalvo](https://www.linkedin.com/in/stephanie-disalvo/), [John D Hazard](https://www.linkedin.com/in/jdhazard/), [Will Karnasiewicz](https://www.linkedin.com/in/wkarnasiewicz/), and [Omar Raheem](https://www.linkedin.com/in/omar-raheem-9153431a/).

### Problem Statement

During the recovery phase immediately following a disaster, FEMA performs damage assessment “on the ground” to assess the level of damage caused to residential parcels and to critical infrastructure. To assure an accurate estimation of the damage, it is important to understand the condition of the structures prior to the event. To help and guide the damage assessment efforts following a disaster, and to assist the surveyors in identification of the structures of interest, SightVisit. It will retrieve screen shots of the structures from Google Street View. A damage assessment form, which, in addition to relevant information about the level of damage to the structures, will also provide a pre-event photo of the assessed structure.

### Executive Summary

The Department of Homeland Security Federal Emergency Management Agency's (FEMA) assists citizens and first responders by ensuring accuracy, consistency, and efficiency in their damage response teams. The challenge faced by local organizations, both in the initial assessment and verification stages, is to quickly and accurately make damage appraisals. Unfortunately, not every volunteer is thoroughly trained and qualified to collect this data.

It’s challenging to train and maintain a volunteer staff with complete knowledge and tools for the required damage assessments during a crisis. Accuracy is problematic without detailed photos before and after an occurrence. As the urgency at disaster zones escalates, consistent, valid reports become even more integral and even more challenging. When volunteers lack handy, easily understood tools, it holds up effective resource deployment.

SightVisit will empower FEMA damage assessment teams, professionally trained or not, to conduct accurate, consistent, site visits. They can quickly access before and after photos of a site, and review a repository of all visits. It's easy to manage and deliver the results to local, county, and state decision makers so they can verify sites remotely. SightVisit maximizes FEMA’s ability to aid to those who need it most and assures proper oversight of all stages of the damage assessment. Our powerful functions will enable you to upload a photo and pertinent details about each location instantly. We’re moving the process away from an analog paper and pencil to an online form, and we can maintain a database of all site visits recorded on any street in any town.

Here at Team Street View, with the cooperation of Newlight Technologies, we love to empower our users with powerful tools utilizing sound data science and reliable results. We're a thoughtful team of data scientists committed to bringing the best possible user experience for local volunteers and adjusters to get their best work done.

We've enjoyed partnering with Newlight Technologies and FEMA to transform how damage assessment teams collect data, and we’re excited to make SightVisit a vital tool in damage assessment and increase the already robust response to crises for all citizens.

If you're ready to move from stacks of complex paper forms to a ready to use, sustainable, web application, Team Street View is willing to take you there. The repository details how we'll do it and what you can expect along the way.

### Use Case Scenario

Carol is a disaster assessment lead at FEMA heading to the field, days after a disaster. She has been tasked to quickly scan the disaster zone and assess the damage to residential property.

She jumps out of her truck, starts walking the street, and sees the first house in disrepair. She pulls out her phone, opens the SightVisit app, and takes a photograph facing the house. Upon taking a photograph she sees a page displaying the photo she took, the image of the home before the disaster, a value estimate of the house, as well as pertinent information regarding the number of stories, bedrooms, and square footage, to give the complete summary of that particular property.

At the backend, each photograph she takes is stored, along with the summary information, and available to be accessed at a later time or when web connectivity is available again. However, ideally, even with limited web connectivity, a low-resolution image can be uploaded directly in real-time to the disaster response team at the home office. This data can be aggregated to assess total damage and real-time statistics relayed to appropriate agencies for assessment, disaster management, and appropriation purposes.

-- Thanks to the General Assembly DSI-6 Team StreetView for this example. 

### Data Acquisition and Processing

Data integration is provided through the following APIs:

Google Street View Static API
Google Geocoding API
Zillow GetDeepSearch-Results API
For ease of use, we have utilized the following Python API Wrappers:

google streetview
pyzillow
pygeocoder
Note that Google charges for API calls to its Google Maps APIs, but provides a free 1-year $300 credit to its Cloud Platform.

### Required Libraries

Python 3.x
Flask 1.0.2
Flask-Cors 3.0.7
Flask-Uploads 0.2.1
Flask-WTF 0.14.2
Pillow 5.4.1
pyzillow 0.5.5
google_streetview 1.2.9
pygeocoder 1.2.5
exif 0.5.1



### SightVisit App

Is currently under development. 

### Opportunities for Further Improvements

SQL/Database Integration
Secure cloud storage of damage information
Deploy live web application
Mobile App
Develop native application for iOS and/or Android
Satellite Data
Incorporate satellite imagery for relevent disaster situations
Insurer Partnership Integration
Work with corporate partners to streamline processes and standardize forms
Incorporate additional data resources to satisfy dual requirements of FEMA and participating insurance companies
Machine Learning
Image recognition to classify damage levels and estimate expenses

### References

FEMA Damage Assesment Operations Manual
Hurricane Sandy Photo by Chester Green
Hurricane Ike Photo by Flickr user "Grue"



