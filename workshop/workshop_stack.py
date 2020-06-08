from aws_cdk import (
    core,
    aws_ec2 as ec2
)

from workshop_alarm import CustomAlarmsConstruct


class WorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(
            self,
            'MyTestVpc',
            cidr='10.1.0.0/24'
        )

        instance = ec2.Instance(
            self,
            'MyTestInstance',
            machine_image=ec2.AmazonLinuxImage(),
            instance_type=ec2.InstanceType('t2.micro'),
            vpc=vpc)

        alarm = CustomAlarmsConstruct(
            self,
            'MyTestAlarm',
            instance_id=instance.instance_id
        )
