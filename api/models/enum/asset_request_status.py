from utils.named_tuple import create_named_tuple

AssetRequestStatus = create_named_tuple(
    'asset_request_status',
    
    'Initiated',
    'InProgress',
    'Complete',
    'Rejected',
)
