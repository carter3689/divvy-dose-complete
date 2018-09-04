# DivvyDose API Project 

Divvy Dose API code test

# Getting Started

The following instructions will cover useful information to start the docker container for the API project

# Prerequisities for docker 

In order to run this container you will need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

# Usage

## Building/Running Docker Image

### Build

```shell
docker build -t divvy_dose .
```

### Run
```shell
docker run -p 5000:5000 -it --rm --name my-running-app divvy_dose
```

# In Case of Emergency (Issues with docker)
create a virtual envirionment using virtualenv

* To install virtualenv use:
```shell
pip install virtualenv venv
```

* To start virtualenv:
- (Windows)
```shell
foo\bar\venv\Scripts\activate
```
-(Mac)
```shell
source venv/bin/activate
```

### Next steps:
- Navigate to working directory
- run ```pip install -r requirements.txt```
* To run the project
- run ```python divvydose_api_1.py```

# Testing
In terms of testing the API:
* I would test for explict responses to the API calls. I would also test for the structure in the body of the response as well.
* Regarding the user input endpoint: I would test for an edgecase specifically targeting blank parameters.
    - I would also throw in random characters and numbers to find out if a response would come back. In the off chance it does, I would want to think about what would be deemed as an "acceptable" username

## To run the testing file:
---
- Run ```shell
py.test test_divvydose.tavern.yaml  -v```
### Further Documentation regarding endpoints

| EndPoint        | Description | 
| ------------- |:-------------:| 
| /commits      | Total number of commits |
| /issuse       | Total number of issues  |
| /languages-used| Total number of languages-used     |
| /stars        | Total number of stars   | 
| /total        | Total number of public repos and forks     |
| /user         | User provided Info - returns results for username      | 
| /watchers     | Total number of watchers|


## Observations regarding project

* The toughest part of the project was finding an optimal way to query each API(GitHub/BitBucket) for seperate infomation, placing the results in one endpoint and making it readable. Which is why I opted for seperate endpoints for specific data.

* With extensive searching, finding total size of accounts and repo topics readily presented.