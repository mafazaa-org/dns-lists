# v1-beta

-   transformed from json to sqlite db
-   all data now is stored in ${level}/data.db
-   blocklist is the list of block domains as before
-   blockregex is a list of keywords with the column 'is_subdomain' to differenciate between the two types
-   zoneslist is list of zone hosts with ids
-   answers is a list of answers with a foreign key for it's host