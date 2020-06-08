from aws_cdk import (
    core,
    aws_cloudwatch as cloudwatch
)


class CustomAlarmsConstruct(core.Construct):

    def __init__(self, scope: core.Construct, id: str, instance_id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        metric = cloudwatch.Metric(
            metric_name='CPUUtilization',
            namespace='AWS/EC2',
            dimensions={'InstanceId': instance_id}
        )

        alarm = cloudwatch.Alarm(
            self,
            id,
            metric=metric,
            threshold=85,
            evaluation_periods=2
        )
