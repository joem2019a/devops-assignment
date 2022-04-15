from utils.named_tuple import create_named_tuple

AssetRequestStatus = create_named_tuple(
    'AssetRequestStatus',
    
    'Initiated',
    'InProgress',
    'Complete',
    'Rejected',
)
