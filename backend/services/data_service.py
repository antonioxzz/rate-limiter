from app.models.data import DataResponse

def get_protected_data_for_client(client_ip: str) -> DataResponse:
    return DataResponse(
        message="This is protected data.",
        client_ip=client_ip
    )
