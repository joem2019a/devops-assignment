from api.utils.named_tuple import create_named_tuple

AssetRequestStatus = create_named_tuple(
    'Initiated',
    'InProgress',
    'Completed',
    'Rejected',
)
