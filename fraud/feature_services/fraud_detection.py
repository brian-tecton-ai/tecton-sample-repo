from tecton import FeatureService
from fraud.features.stream_window_aggregate_feature_views.user_transaction_amount_metrics import user_transaction_amount_metrics
from fraud.features.batch_window_aggregate_feature_views.user_transaction_counts import user_transaction_counts
from fraud.features.stream_feature_views.last_transaction_amount_sql import last_transaction_amount_sql
from fraud.features.on_demand_feature_views.transaction_amount_is_high import transaction_amount_is_high
from fraud.features.on_demand_feature_views.transaction_amount_is_higher_than_average import transaction_amount_is_higher_than_average
from fraud.features.feature_tables.user_login_counts import user_login_counts
from fraud.features.batch_feature_views.transaction_user_has_good_credit import transaction_user_has_good_credit
# from fraud.features.batch_feature_views.user_has_good_credit import user_has_good_credit


fraud_detection_feature_service = FeatureService(
    name='fraud_detection_feature_service',
    features=[
        last_transaction_amount_sql,
        transaction_amount_is_high,
        transaction_amount_is_higher_than_average,
        user_transaction_amount_metrics,
        user_transaction_counts,
        user_login_counts,
        transaction_user_has_good_credit
    ]
)

minimal_fs = FeatureService(
    name='minimal_fs',
    features=[
        transaction_amount_is_high
    ]
)

# fraud_detection_feature_service_v2 = FeatureService(
#     name='fraud_detection_feature_service:v2',
#     description='A FeatureService providing features for a model that predicts if a transaction is fraudulent.',
#     family='fraud',
#     tags={'release': 'production'},
#     features=[
#        user_has_good_credit, # New feature
#        transaction_amount_is_high,
#        transaction_amount_is_higher_than_average,
#        user_transaction_amount_metrics,
#        user_transaction_counts,
#        last_transaction_amount_sql
#     ]
# )
