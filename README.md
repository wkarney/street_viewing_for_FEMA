# Project SightVisit: Collaboration Between New Light Technologies and General Assembly's Team StreetView

## Table of Contents
  - [Team Introduction](#team-introduction)
  - [Problem Statement](#problem-statement)
  - [Executive Summary](#executive-summary)
  - [Use Case Scenario](#use-case-scenario)
  - [SightVisit App](#sightvisit-app)
  - [Data Acquisition](#data-acquisition)
  - [Required Libraries](#required-libraries)
  - [Opportunities for Further Improvements](#opportunities-for-further-improvements)
  - [References](#references)

## Team Introduction

[New Light Technologies](https://www.newlight.com) is a small, award-winning organization based in Washington, D.C. that provides solutions to government, commercial, and non-profit clients. NLT is a team of dedicated technologists, scientists, engineers, designers, and strategists working on some of the most interesting, challenging, and important assignments in the world, ranging from disaster response to enabling growing telecommunications networks to providing healthcare to Americans. Some of the organizations they work with include FEMA (the Federal Emergency Management Agency), USAID (the United States Agency for International Development), the U.S. Census Bureau, and The World Bank.

[Ran Goldblatt, Ph.D.](https://newlighttechnologies.com/staff/ran-goldblatt/) our contact with NLT, is a Chief Scientist and a Senior Consultant at New Light Technologies. He is a remote sensing scientist, with extensive experience in geospatial analysis and image processing. Ran’s work supports disaster response through the development of innovative methods for data fusion, image processing, management and consolidation of multi-sources imagery, at FEMA, as well as other NLT clients.

Team StreetView is composed of full-time data science immersive students at [General Assembly (GA)](https://generalassemb.ly). We draw our experiences from a diversity of backgrounds and industry experiences and are collaborating with NLT on the specific task of interest for which we have created a framework and concept for the SightVisit application.

Our team is [Stevie DiSalvo](https://www.linkedin.com/in/stephanie-disalvo/), [John D Hazard](https://www.linkedin.com/in/jdhazard/), [Will Karnasiewicz](https://www.linkedin.com/in/wkarnasiewicz/), and [Omar Raheem](https://www.linkedin.com/in/omar-raheem-9153431a/).

## Problem Statement

During the recovery phase immediately following a disaster, FEMA performs damage assessment “on the ground” to assess the level of damage caused to residential parcels and to critical infrastructure. To assure an accurate estimation of the damage, it is important to understand the condition of the structures prior to the event. To help and guide the damage assessment efforts following a disaster, and to assist the surveyors in identification of the structures of interest, SightVisit. It will retrieve screen shots of the structures from Google Street View. A damage assessment form, which, in addition to relevant information about the level of damage to the structures, will also provide a pre-event photo of the assessed structure.

## Executive Summary

## Use Case Scenario

Carol Evans is an emergency management specialist at FEMA. Days after a disaster, she's out in the field assessing residential properties. She hops out of her car and takes a photo of the first house she sees in disrepair. She uploads the photo to SightVisit, sees the photo she took as well as an image of the home prior to the disaster. The web app also displays a value estimate of the house and additional property details (such as square footage, number of bedrooms/bathrooms, and housing type).

## SightVisit App



## Data Acquisition

Data integration is provided through the following APIs: 
* [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/intro)
* [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start)
* [Zillow GetDeepSearch-Results API](https://www.zillow.com/howto/api/GetDeepSearchResults.htm)

For ease of use, we have utilized the following Python API Wrappers:
*  [google streetview](https://github.com/rrwen/google_streetview)
*  [pyzillow](https://github.com/hanneshapke/pyzillow)
*  [pygeocoder](pygeocoder)

Note that Google charges for API calls to its Google Maps APIs, but provides a free 1-year $300 credit to its Cloud Platform.

## Required Libraries
* Python 3.x
* Flask 1.0.2
* Flask-Cors 3.0.7
* Flask-Uploads 0.2.1
* Flask-WTF 0.14.2
* Pillow 5.4.1
* pyzillow 0.5.5
* google_streetview 1.2.9
* pygeocoder 1.2.5
* exif 0.5.1

## Opportunities for Further Improvements

* SQL/Database Integration
    - Secure cloud storage of damage information
    - Deploy live web application
* Mobile App
    - Develop native application for iOS and/or Android
* Satellite Data
    - Incorporate satellite imagery for relevent disaster situations
* Insurer Partnership Integration
    - Work with corporate partners to streamline processes and standardize forms
    - Incorporate additional data resources to satisfy dual requirements of FEMA and participating insurance companies 
* Machine Learning
    - Image recognition to classify damage levels and estimate expenses

## References
* [*FEMA Damage Assesment Operations Manual*](https://www.fema.gov/media-library-data/1459972926996-a31eb90a2741e86699ef34ce2069663a/PDAManualFinal6.pdf)
* [Hurricane Sandy Photo by Chester Green](https://www.flickr.com/photos/24531833@N02/8162005749/in/photolist-drfpX4-drfoAJ-drfsto-dp2FKF-drfqsE-drfhFV-dp3D53-dp4xyV-doEcnm-dqJRKr-doVMXY-dqK27z-dpkrnc-dqJPsF-dvjbKq-dqJWsu-dqJUh7-dqJVws-dtcnju-dqJYoa-drfo2D-doV9fm-dqJVLu-doVEX8-dqJY1m-doXbEJ-fAZ2Ap-drwzVa-dqK5mW-dqJLxi-dqK6eq-dtbnax-sJjkTN-dqJT85-dtbndk-drfjXi-dqK4kE-stWQj7-dpkxxH-drfqCR-drfqUy-dqK8g3-su3DRE-doVF5k-dqJXqb-dp3aCf-dpjmxT-dy7Tz6-dwYf5a-dqh3VX)
* [Hurricane Ike Photo by Flickr user "Grue"](https://www.flickr.com/photos/grue/2886868164/in/photolist-TDJ27B-aPpNhK-8JUUYq-rHXa9-dGUp4-6oUzjN-LrrAo-6mDYdV-4DCkU-2cbqVLP-VpNBb1-65p5f2-qKTW37-5p6Xk3-4dbnrc-djn8T-cMMXuU-q6EuBV-5XLNfX-dAYod6-2fovhc-r1arYw-8r1is2-nnZS4-6ugFFr-9gUewF-VsuFgH-7yCPo6-5wfSDc-Q3miML-9TiJs-29pW6M7-4kfVP1-mbxBc-5mNwkv-YxwoER-kmjyu-usNKC-5B9CHd-apNq68-6mK4w1-aPpNiB-2b5tiXW-9gXmmy-5p6XfJ-2c6VV8N-5h5Mzk-7gRKuQ-fezVU-6ftKvx)