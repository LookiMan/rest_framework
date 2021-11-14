# DJANGO || rest_framework

<br />
<br />
<br />

# Test posts api

<br />

# 1. Create new post

Method: `POST`

URL: `http://127.0.0.1:8001/news_api/posts/create`

Params: `{ "title": "title1", "url": "https://github.com/1", "author": "Author1" }`

Response: `{ "id": 1, "title": "title1", "url": "https://github.com/1", "author": "Author1", "votes": 0, "created_at": "2021-11-14T14:40:42.233000Z" }`

# 2. Get post detail

Method: `GET`

URL: `http://127.0.0.1:8001/news_api/posts/detail/1`

Params: `None`

Response: `{ "id": 1, "title": "title1", "url": "https://github.com/1", "author": "Author1", "votes": 0, "created_at": "2021-11-14T09:47:56.041000Z" }`

<hr>

Method: `POST`

URL: `http://127.0.0.1:8001/news_api/posts/detail/1`

Params: `None`

Response: `{"detail": "Method \"POST\" not allowed."}`

# 3. Update post

Method: `PUT`

URL: `http://127.0.0.1:8001/news_api/posts/update/1`

Params: `{ "title": "title1", "url": "https://github.com/1", "author": "Author1", "votes": 1 }`

Response: `{ "id": 1, "title": "title1", "url": "https://github.com/1", "author": "Author", "votes": 1, "created_at": "2021-11-14T14:40:42.233000Z" }`

# 4. Delete post

Method: `GET`

URL: `http://127.0.0.1:8001/news_api/posts/delete/1`

Response: `{ "detail": "Method \"GET\" not allowed." }`

<hr>

Method: `DELETE`

URL: `http://127.0.0.1:8001/news_api/posts/delete/1`

Response: `Deleted post with id 1`

# 5. Vote for post

Method: `GET`

URL: `http://127.0.0.1:8001/news_api/posts/vote_for_post/1`

Response: `Succesfuly voted for post with id 1`

<br />
<br />
<br />

# Test Comments api

<br />

# 1. Create new comment

Method: `POST`

URL: `http://127.0.0.1:8001/news_api/comments/create`

Params: `{ "Post": 1, "author": "CommentAuthor1", "message": "New comment" }`

Response: `{ "id": 1, "author": "CommentAuthor1", "message": "New comment", "created_at": "2021-11-14T15:20:55.120000Z", "post": 1 }`

# 2. Get comment detail

Method: `GET`

URL: `http://127.0.0.1:8001/news_api/comments/detail/1`

Params: `None`

Response: `{ "id": 1, "author": "CommentAuthor1", "message": "New comment", "created_at": "2021-11-14T15:22:46.787000Z", "post": 1 }`

<hr>

Method: `POST`

URL: `http://127.0.0.1:8001/news_api/comments/detail/1`

Params: `None`

Response: `{"detail": "Method \"POST\" not allowed."}`

# 3. Update post

Method: `PUT`

URL: `http://127.0.0.1:8001/news_api/coments/update/1`

Params: `{ "post": 1, "author": "CommentAuthor1", "message": "Updated comment" }`

Response: `{ "id": 1, "author": "CommentAuthor1", "message": "Updated comment", "created_at": "2021-11-14T15:22:46.787000Z", "post": 1 }`

# 4. Delete comment

Method: `GET`

URL: `http://127.0.0.1:8001/news_api/comments/delete/1`

Response: `{ "detail": "Method \"GET\" not allowed." }`

<hr>

Method: `DELETE`

URL: `http://127.0.0.1:8001/news_api/comments/delete/1`

Response: `Deleted comment with id 1`
