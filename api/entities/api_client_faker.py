import json

from api.entities.api_client_new import ApiClientNew
from typing import Dict, Any
import requests

from models.model_faker import Activities, Authors, Books, CoverBooks, Users


class ApiClientFaker(ApiClientNew):

    def __init__(self, url: str, timeout: float = None, ssl: bool = False):
        super(ApiClientFaker, self).__init__(url=f"{url}", timeout=timeout, ssl=ssl)

    def get_activities(self):
        return super()._get(
            endpoint='/api/v1/Activities',
            headers={'Content-Type': 'application/json'},
            expected_type=Activities,
            error_type=Activities
        )

    def post_activities(self, dto: Activities):
        return super()._post(
            endpoint='/api/v1/Activities',
            dto=dto,
            expected_type=Activities,
            error_type=Activities,
            headers={'Content-Type': 'application/json'},
        )

    def get_activities_id(self, id: int) -> Activities:
        return super()._get(
            endpoint=f'/api/v1/Activities/{id}',
            expected_type=Activities,
            error_type=Activities,
            headers={'Content-Type': 'application/json'},
        )

    def put_activities_id(self, dto: Activities, id: int):
        return super()._put(
            endpoint=f'/api/v1/Activities/{id}',
            dto=dto,
            expected_type=Activities,
            error_type=Activities,
            headers={'Content-Type': 'application/json'},
        )

    def delete_activities(self, id: int):
        return super()._delete(
            endpoint=f'/api/v1/Activities/{id}',
            headers={'Content-Type': 'application/json'},
        )

    def get_authors(self):
        return super()._get(
            endpoint='/api/v1/Authors',
            headers={'Content-Type': 'application/json'},
            expected_type=Authors,
            error_type=Authors
        )

    def post_authors(self, dto: Authors):
        return super()._post(
            endpoint='/api/v1/Authors',
            dto=dto,
            expected_type=Authors,
            error_type=Authors,
            headers={'Content-Type': 'application/json'}
        )
    def get_authors_book(self, id_book: int) -> Authors:
        return super()._get(
            endpoint=f'/api/v1/Authors/authors/books/{id_book}',
            expected_type=Authors,
            error_type=Authors,
            headers={'Content-Type': 'application/json'}
        )

    def get_authors_id(self, id: int) -> Authors:
        return super()._get(
            endpoint=f'/api/v1/Authors/{id}',
            expected_type=Authors,
            headers={'Content-Type': 'application/json'},
        )

    def put_authors(self, dto: Authors, id: int):
        return super()._put(
            endpoint=f'/api/v1/Authors/{id}',
            dto=dto,
            expected_type=Authors,
            error_type=Authors,
            headers={'Content-Type': 'application/json'},
        )

    def delete_authors(self, id: int):
        return super()._delete(
            endpoint=f'/api/v1/Authors/{id}',
            headers={'Content-Type': 'application/json'},
        )

    def get_books(self):
        return super()._get(
            endpoint='/api/v1/Books',
            headers={'Content-Type': 'application/json'}
        )

    def post_books(self, dto: Books):
        return super()._post(
            endpoint='/api/v1/Books',
            dto=dto,
            expected_type=Books,
            error_type=Books,
            headers={'Content-Type': 'application/json'}
        )

    def get_books_id(self, id: int):
        return super()._get(
            endpoint=f'/api/v1/Books/{id}',
            expected_type=Books,
            error_type=Books,
            headers={'Content-Type': 'application/json'}
    )

    def put_books(self, dto: Books):
        return super()._put(
            endpoint=f'/api/v1/Books/{id}',
            dto=dto,
            expected_type=Books,
            error_type=Books,
            headers={'Content-Type': 'application/json'}
        )

    def delete_books(self):
        return super()._delete(
            endpoint=f'/api/v1/Books/{id}',
            headers={'Content-Type': 'application/json'}
        )

    def get_cover_photos(self):
        return super()._get(
            endpoint='/api/v1/CoverPhotos',
            headers={'Content-Type': 'application/json'}
        )

    def post_cover_photos(self, dto: CoverBooks):
        return super()._post(
            endpoint='/api/v1/CoverPhotos',
            dto=dto,
            expected_type=CoverBooks,
            error_type=CoverBooks,
            headers={'Content-Type': 'application/json'}
        )

    def get_cover_photos_idbook(self, id_book: int) -> CoverBooks:
        return super()._get(
            endpoint=f'/api/v1/CoverPhotos/books/covers/{id_book}',
            expected_type=CoverBooks,
            error_type=CoverBooks,
            headers={'Content-Type': 'application/json'}
        )

    def get_cover_photos_id(self, id: int) -> CoverBooks:
        return super()._get(
            endpoint=f'/api/v1/CoverPhotos/{id}',
            expected_type=CoverBooks,
            error_type=CoverBooks,
            headers={'Content-Type': 'application/json'}
        )

    def put_cover_photos(self, id: int, dto: CoverBooks):
        return super()._put(
            endpoint=f'/api/v1/CoverPhotos/{id}',
            dto=dto,
            expected_type=CoverBooks,
            error_type=CoverBooks,
            headers={'Content-Type': 'application/json'}
        )

    def delete_cover_photos(self, id: int):
        return super()._delete(
            endpoint=f'/api/v1/CoverPhotos/{id}',
            headers={'Content-Type': 'application/json'}
        )

    def get_users(self):
        return super()._get(
            endpoint='/api/v1/Users',
            headers={'Content-Type': 'application/json'}
        )

    def post_users(self, dto: Users):
        return super()._post(
            endpoint='/api/v1/Users',
            dto=dto,
            expected_type=Users,
            error_type=Users,
            headers={'Content-Type': 'application/json'}
        )

    def get_users_id(self, id: int) -> Users:
        return super()._get(
            endpoint=f'/api/v1/Users/{id}',
            expected_type=Users,
            error_type=Users,
            headers={'Content-Type': 'application/json'}
        )

    def put_users_id(self, id: int, dto: Users):
        return super()._put(
            endpoint=f'/api/v1/Users/{id}',
            dto=dto,
            expected_type=Users,
            error_type=Users,
            headers={'Content-Type': 'application/json'}
        )

    def delete_users_id(self, id: int):
        return super()._delete(
            endpoint=f'/api/v1/Users/{id}',
            headers={'Content-Type': 'application/json'}
        )


