# + Django GraphQL API

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


### - Checking the type schema of data stored in the database (go to https://graphql.org/swapi-graphql/ and click on docs) :

![](./static/schema_explorer.png)

    + Query Starwar films using arguments :

        *go to the schema explorer, you will get all objects with there methods and arguments and types of return :

        - Example / to get a film by 'filmID' :

        -> film(id: IDfilmID: ID): Film

        {
          film(filmID: "1") {
            title
            episodeID
          }
        }


