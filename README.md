# REST-vs-GraphQL
A demonstration of the major difference between REST and GraphQL.
This demonstrates how GraphQL solves the problem of over and under-fetching in modern Web Development
and how it enables frontend and backend teams to function independently.

## Installation:

* Clone the repo

  ```
  git clone https://github.com/nakuldahiwade/REST-vs-GraphQL.git
  ```

* Create Virtual Environment.	

  ```
  virtualenv venv
  ```
  
* Install requirements.txt.	

  ```
  cd venv; pip install -r requirements.txt
  ```

All set to perform the demo.



## Perform the Demo:

The DB_Schema is very simple. There are three tables: Compute, Network and Volume(Storage).
Simple Infra/Cloud concept of a VM attached to Network and a Volume (Storage) attached to it.
Compute has network and volume as db_relationships. I am using SQLite.

* Start the REST api
  ```
  python api.py
  ```

* Start the GraphQL api
  ```
  python app_graphql.py
  ```
 
 * Simultaneously fetch the comupute (VM) object via both REST and GraphQL endpoints
  REST Endpoint
  ```
  localhost:5001/compute
  ```
  
  GraphQL Endpoint
  ```
  localhost:5000/graphql
  ```

* To fetch the Network and Volume objects via REST we'll have to hit the respective endpoints
  ```
  localhost:5001/network
  ```
  
  ```
  localhost:5001/volume
  ```
  
* However to fetch the attached network and volume within the API call (using the db_relationships)
  via GraphQL we simply need to change the fetching parameters in the graphiql client, without having
  to change anything in the backend.

* To perform the same fetching in REST (currently under-fetching), the backend team would have add this
  functionality in the compute API, and after making the change if the requirements change on the front-end,
  this would lead to over-fetching.

As the requirements change on the client side, there is a lot of back-and-forth between the backend
and frontend teams. GraphQL solves this problem by enabling the client to fetch the exact amount of data
as per the current requirement.
  


