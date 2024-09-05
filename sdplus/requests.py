'Script for Requests API'

from dataclasses import dataclass, asdict
import requests


@dataclass
class Request: #pylint: disable=too-many-instance-attributes
    '''
    Class to represent a request to the ManageEngine ServiceDesk Plus API

    Mandatory fields:
        - subject: str
        - requester: dict
    '''
    id: str = None
    subject: str
    description: str = None
    short_description: str = None
    request_type: dict = None
    impact: dict = None
    impact_details: str = None
    status: dict = None
    mode: dict = None
    level: dict = None
    urgency: dict = None
    priority: dict = None
    service_category: dict = None
    requester: dict
    department: dict = None
    assets: list = None
    deleted_assets: list = None
    deleted_on: dict = None
    deleted_by: dict = None
    site: dict = None
    group: dict = None
    technician: dict = None
    category: dict = None
    subcategory: dict = None
    item: dict = None
    on_behalf_of: dict = None
    service_approvers: list = None
    sla: dict = None
    service_cost: float = None
    total_cost: float = None
    template: dict = None
    request_template_task_ids: list = None
    created_by: dict = None
    editor: dict = None
    email_ids_to_notify: list = None
    email_to: list = None
    email_cc: list = None
    update_reason: str = None
    status_change_comments: str = None
    time_elapsed: int = None
    approval_status: str = None
    notification_status: str = None
    linked_requests_count: int = None
    created_time: str = None
    due_by_time: str = None
    first_response_due_by_time: str = None
    completed_time: str = None
    resolved_time: str = None
    responded_time: str = None
    assigned_time: str = None
    last_updated_time: str = None
    has_request_initiated_change: bool = None
    has_request_caused_by_change: bool = None
    has_project: bool = None
    has_problem: bool = None
    has_purchase_orders: bool = None
    has_draft: bool = None
    is_reopened: bool = None
    has_dependency: bool = None
    is_fcr: bool = None
    has_linked_requests: bool = None
    has_attachments: bool = None
    has_notes: bool = None
    is_trashed: bool = None
    is_service_request: bool = None
    is_overdue: bool = None
    is_read: bool = None
    is_first_response_overdue: bool = None
    has_my_worklog_timer: bool = None
    is_editing_completed: bool = None
    attachments: list = None
    resources: dict = None
    udf_fields: dict = None
    resolution: dict = None
    closure_info: dict = None
    add_to_linked_requests: bool = None
    requester_ack_resolution: bool = None
    requester_ack_comments: str = None
    closure_comments: str = None
    onhold_scheduler: dict = None
    comments: str = None
    holded_by: dict = None
    change_to_status: dict = None
    linked_to_request: dict = None

    def to_dict(self):
        'Method to convert the request to a dictionary'
        return asdict(self)

@dataclass
class SearchCriteria:
    'Class to represent a search criteria object for the ManageEngine ServiceDesk Plus API'
    field: str
    value: str
    condition: str
    logical_operator: str = None

    def to_dict(self):
        'Method to convert the search criteria to a dictionary'
        return asdict(self)

@dataclass
class ListInfo:
    '''
    Class to represent a list info object for the ManageEngine ServiceDesk Plus API

    Search criteria is a list of SearchCriteria objects
    Filter by is a dictionary
        - The key is the name of the filter
    '''
    row_count: int
    start_index: int
    sort_field: str
    sort_order: str
    get_total_count: bool
    search_criteria: list[SearchCriteria]
    filter_by: dict

    def to_dict(self):
        'Method to convert the list info to a dictionary'
        self.search_criteria = [criteria.to_dict() for criteria in self.search_criteria]
        return asdict(self)

@dataclass
class ClosureInfo:
    'Class to represent a closure info object for the ManageEngine ServiceDesk Plus API'
    requester_ack_resolution: bool
    requester_ack_comments: str
    closure_comments: str
    closure_code: dict

    def to_dict(self):
        'Method to convert the closure info to a dictionary'
        return asdict(self)

