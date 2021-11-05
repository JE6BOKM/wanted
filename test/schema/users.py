import pytest
from schema import Schema


@pytest.fixture
def user_detail_data():
    return {"id": str, "username": str, "email": str}


@pytest.fixture
def user_detail_schema(user_detail_data):
    schema = Schema(user_detail_data)
    return schema


@pytest.fixture
def login_resp_schema(user_detail_schema):
    # register 성공시 return 되는 데이터와 동일
    schema = Schema(
        {"user": user_detail_schema, "access_token": str, "refresh_token": str}
    )
    return schema
