# Skattetat service
Skattetat service is one of multiple micro services for redusert foreldrebetaling. Visit the [main repo](https://github.com/Altinn/summer-camp-2021) to get an overview and read more documentation.

Skattetat service is intended to be a communication layer between the [Hub service](https://github.com/Digihelgeland-Sommercamp/hubService) and the Skattetat databese.
It is coupled with the following microservices:
* [Hub service](https://github.com/Digihelgeland-Sommercamp/hubService)


## API
Every route can be found in [app.py](https://github.com/Digihelgeland-Sommercamp/skatteservice/blob/main/app.py)   
Each route below links to the OpenAPI specification on swaggerhub.

* [GET] [/skattemeldinger](https://app.swaggerhub.com/apis/emilwhj/Skatteservice/0.1#/default/get_skattemeldinger)
* [GET] [/get_skattemelding/\<inntektsaar\>/\<personidentifikator\>](https://app.swaggerhub.com/apis/emilwhj/Skatteservice/0.1#/default/get_get_skattemelding__inntektsaar___personidentifikator_)

### Installation
This service is intended to run in a kubernetes cluster with the micro services it is coupled with, mentioned at the top of this document. It makes no sense for this service to run alone.
The intention is to only expose this service with a public IP, but this is not mandatory.

You can use the [deployment.yaml](https://github.com/Digihelgeland-Sommercamp/skatteservice/blob/main/deployment.yaml) to create a deployment in kubernetes, and [service.yaml](https://github.com/Digihelgeland-Sommercamp/skatteservice/blob/main/service.yaml) to create a service.



### Architecture
Visual representation of the microservices:
![Picture of the architecture and coupling of the services](https://github.com/Altinn/summer-camp-2021/blob/main/Documentation/Architecture/Microservice%20overview.png "Picture of the architecture and coupling of the services")