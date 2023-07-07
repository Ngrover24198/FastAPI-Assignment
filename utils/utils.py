from datetime import datetime, timedelta

from models.db_models import Assignment
from schema.response_schema import GetDataResponse


def get_add_details(details):
    user = Assignment()
    user.source_id = details.source_id,
    user.source = details.source,
    user.source_type = details.source_type,
    user.source_tag = details.source_tag,
    user.last_updated_date = details.last_updated_date,
    user.from_date = details.from_date,
    user.to_date = details.to_date,
    user.frequency = details.frequency
    
    return user


def get_data_response(details):
    response = None
    if details:
        response = GetDataResponse(
                source_id = details.source_id,
                source = details.source,
                source_type = details.source_type,
                source_tag = details.source_tag,
                last_updated_date = details.last_updated_date,
                from_date = details.from_date,
                to_date = details.to_date,
                frequency = details.frequency
                )
    
    return response


def get_trigger_data_response(response):
    freq = response.frequency
    freq = int(freq[:-1])
    
    response.from_date = response.from_date + timedelta(minutes=freq)
    response.to_date = response.to_date + timedelta(minutes=freq)

    return response


def update_details(assignment, user):
    assignment.last_updated_date = user.last_updated_date
    assignment.from_date = user.from_date
    assignment.to_date = user.to_date
    
    