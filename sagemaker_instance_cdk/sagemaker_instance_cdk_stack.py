from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sagemaker as sagemaker,
)

from sagemaker_instance_cdk.props_lib import get_sagemaker_notebook_instance_creation_role

class SagemakerInstanceCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # sagemakerInstanceCreationRole = iam.CfnRole(
        #     self, "NinjaTechAiAssessmentSagemakerExecutionRole",
        #     assume_role_policy_document=get_sagemaker_notebook_instance_creation_role()
        #     # managed_policy_arns=[
        #     #     "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
        #     # ]
        # )

        sagemakerNotebookInstance = sagemaker.CfnNotebookInstance(
            self, "SagemakeInstanceCdkNotebook",
            # instance_type='ml.g5.xlarge', # single GPU 16GB memory
            instance_type='ml.t2.medium',
            role_arn="arn:aws:iam::340019311433:role/AWSSagemakerExecutionRole"
        )
