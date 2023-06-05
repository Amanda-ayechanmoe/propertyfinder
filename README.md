# Project Name
> ETL job for property data from https://www.propertyguru.com.sg using python, airflow, AWS S3, AWS Glue, AWS Athena, docker and Tableau.
> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- This project intend to help users to automate the searching of property that they are looking for based on the pre-stroed search criteria and get insight of property data.
- In this project Streamlit is used for web application to let users to submit their search criteria such as MRT and property type room or whole unit. Once user has submitted search criterias, those are stroed in S3 bucket.
![Example screenshot](./img/Screenshot01.png)
- Airlflow is used to orchestrate the following tasks:
  1. Obtaining the search criteria from S3 bucket.
  2. Calling customized API built with FLASK for web scrapping from https://www.propertyguru.com.sg using selenuim and beautiful soup. 
  3. Upload the extracted data to S3 bucket.
<!-- Screenshot here -->
- AWS Glue job is used to transform the data written in python. Transfromed data is stored in S3 bucket.
- AWS Athena is used to created database from transformed data S3 bucket and run query driectly on S3 for analysis.
- Query result from AWS Athena is viauslize using Tableau.
<!-- Screenshot here -->
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Tech 1 - version 1.0
- Tech 2 - version 2.0
- Tech 3 - version 3.0


## Features
List the ready features here:
- Awesome feature 1
- Awesome feature 2
- Awesome feature 3


## Screenshots
<!-- ![Example screenshot](./img/screenshot.png) -->
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
