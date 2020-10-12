# Django GraphQL API

    + GraphQL IDE to execute queries :
    -> https://graphql.org/swapi-graphql/

    + The API that will be used by the IDE (Starwar Movies):
    -> https://swapi.dev/

    + REST vs GRAPHQL :

    * Problem with REST endpoints is that, data getting from this endpoint is huge and sometimes we don't need all the attributes
      so this is why GRAPHQL came to fix this problem of over-fetching with it's query language and request just the data needed,
      trying to minimize data loading and providing a flexibility that doesn't exist in REST concept.

    #Example :

    - Run this REST query to get all films :
    -> https://swapi.dev/api/films/

    - Run this GRAPHQL query to get all films is producer :

    ->  {
          allFilms{
            films{
              producers
            }
          }
        }


