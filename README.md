# BookProject
BOOKSTORE PROJECT USING REST APIS


Admin/Superuser - can register, login, authenticate and perform all CRUD operations including search operations.
Normal Users - can login, authenticate and view list of books and perform search operations.

Using Class Based Views - viewsets.ModelViewSet

APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name)
Url - http://127.0.0.1:8000/bookstore/booklist/  (Complete List of Books)
Url - http://127.0.0.1:8000/book/<int:pk>/detail/ (Particular Book)
Response - status 200 ok

Request Method : POST
Url - http://127.0.0.1:8000/bookstore/bookcreate/
Body - {
    "author_name": [
        {
            "author_name": "APJ Abdul Kalam"
        }
    ],
    "title": "Ignited Minds",
    "publication_date": "2012-03-19"
}
Response - status 201 created


Request Method : PUT
Url - http://127.0.0.1:8000/book/<int:pk>/update/
Body - {
    "author_name": [
        {
            "author_name": "APJ Abdul Kalam"
        }
    ],
    "title": "Ignited Minds",
    "publication_date": "2021-03-19"
}
Response - status 200 ok


Request Method : PATCH
Url - http://127.0.0.1:8000/book/<int:pk>/update/
Body - {
    "title": "Ignited Minds 22",
    "publication_date": "2012-03-19"
}
Response - status 200 ok


Request Method : DELETE
Url - http://127.0.0.1:8000/book/<int:pk>/delete/
Response - status 204 no content

Additional Features - Searching list of books with search filters applied in GET method above that searches availability of books using author name or book name.