@dataclass
class RequestSummary:
    'Class to represent a request summary object for the ManageEngine ServiceDesk Plus API'
    task_completed_count: int
    task_total_count: int
    dependency_count: int
    note_count: int
    link_request_count: int

    def to_dict(self):
        'Method to convert the request summary to a dictionary'
        return asdict(self)


class Requests:
    'Class to handle requests to the ManageEngine ServiceDesk Plus API'

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'authtoken': api_key
        }

    def __send_request(self, method, endpoint, data=None):
        'Method to send a request to the ServiceDesk Plus API'
        response = requests.request(
            method,
            f'{self.url}/api/v3/{endpoint}',
            headers=self.headers,
            json=data,
            timeout=10
        )
        return response.json()

    def __dict_to_request(self, data):
        'Method to convert a dictionary to a request object'
        return Request(**data)

    def add_request(self, request = Request) -> Request:
        'Method to add a request to the ServiceDesk Plus API'
        return_data = self.__send_request('POST', 'requests', request)
        return self.__dict_to_request(return_data)

    def update_request(self, request = Request) -> Request:
        'Method to update a request in the ServiceDesk Plus API'
        return_data = self.__send_request('PUT', f'requests/{request.id}', request)
        return self.__dict_to_request(return_data)

    def view_request(self, request_id = int) -> Request:
        'Method to view a request in the ServiceDesk Plus API'
        return_data = self.__send_request('GET', f'requests/{request_id}')
        return self.__dict_to_request(return_data)

    def view_all_requests(self, list_info = ListInfo) -> list[Request]:
        'Method to view all requests in the ServiceDesk Plus API'
        return_data = self.__send_request('GET', 'requests', list_info.to_dict())
        return [self.__dict_to_request(data) for data in return_data['data']]

    def view_all_request_filters(self) -> list[dict]:
        'Method to view all request filters in the ServiceDesk Plus API'
        return_data = self.__send_request('GET', 'list_view_filters/show_all')
        return return_data['data']

    def close_request(self, request_id, closure_info = ClosureInfo) -> Request:
        'Method to close a request in the ServiceDesk Plus API'
        return_data = self.__send_request('PUT', f'requests/{request_id}/close', closure_info)
        return self.__dict_to_request(return_data)

    def pickup_request(self, request_id) -> Request:
        'Method to pickup a request in the ServiceDesk Plus API'
        return_data = self.__send_request('PUT', f'requests/{request_id}/pickup')
        return self.__dict_to_request(return_data)

    def assign_request(self, request_id, group, technician) -> Request:
        'Method to assign a request in the ServiceDesk Plus API'
        data = {
            'request': {
                'group': group,
                'technician': technician
            }
        }
        return_data = self.__send_request('PUT', f'requests/{request_id}/assign', data)
        return self.__dict_to_request(return_data)

    def get_resolution(self, request_id) -> dict:
        'Method to get resolution of a request in the ServiceDesk Plus API'
        return_data = self.__send_request('GET', f'requests/{request_id}/resolutions')
        return return_data

    def add_resolution(self, request_id, resolution) -> dict:
        'Method to add resolution to a request in the ServiceDesk Plus API'
        data = {
            'resolution': {
                'content': resolution
            }
        }
        return_data = self.__send_request('POST', f'requests/{request_id}/resolutions', data)
        return return_data

    def merge_requests(self, request_id, merge_requests = list[int]) -> dict:
        '''
        Method to merge requests in the ServiceDesk Plus API

        merge_requests is a list of request IDs
        '''
        data = {
            'merge_requests': [
                {'id': str(merge_request)} for merge_request in merge_requests
            ]
        }
        return_data = self.__send_request('PUT', f'requests/{request_id}/merge_requests', data)
        return return_data

    def get_request_summary(self, request_id) -> RequestSummary:
        'Method to get request summary in the ServiceDesk Plus API'
        return_data = self.__send_request('GET', f'requests/{request_id}/summary')
        return RequestSummary(**return_data)
