import json

def get_sagemaker_notebook_instance_creation_role():
    role_policy_document = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "sagemaker:*",
                        "ecr:GetAuthorizationToken",
                        "ecr:GetDownloadUrlForLayer",
                        "ecr:BatchGetImage",
                        "ecr:BatchCheckLayerAvailability",
                        "ecr:SetRepositoryPolicy",
                        "ecr:CompleteLayerUpload",
                        "ecr:BatchDeleteImage",
                        "ecr:UploadLayerPart",
                        "ecr:DeleteRepositoryPolicy",
                        "ecr:InitiateLayerUpload",
                        "ecr:DeleteRepository",
                        "ecr:PutImage",
                        "ecr:CreateRepository",
                        "cloudwatch:PutMetricData",
                        "cloudwatch:GetMetricData",
                        "cloudwatch:GetMetricStatistics",
                        "cloudwatch:ListMetrics",
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:DescribeLogStreams",
                        "logs:PutLogEvents",
                        "logs:GetLogEvents",
                        "s3:CreateBucket",
                        "s3:ListBucket",
                        "s3:GetBucketLocation",
                        "s3:GetObject",
                        "s3:PutObject",
                        "s3:DeleteObject",
                        "robomaker:CreateSimulationApplication",
                        "robomaker:DescribeSimulationApplication",
                        "robomaker:DeleteSimulationApplication",
                        "robomaker:CreateSimulationJob",
                        "robomaker:DescribeSimulationJob",
                        "robomaker:CancelSimulationJob",
                        "ec2:CreateVpcEndpoint",
                        "ec2:DescribeRouteTables",
                        "elasticfilesystem:DescribeMountTargets"
                    ],
                    "Resource": "*"
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "codecommit:GitPull",
                        "codecommit:GitPush"
                    ],
                    "Resource": [
                        "arn:aws:codecommit:*:*:*sagemaker*",
                        "arn:aws:codecommit:*:*:*SageMaker*",
                        "arn:aws:codecommit:*:*:*Sagemaker*"
                    ]
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "iam:PassRole"
                    ],
                    "Resource": "*",
                    "Condition": {
                        "StringEquals": {
                            "iam:PassedToService": "sagemaker.amazonaws.com"
                        }
                    }
                }
            ]
        }
    )

    return role_policy_document