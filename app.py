#!/usr/bin/env python3

import aws_cdk as cdk

from sagemaker_instance_cdk.sagemaker_instance_cdk_stack import SagemakerInstanceCdkStack


app = cdk.App()
SagemakerInstanceCdkStack(app, "sagemaker-instance-cdk")

app.synth()
