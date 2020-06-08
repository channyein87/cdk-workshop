import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.core
import aws_cdk.cx_api
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-ssm", "1.15.0", __name__, "aws-ssm@1.15.0.jsii.tgz")
class CfnAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnAssociation"):
    """A CloudFormation ``AWS::SSM::Association``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::Association
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, association_name: typing.Optional[str]=None, document_version: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, output_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceAssociationOutputLocationProperty"]]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "ParameterValuesProperty"]]]]]=None, schedule_expression: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]=None) -> None:
        """Create a new ``AWS::SSM::Association``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param name: ``AWS::SSM::Association.Name``.
        :param association_name: ``AWS::SSM::Association.AssociationName``.
        :param document_version: ``AWS::SSM::Association.DocumentVersion``.
        :param instance_id: ``AWS::SSM::Association.InstanceId``.
        :param output_location: ``AWS::SSM::Association.OutputLocation``.
        :param parameters: ``AWS::SSM::Association.Parameters``.
        :param schedule_expression: ``AWS::SSM::Association.ScheduleExpression``.
        :param targets: ``AWS::SSM::Association.Targets``.
        """
        props = CfnAssociationProps(name=name, association_name=association_name, document_version=document_version, instance_id=instance_id, output_location=output_location, parameters=parameters, schedule_expression=schedule_expression, targets=targets)

        jsii.create(CfnAssociation, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::SSM::Association.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="associationName")
    def association_name(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.AssociationName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        """
        return jsii.get(self, "associationName")

    @association_name.setter
    def association_name(self, value: typing.Optional[str]):
        return jsii.set(self, "associationName", value)

    @property
    @jsii.member(jsii_name="documentVersion")
    def document_version(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.DocumentVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        """
        return jsii.get(self, "documentVersion")

    @document_version.setter
    def document_version(self, value: typing.Optional[str]):
        return jsii.set(self, "documentVersion", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="outputLocation")
    def output_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceAssociationOutputLocationProperty"]]]:
        """``AWS::SSM::Association.OutputLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        """
        return jsii.get(self, "outputLocation")

    @output_location.setter
    def output_location(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceAssociationOutputLocationProperty"]]]):
        return jsii.set(self, "outputLocation", value)

    @property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "ParameterValuesProperty"]]]]]:
        """``AWS::SSM::Association.Parameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        """
        return jsii.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "ParameterValuesProperty"]]]]]):
        return jsii.set(self, "parameters", value)

    @property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.ScheduleExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        """
        return jsii.get(self, "scheduleExpression")

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[str]):
        return jsii.set(self, "scheduleExpression", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]:
        """``AWS::SSM::Association.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]):
        return jsii.set(self, "targets", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnAssociation.InstanceAssociationOutputLocationProperty", jsii_struct_bases=[], name_mapping={'s3_location': 's3Location'})
    class InstanceAssociationOutputLocationProperty():
        def __init__(self, *, s3_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAssociation.S3OutputLocationProperty"]]]=None):
            """
            :param s3_location: ``CfnAssociation.InstanceAssociationOutputLocationProperty.S3Location``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html
            """
            self._values = {
            }
            if s3_location is not None: self._values["s3_location"] = s3_location

        @property
        def s3_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAssociation.S3OutputLocationProperty"]]]:
            """``CfnAssociation.InstanceAssociationOutputLocationProperty.S3Location``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html#cfn-ssm-association-instanceassociationoutputlocation-s3location
            """
            return self._values.get('s3_location')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceAssociationOutputLocationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnAssociation.ParameterValuesProperty", jsii_struct_bases=[], name_mapping={'parameter_values': 'parameterValues'})
    class ParameterValuesProperty():
        def __init__(self, *, parameter_values: typing.List[str]):
            """
            :param parameter_values: ``CfnAssociation.ParameterValuesProperty.ParameterValues``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html
            """
            self._values = {
                'parameter_values': parameter_values,
            }

        @property
        def parameter_values(self) -> typing.List[str]:
            """``CfnAssociation.ParameterValuesProperty.ParameterValues``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-parametervalues.html#cfn-ssm-association-parametervalues-parametervalues
            """
            return self._values.get('parameter_values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ParameterValuesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnAssociation.S3OutputLocationProperty", jsii_struct_bases=[], name_mapping={'output_s3_bucket_name': 'outputS3BucketName', 'output_s3_key_prefix': 'outputS3KeyPrefix'})
    class S3OutputLocationProperty():
        def __init__(self, *, output_s3_bucket_name: typing.Optional[str]=None, output_s3_key_prefix: typing.Optional[str]=None):
            """
            :param output_s3_bucket_name: ``CfnAssociation.S3OutputLocationProperty.OutputS3BucketName``.
            :param output_s3_key_prefix: ``CfnAssociation.S3OutputLocationProperty.OutputS3KeyPrefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html
            """
            self._values = {
            }
            if output_s3_bucket_name is not None: self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None: self._values["output_s3_key_prefix"] = output_s3_key_prefix

        @property
        def output_s3_bucket_name(self) -> typing.Optional[str]:
            """``CfnAssociation.S3OutputLocationProperty.OutputS3BucketName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3bucketname
            """
            return self._values.get('output_s3_bucket_name')

        @property
        def output_s3_key_prefix(self) -> typing.Optional[str]:
            """``CfnAssociation.S3OutputLocationProperty.OutputS3KeyPrefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html#cfn-ssm-association-s3outputlocation-outputs3keyprefix
            """
            return self._values.get('output_s3_key_prefix')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'S3OutputLocationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnAssociation.TargetProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'values': 'values'})
    class TargetProperty():
        def __init__(self, *, key: str, values: typing.List[str]):
            """
            :param key: ``CfnAssociation.TargetProperty.Key``.
            :param values: ``CfnAssociation.TargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html
            """
            self._values = {
                'key': key,
                'values': values,
            }

        @property
        def key(self) -> str:
            """``CfnAssociation.TargetProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-key
            """
            return self._values.get('key')

        @property
        def values(self) -> typing.List[str]:
            """``CfnAssociation.TargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-target.html#cfn-ssm-association-target-values
            """
            return self._values.get('values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnAssociationProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'association_name': 'associationName', 'document_version': 'documentVersion', 'instance_id': 'instanceId', 'output_location': 'outputLocation', 'parameters': 'parameters', 'schedule_expression': 'scheduleExpression', 'targets': 'targets'})
class CfnAssociationProps():
    def __init__(self, *, name: str, association_name: typing.Optional[str]=None, document_version: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, output_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAssociation.InstanceAssociationOutputLocationProperty"]]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "CfnAssociation.ParameterValuesProperty"]]]]]=None, schedule_expression: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssociation.TargetProperty"]]]]]=None):
        """Properties for defining a ``AWS::SSM::Association``.

        :param name: ``AWS::SSM::Association.Name``.
        :param association_name: ``AWS::SSM::Association.AssociationName``.
        :param document_version: ``AWS::SSM::Association.DocumentVersion``.
        :param instance_id: ``AWS::SSM::Association.InstanceId``.
        :param output_location: ``AWS::SSM::Association.OutputLocation``.
        :param parameters: ``AWS::SSM::Association.Parameters``.
        :param schedule_expression: ``AWS::SSM::Association.ScheduleExpression``.
        :param targets: ``AWS::SSM::Association.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html
        """
        self._values = {
            'name': name,
        }
        if association_name is not None: self._values["association_name"] = association_name
        if document_version is not None: self._values["document_version"] = document_version
        if instance_id is not None: self._values["instance_id"] = instance_id
        if output_location is not None: self._values["output_location"] = output_location
        if parameters is not None: self._values["parameters"] = parameters
        if schedule_expression is not None: self._values["schedule_expression"] = schedule_expression
        if targets is not None: self._values["targets"] = targets

    @property
    def name(self) -> str:
        """``AWS::SSM::Association.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-name
        """
        return self._values.get('name')

    @property
    def association_name(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.AssociationName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-associationname
        """
        return self._values.get('association_name')

    @property
    def document_version(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.DocumentVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-documentversion
        """
        return self._values.get('document_version')

    @property
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-instanceid
        """
        return self._values.get('instance_id')

    @property
    def output_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAssociation.InstanceAssociationOutputLocationProperty"]]]:
        """``AWS::SSM::Association.OutputLocation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-outputlocation
        """
        return self._values.get('output_location')

    @property
    def parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "CfnAssociation.ParameterValuesProperty"]]]]]:
        """``AWS::SSM::Association.Parameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-parameters
        """
        return self._values.get('parameters')

    @property
    def schedule_expression(self) -> typing.Optional[str]:
        """``AWS::SSM::Association.ScheduleExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-scheduleexpression
        """
        return self._values.get('schedule_expression')

    @property
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAssociation.TargetProperty"]]]]]:
        """``AWS::SSM::Association.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html#cfn-ssm-association-targets
        """
        return self._values.get('targets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnDocument(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnDocument"):
    """A CloudFormation ``AWS::SSM::Document``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::Document
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, content: typing.Any, document_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::SSM::Document``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param content: ``AWS::SSM::Document.Content``.
        :param document_type: ``AWS::SSM::Document.DocumentType``.
        :param tags: ``AWS::SSM::Document.Tags``.
        """
        props = CfnDocumentProps(content=content, document_type=document_type, tags=tags)

        jsii.create(CfnDocument, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SSM::Document.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        """``AWS::SSM::Document.Content``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        """
        return jsii.get(self, "content")

    @content.setter
    def content(self, value: typing.Any):
        return jsii.set(self, "content", value)

    @property
    @jsii.member(jsii_name="documentType")
    def document_type(self) -> typing.Optional[str]:
        """``AWS::SSM::Document.DocumentType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        """
        return jsii.get(self, "documentType")

    @document_type.setter
    def document_type(self, value: typing.Optional[str]):
        return jsii.set(self, "documentType", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnDocumentProps", jsii_struct_bases=[], name_mapping={'content': 'content', 'document_type': 'documentType', 'tags': 'tags'})
class CfnDocumentProps():
    def __init__(self, *, content: typing.Any, document_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::SSM::Document``.

        :param content: ``AWS::SSM::Document.Content``.
        :param document_type: ``AWS::SSM::Document.DocumentType``.
        :param tags: ``AWS::SSM::Document.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html
        """
        self._values = {
            'content': content,
        }
        if document_type is not None: self._values["document_type"] = document_type
        if tags is not None: self._values["tags"] = tags

    @property
    def content(self) -> typing.Any:
        """``AWS::SSM::Document.Content``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-content
        """
        return self._values.get('content')

    @property
    def document_type(self) -> typing.Optional[str]:
        """``AWS::SSM::Document.DocumentType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-documenttype
        """
        return self._values.get('document_type')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SSM::Document.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html#cfn-ssm-document-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDocumentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnMaintenanceWindow(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindow"):
    """A CloudFormation ``AWS::SSM::MaintenanceWindow``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::MaintenanceWindow
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, allow_unassociated_targets: typing.Union[bool, aws_cdk.core.IResolvable], cutoff: jsii.Number, duration: jsii.Number, name: str, schedule: str, description: typing.Optional[str]=None, end_date: typing.Optional[str]=None, schedule_timezone: typing.Optional[str]=None, start_date: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::SSM::MaintenanceWindow``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param allow_unassociated_targets: ``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.
        :param cutoff: ``AWS::SSM::MaintenanceWindow.Cutoff``.
        :param duration: ``AWS::SSM::MaintenanceWindow.Duration``.
        :param name: ``AWS::SSM::MaintenanceWindow.Name``.
        :param schedule: ``AWS::SSM::MaintenanceWindow.Schedule``.
        :param description: ``AWS::SSM::MaintenanceWindow.Description``.
        :param end_date: ``AWS::SSM::MaintenanceWindow.EndDate``.
        :param schedule_timezone: ``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.
        :param start_date: ``AWS::SSM::MaintenanceWindow.StartDate``.
        :param tags: ``AWS::SSM::MaintenanceWindow.Tags``.
        """
        props = CfnMaintenanceWindowProps(allow_unassociated_targets=allow_unassociated_targets, cutoff=cutoff, duration=duration, name=name, schedule=schedule, description=description, end_date=end_date, schedule_timezone=schedule_timezone, start_date=start_date, tags=tags)

        jsii.create(CfnMaintenanceWindow, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SSM::MaintenanceWindow.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="allowUnassociatedTargets")
    def allow_unassociated_targets(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        """
        return jsii.get(self, "allowUnassociatedTargets")

    @allow_unassociated_targets.setter
    def allow_unassociated_targets(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "allowUnassociatedTargets", value)

    @property
    @jsii.member(jsii_name="cutoff")
    def cutoff(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindow.Cutoff``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        """
        return jsii.get(self, "cutoff")

    @cutoff.setter
    def cutoff(self, value: jsii.Number):
        return jsii.set(self, "cutoff", value)

    @property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindow.Duration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        """
        return jsii.get(self, "duration")

    @duration.setter
    def duration(self, value: jsii.Number):
        return jsii.set(self, "duration", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::SSM::MaintenanceWindow.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> str:
        """``AWS::SSM::MaintenanceWindow.Schedule``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        """
        return jsii.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: str):
        return jsii.set(self, "schedule", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.EndDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        """
        return jsii.get(self, "endDate")

    @end_date.setter
    def end_date(self, value: typing.Optional[str]):
        return jsii.set(self, "endDate", value)

    @property
    @jsii.member(jsii_name="scheduleTimezone")
    def schedule_timezone(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        """
        return jsii.get(self, "scheduleTimezone")

    @schedule_timezone.setter
    def schedule_timezone(self, value: typing.Optional[str]):
        return jsii.set(self, "scheduleTimezone", value)

    @property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.StartDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        """
        return jsii.get(self, "startDate")

    @start_date.setter
    def start_date(self, value: typing.Optional[str]):
        return jsii.set(self, "startDate", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowProps", jsii_struct_bases=[], name_mapping={'allow_unassociated_targets': 'allowUnassociatedTargets', 'cutoff': 'cutoff', 'duration': 'duration', 'name': 'name', 'schedule': 'schedule', 'description': 'description', 'end_date': 'endDate', 'schedule_timezone': 'scheduleTimezone', 'start_date': 'startDate', 'tags': 'tags'})
class CfnMaintenanceWindowProps():
    def __init__(self, *, allow_unassociated_targets: typing.Union[bool, aws_cdk.core.IResolvable], cutoff: jsii.Number, duration: jsii.Number, name: str, schedule: str, description: typing.Optional[str]=None, end_date: typing.Optional[str]=None, schedule_timezone: typing.Optional[str]=None, start_date: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::SSM::MaintenanceWindow``.

        :param allow_unassociated_targets: ``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.
        :param cutoff: ``AWS::SSM::MaintenanceWindow.Cutoff``.
        :param duration: ``AWS::SSM::MaintenanceWindow.Duration``.
        :param name: ``AWS::SSM::MaintenanceWindow.Name``.
        :param schedule: ``AWS::SSM::MaintenanceWindow.Schedule``.
        :param description: ``AWS::SSM::MaintenanceWindow.Description``.
        :param end_date: ``AWS::SSM::MaintenanceWindow.EndDate``.
        :param schedule_timezone: ``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.
        :param start_date: ``AWS::SSM::MaintenanceWindow.StartDate``.
        :param tags: ``AWS::SSM::MaintenanceWindow.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html
        """
        self._values = {
            'allow_unassociated_targets': allow_unassociated_targets,
            'cutoff': cutoff,
            'duration': duration,
            'name': name,
            'schedule': schedule,
        }
        if description is not None: self._values["description"] = description
        if end_date is not None: self._values["end_date"] = end_date
        if schedule_timezone is not None: self._values["schedule_timezone"] = schedule_timezone
        if start_date is not None: self._values["start_date"] = start_date
        if tags is not None: self._values["tags"] = tags

    @property
    def allow_unassociated_targets(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::SSM::MaintenanceWindow.AllowUnassociatedTargets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-allowunassociatedtargets
        """
        return self._values.get('allow_unassociated_targets')

    @property
    def cutoff(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindow.Cutoff``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-cutoff
        """
        return self._values.get('cutoff')

    @property
    def duration(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindow.Duration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-duration
        """
        return self._values.get('duration')

    @property
    def name(self) -> str:
        """``AWS::SSM::MaintenanceWindow.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-name
        """
        return self._values.get('name')

    @property
    def schedule(self) -> str:
        """``AWS::SSM::MaintenanceWindow.Schedule``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-schedule
        """
        return self._values.get('schedule')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-description
        """
        return self._values.get('description')

    @property
    def end_date(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.EndDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-enddate
        """
        return self._values.get('end_date')

    @property
    def schedule_timezone(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.ScheduleTimezone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-scheduletimezone
        """
        return self._values.get('schedule_timezone')

    @property
    def start_date(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindow.StartDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-startdate
        """
        return self._values.get('start_date')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SSM::MaintenanceWindow.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html#cfn-ssm-maintenancewindow-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMaintenanceWindowProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnMaintenanceWindowTarget(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTarget"):
    """A CloudFormation ``AWS::SSM::MaintenanceWindowTarget``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::MaintenanceWindowTarget
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, resource_type: str, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetsProperty"]]], window_id: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, owner_information: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::SSM::MaintenanceWindowTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param resource_type: ``AWS::SSM::MaintenanceWindowTarget.ResourceType``.
        :param targets: ``AWS::SSM::MaintenanceWindowTarget.Targets``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTarget.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTarget.Description``.
        :param name: ``AWS::SSM::MaintenanceWindowTarget.Name``.
        :param owner_information: ``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.
        """
        props = CfnMaintenanceWindowTargetProps(resource_type=resource_type, targets=targets, window_id=window_id, description=description, name=name, owner_information=owner_information)

        jsii.create(CfnMaintenanceWindowTarget, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> str:
        """``AWS::SSM::MaintenanceWindowTarget.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        """
        return jsii.get(self, "resourceType")

    @resource_type.setter
    def resource_type(self, value: str):
        return jsii.set(self, "resourceType", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetsProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTarget.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetsProperty"]]]):
        return jsii.set(self, "targets", value)

    @property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> str:
        """``AWS::SSM::MaintenanceWindowTarget.WindowId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        """
        return jsii.get(self, "windowId")

    @window_id.setter
    def window_id(self, value: str):
        return jsii.set(self, "windowId", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="ownerInformation")
    def owner_information(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        """
        return jsii.get(self, "ownerInformation")

    @owner_information.setter
    def owner_information(self, value: typing.Optional[str]):
        return jsii.set(self, "ownerInformation", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTarget.TargetsProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'values': 'values'})
    class TargetsProperty():
        def __init__(self, *, key: str, values: typing.Optional[typing.List[str]]=None):
            """
            :param key: ``CfnMaintenanceWindowTarget.TargetsProperty.Key``.
            :param values: ``CfnMaintenanceWindowTarget.TargetsProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html
            """
            self._values = {
                'key': key,
            }
            if values is not None: self._values["values"] = values

        @property
        def key(self) -> str:
            """``CfnMaintenanceWindowTarget.TargetsProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-key
            """
            return self._values.get('key')

        @property
        def values(self) -> typing.Optional[typing.List[str]]:
            """``CfnMaintenanceWindowTarget.TargetsProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html#cfn-ssm-maintenancewindowtarget-targets-values
            """
            return self._values.get('values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTargetProps", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'targets': 'targets', 'window_id': 'windowId', 'description': 'description', 'name': 'name', 'owner_information': 'ownerInformation'})
class CfnMaintenanceWindowTargetProps():
    def __init__(self, *, resource_type: str, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMaintenanceWindowTarget.TargetsProperty"]]], window_id: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None, owner_information: typing.Optional[str]=None):
        """Properties for defining a ``AWS::SSM::MaintenanceWindowTarget``.

        :param resource_type: ``AWS::SSM::MaintenanceWindowTarget.ResourceType``.
        :param targets: ``AWS::SSM::MaintenanceWindowTarget.Targets``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTarget.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTarget.Description``.
        :param name: ``AWS::SSM::MaintenanceWindowTarget.Name``.
        :param owner_information: ``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html
        """
        self._values = {
            'resource_type': resource_type,
            'targets': targets,
            'window_id': window_id,
        }
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if owner_information is not None: self._values["owner_information"] = owner_information

    @property
    def resource_type(self) -> str:
        """``AWS::SSM::MaintenanceWindowTarget.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-resourcetype
        """
        return self._values.get('resource_type')

    @property
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMaintenanceWindowTarget.TargetsProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTarget.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-targets
        """
        return self._values.get('targets')

    @property
    def window_id(self) -> str:
        """``AWS::SSM::MaintenanceWindowTarget.WindowId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-windowid
        """
        return self._values.get('window_id')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-description
        """
        return self._values.get('description')

    @property
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-name
        """
        return self._values.get('name')

    @property
    def owner_information(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTarget.OwnerInformation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html#cfn-ssm-maintenancewindowtarget-ownerinformation
        """
        return self._values.get('owner_information')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMaintenanceWindowTargetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnMaintenanceWindowTask(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask"):
    """A CloudFormation ``AWS::SSM::MaintenanceWindowTask``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::MaintenanceWindowTask
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, max_concurrency: str, max_errors: str, priority: jsii.Number, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]], task_arn: str, task_type: str, window_id: str, description: typing.Optional[str]=None, logging_info: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoggingInfoProperty"]]]=None, name: typing.Optional[str]=None, service_role_arn: typing.Optional[str]=None, task_invocation_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TaskInvocationParametersProperty"]]]=None, task_parameters: typing.Any=None) -> None:
        """Create a new ``AWS::SSM::MaintenanceWindowTask``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param max_concurrency: ``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::MaintenanceWindowTask.MaxErrors``.
        :param priority: ``AWS::SSM::MaintenanceWindowTask.Priority``.
        :param targets: ``AWS::SSM::MaintenanceWindowTask.Targets``.
        :param task_arn: ``AWS::SSM::MaintenanceWindowTask.TaskArn``.
        :param task_type: ``AWS::SSM::MaintenanceWindowTask.TaskType``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTask.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTask.Description``.
        :param logging_info: ``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.
        :param name: ``AWS::SSM::MaintenanceWindowTask.Name``.
        :param service_role_arn: ``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.
        :param task_invocation_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.
        :param task_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskParameters``.
        """
        props = CfnMaintenanceWindowTaskProps(max_concurrency=max_concurrency, max_errors=max_errors, priority=priority, targets=targets, task_arn=task_arn, task_type=task_type, window_id=window_id, description=description, logging_info=logging_info, name=name, service_role_arn=service_role_arn, task_invocation_parameters=task_invocation_parameters, task_parameters=task_parameters)

        jsii.create(CfnMaintenanceWindowTask, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        """
        return jsii.get(self, "maxConcurrency")

    @max_concurrency.setter
    def max_concurrency(self, value: str):
        return jsii.set(self, "maxConcurrency", value)

    @property
    @jsii.member(jsii_name="maxErrors")
    def max_errors(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.MaxErrors``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        """
        return jsii.get(self, "maxErrors")

    @max_errors.setter
    def max_errors(self, value: str):
        return jsii.set(self, "maxErrors", value)

    @property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindowTask.Priority``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        """
        return jsii.get(self, "priority")

    @priority.setter
    def priority(self, value: jsii.Number):
        return jsii.set(self, "priority", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]):
        return jsii.set(self, "targets", value)

    @property
    @jsii.member(jsii_name="taskArn")
    def task_arn(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.TaskArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        """
        return jsii.get(self, "taskArn")

    @task_arn.setter
    def task_arn(self, value: str):
        return jsii.set(self, "taskArn", value)

    @property
    @jsii.member(jsii_name="taskParameters")
    def task_parameters(self) -> typing.Any:
        """``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        """
        return jsii.get(self, "taskParameters")

    @task_parameters.setter
    def task_parameters(self, value: typing.Any):
        return jsii.set(self, "taskParameters", value)

    @property
    @jsii.member(jsii_name="taskType")
    def task_type(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.TaskType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        """
        return jsii.get(self, "taskType")

    @task_type.setter
    def task_type(self, value: str):
        return jsii.set(self, "taskType", value)

    @property
    @jsii.member(jsii_name="windowId")
    def window_id(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.WindowId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        """
        return jsii.get(self, "windowId")

    @window_id.setter
    def window_id(self, value: str):
        return jsii.set(self, "windowId", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoggingInfoProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        """
        return jsii.get(self, "loggingInfo")

    @logging_info.setter
    def logging_info(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoggingInfoProperty"]]]):
        return jsii.set(self, "loggingInfo", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        """
        return jsii.get(self, "serviceRoleArn")

    @service_role_arn.setter
    def service_role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "serviceRoleArn", value)

    @property
    @jsii.member(jsii_name="taskInvocationParameters")
    def task_invocation_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TaskInvocationParametersProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        """
        return jsii.get(self, "taskInvocationParameters")

    @task_invocation_parameters.setter
    def task_invocation_parameters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TaskInvocationParametersProperty"]]]):
        return jsii.set(self, "taskInvocationParameters", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.LoggingInfoProperty", jsii_struct_bases=[], name_mapping={'region': 'region', 's3_bucket': 's3Bucket', 's3_prefix': 's3Prefix'})
    class LoggingInfoProperty():
        def __init__(self, *, region: str, s3_bucket: str, s3_prefix: typing.Optional[str]=None):
            """
            :param region: ``CfnMaintenanceWindowTask.LoggingInfoProperty.Region``.
            :param s3_bucket: ``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Bucket``.
            :param s3_prefix: ``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html
            """
            self._values = {
                'region': region,
                's3_bucket': s3_bucket,
            }
            if s3_prefix is not None: self._values["s3_prefix"] = s3_prefix

        @property
        def region(self) -> str:
            """``CfnMaintenanceWindowTask.LoggingInfoProperty.Region``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-region
            """
            return self._values.get('region')

        @property
        def s3_bucket(self) -> str:
            """``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3bucket
            """
            return self._values.get('s3_bucket')

        @property
        def s3_prefix(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.LoggingInfoProperty.S3Prefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html#cfn-ssm-maintenancewindowtask-logginginfo-s3prefix
            """
            return self._values.get('s3_prefix')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LoggingInfoProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty", jsii_struct_bases=[], name_mapping={'document_version': 'documentVersion', 'parameters': 'parameters'})
    class MaintenanceWindowAutomationParametersProperty():
        def __init__(self, *, document_version: typing.Optional[str]=None, parameters: typing.Any=None):
            """
            :param document_version: ``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.DocumentVersion``.
            :param parameters: ``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.Parameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html
            """
            self._values = {
            }
            if document_version is not None: self._values["document_version"] = document_version
            if parameters is not None: self._values["parameters"] = parameters

        @property
        def document_version(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.DocumentVersion``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-documentversion
            """
            return self._values.get('document_version')

        @property
        def parameters(self) -> typing.Any:
            """``CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty.Parameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowautomationparameters-parameters
            """
            return self._values.get('parameters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MaintenanceWindowAutomationParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty", jsii_struct_bases=[], name_mapping={'client_context': 'clientContext', 'payload': 'payload', 'qualifier': 'qualifier'})
    class MaintenanceWindowLambdaParametersProperty():
        def __init__(self, *, client_context: typing.Optional[str]=None, payload: typing.Optional[str]=None, qualifier: typing.Optional[str]=None):
            """
            :param client_context: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.ClientContext``.
            :param payload: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Payload``.
            :param qualifier: ``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Qualifier``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html
            """
            self._values = {
            }
            if client_context is not None: self._values["client_context"] = client_context
            if payload is not None: self._values["payload"] = payload
            if qualifier is not None: self._values["qualifier"] = qualifier

        @property
        def client_context(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.ClientContext``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-clientcontext
            """
            return self._values.get('client_context')

        @property
        def payload(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Payload``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-payload
            """
            return self._values.get('payload')

        @property
        def qualifier(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty.Qualifier``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowlambdaparameters-qualifier
            """
            return self._values.get('qualifier')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MaintenanceWindowLambdaParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty", jsii_struct_bases=[], name_mapping={'comment': 'comment', 'document_hash': 'documentHash', 'document_hash_type': 'documentHashType', 'notification_config': 'notificationConfig', 'output_s3_bucket_name': 'outputS3BucketName', 'output_s3_key_prefix': 'outputS3KeyPrefix', 'parameters': 'parameters', 'service_role_arn': 'serviceRoleArn', 'timeout_seconds': 'timeoutSeconds'})
    class MaintenanceWindowRunCommandParametersProperty():
        def __init__(self, *, comment: typing.Optional[str]=None, document_hash: typing.Optional[str]=None, document_hash_type: typing.Optional[str]=None, notification_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.NotificationConfigProperty"]]]=None, output_s3_bucket_name: typing.Optional[str]=None, output_s3_key_prefix: typing.Optional[str]=None, parameters: typing.Any=None, service_role_arn: typing.Optional[str]=None, timeout_seconds: typing.Optional[jsii.Number]=None):
            """
            :param comment: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Comment``.
            :param document_hash: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHash``.
            :param document_hash_type: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHashType``.
            :param notification_config: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.NotificationConfig``.
            :param output_s3_bucket_name: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3BucketName``.
            :param output_s3_key_prefix: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3KeyPrefix``.
            :param parameters: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Parameters``.
            :param service_role_arn: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.ServiceRoleArn``.
            :param timeout_seconds: ``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.TimeoutSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html
            """
            self._values = {
            }
            if comment is not None: self._values["comment"] = comment
            if document_hash is not None: self._values["document_hash"] = document_hash
            if document_hash_type is not None: self._values["document_hash_type"] = document_hash_type
            if notification_config is not None: self._values["notification_config"] = notification_config
            if output_s3_bucket_name is not None: self._values["output_s3_bucket_name"] = output_s3_bucket_name
            if output_s3_key_prefix is not None: self._values["output_s3_key_prefix"] = output_s3_key_prefix
            if parameters is not None: self._values["parameters"] = parameters
            if service_role_arn is not None: self._values["service_role_arn"] = service_role_arn
            if timeout_seconds is not None: self._values["timeout_seconds"] = timeout_seconds

        @property
        def comment(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Comment``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-comment
            """
            return self._values.get('comment')

        @property
        def document_hash(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHash``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthash
            """
            return self._values.get('document_hash')

        @property
        def document_hash_type(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.DocumentHashType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-documenthashtype
            """
            return self._values.get('document_hash_type')

        @property
        def notification_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.NotificationConfigProperty"]]]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.NotificationConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-notificationconfig
            """
            return self._values.get('notification_config')

        @property
        def output_s3_bucket_name(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3BucketName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3bucketname
            """
            return self._values.get('output_s3_bucket_name')

        @property
        def output_s3_key_prefix(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.OutputS3KeyPrefix``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-outputs3keyprefix
            """
            return self._values.get('output_s3_key_prefix')

        @property
        def parameters(self) -> typing.Any:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.Parameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-parameters
            """
            return self._values.get('parameters')

        @property
        def service_role_arn(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.ServiceRoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-servicerolearn
            """
            return self._values.get('service_role_arn')

        @property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty.TimeoutSeconds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowruncommandparameters-timeoutseconds
            """
            return self._values.get('timeout_seconds')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MaintenanceWindowRunCommandParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty", jsii_struct_bases=[], name_mapping={'input': 'input', 'name': 'name'})
    class MaintenanceWindowStepFunctionsParametersProperty():
        def __init__(self, *, input: typing.Optional[str]=None, name: typing.Optional[str]=None):
            """
            :param input: ``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Input``.
            :param name: ``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
            """
            self._values = {
            }
            if input is not None: self._values["input"] = input
            if name is not None: self._values["name"] = name

        @property
        def input(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Input``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input
            """
            return self._values.get('input')

        @property
        def name(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MaintenanceWindowStepFunctionsParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.NotificationConfigProperty", jsii_struct_bases=[], name_mapping={'notification_arn': 'notificationArn', 'notification_events': 'notificationEvents', 'notification_type': 'notificationType'})
    class NotificationConfigProperty():
        def __init__(self, *, notification_arn: str, notification_events: typing.Optional[typing.List[str]]=None, notification_type: typing.Optional[str]=None):
            """
            :param notification_arn: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationArn``.
            :param notification_events: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationEvents``.
            :param notification_type: ``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html
            """
            self._values = {
                'notification_arn': notification_arn,
            }
            if notification_events is not None: self._values["notification_events"] = notification_events
            if notification_type is not None: self._values["notification_type"] = notification_type

        @property
        def notification_arn(self) -> str:
            """``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationarn
            """
            return self._values.get('notification_arn')

        @property
        def notification_events(self) -> typing.Optional[typing.List[str]]:
            """``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationEvents``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationevents
            """
            return self._values.get('notification_events')

        @property
        def notification_type(self) -> typing.Optional[str]:
            """``CfnMaintenanceWindowTask.NotificationConfigProperty.NotificationType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html#cfn-ssm-maintenancewindowtask-notificationconfig-notificationtype
            """
            return self._values.get('notification_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NotificationConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.TargetProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'values': 'values'})
    class TargetProperty():
        def __init__(self, *, key: str, values: typing.Optional[typing.List[str]]=None):
            """
            :param key: ``CfnMaintenanceWindowTask.TargetProperty.Key``.
            :param values: ``CfnMaintenanceWindowTask.TargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html
            """
            self._values = {
                'key': key,
            }
            if values is not None: self._values["values"] = values

        @property
        def key(self) -> str:
            """``CfnMaintenanceWindowTask.TargetProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-key
            """
            return self._values.get('key')

        @property
        def values(self) -> typing.Optional[typing.List[str]]:
            """``CfnMaintenanceWindowTask.TargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-target.html#cfn-ssm-maintenancewindowtask-target-values
            """
            return self._values.get('values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTask.TaskInvocationParametersProperty", jsii_struct_bases=[], name_mapping={'maintenance_window_automation_parameters': 'maintenanceWindowAutomationParameters', 'maintenance_window_lambda_parameters': 'maintenanceWindowLambdaParameters', 'maintenance_window_run_command_parameters': 'maintenanceWindowRunCommandParameters', 'maintenance_window_step_functions_parameters': 'maintenanceWindowStepFunctionsParameters'})
    class TaskInvocationParametersProperty():
        def __init__(self, *, maintenance_window_automation_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty"]]]=None, maintenance_window_lambda_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty"]]]=None, maintenance_window_run_command_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty"]]]=None, maintenance_window_step_functions_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty"]]]=None):
            """
            :param maintenance_window_automation_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowAutomationParameters``.
            :param maintenance_window_lambda_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowLambdaParameters``.
            :param maintenance_window_run_command_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowRunCommandParameters``.
            :param maintenance_window_step_functions_parameters: ``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowStepFunctionsParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
            """
            self._values = {
            }
            if maintenance_window_automation_parameters is not None: self._values["maintenance_window_automation_parameters"] = maintenance_window_automation_parameters
            if maintenance_window_lambda_parameters is not None: self._values["maintenance_window_lambda_parameters"] = maintenance_window_lambda_parameters
            if maintenance_window_run_command_parameters is not None: self._values["maintenance_window_run_command_parameters"] = maintenance_window_run_command_parameters
            if maintenance_window_step_functions_parameters is not None: self._values["maintenance_window_step_functions_parameters"] = maintenance_window_step_functions_parameters

        @property
        def maintenance_window_automation_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowAutomationParametersProperty"]]]:
            """``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowAutomationParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters
            """
            return self._values.get('maintenance_window_automation_parameters')

        @property
        def maintenance_window_lambda_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowLambdaParametersProperty"]]]:
            """``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowLambdaParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters
            """
            return self._values.get('maintenance_window_lambda_parameters')

        @property
        def maintenance_window_run_command_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowRunCommandParametersProperty"]]]:
            """``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowRunCommandParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters
            """
            return self._values.get('maintenance_window_run_command_parameters')

        @property
        def maintenance_window_step_functions_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.MaintenanceWindowStepFunctionsParametersProperty"]]]:
            """``CfnMaintenanceWindowTask.TaskInvocationParametersProperty.MaintenanceWindowStepFunctionsParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters
            """
            return self._values.get('maintenance_window_step_functions_parameters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TaskInvocationParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnMaintenanceWindowTaskProps", jsii_struct_bases=[], name_mapping={'max_concurrency': 'maxConcurrency', 'max_errors': 'maxErrors', 'priority': 'priority', 'targets': 'targets', 'task_arn': 'taskArn', 'task_type': 'taskType', 'window_id': 'windowId', 'description': 'description', 'logging_info': 'loggingInfo', 'name': 'name', 'service_role_arn': 'serviceRoleArn', 'task_invocation_parameters': 'taskInvocationParameters', 'task_parameters': 'taskParameters'})
class CfnMaintenanceWindowTaskProps():
    def __init__(self, *, max_concurrency: str, max_errors: str, priority: jsii.Number, targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMaintenanceWindowTask.TargetProperty"]]], task_arn: str, task_type: str, window_id: str, description: typing.Optional[str]=None, logging_info: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.LoggingInfoProperty"]]]=None, name: typing.Optional[str]=None, service_role_arn: typing.Optional[str]=None, task_invocation_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.TaskInvocationParametersProperty"]]]=None, task_parameters: typing.Any=None):
        """Properties for defining a ``AWS::SSM::MaintenanceWindowTask``.

        :param max_concurrency: ``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.
        :param max_errors: ``AWS::SSM::MaintenanceWindowTask.MaxErrors``.
        :param priority: ``AWS::SSM::MaintenanceWindowTask.Priority``.
        :param targets: ``AWS::SSM::MaintenanceWindowTask.Targets``.
        :param task_arn: ``AWS::SSM::MaintenanceWindowTask.TaskArn``.
        :param task_type: ``AWS::SSM::MaintenanceWindowTask.TaskType``.
        :param window_id: ``AWS::SSM::MaintenanceWindowTask.WindowId``.
        :param description: ``AWS::SSM::MaintenanceWindowTask.Description``.
        :param logging_info: ``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.
        :param name: ``AWS::SSM::MaintenanceWindowTask.Name``.
        :param service_role_arn: ``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.
        :param task_invocation_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.
        :param task_parameters: ``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html
        """
        self._values = {
            'max_concurrency': max_concurrency,
            'max_errors': max_errors,
            'priority': priority,
            'targets': targets,
            'task_arn': task_arn,
            'task_type': task_type,
            'window_id': window_id,
        }
        if description is not None: self._values["description"] = description
        if logging_info is not None: self._values["logging_info"] = logging_info
        if name is not None: self._values["name"] = name
        if service_role_arn is not None: self._values["service_role_arn"] = service_role_arn
        if task_invocation_parameters is not None: self._values["task_invocation_parameters"] = task_invocation_parameters
        if task_parameters is not None: self._values["task_parameters"] = task_parameters

    @property
    def max_concurrency(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.MaxConcurrency``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxconcurrency
        """
        return self._values.get('max_concurrency')

    @property
    def max_errors(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.MaxErrors``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-maxerrors
        """
        return self._values.get('max_errors')

    @property
    def priority(self) -> jsii.Number:
        """``AWS::SSM::MaintenanceWindowTask.Priority``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-priority
        """
        return self._values.get('priority')

    @property
    def targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMaintenanceWindowTask.TargetProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-targets
        """
        return self._values.get('targets')

    @property
    def task_arn(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.TaskArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskarn
        """
        return self._values.get('task_arn')

    @property
    def task_type(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.TaskType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-tasktype
        """
        return self._values.get('task_type')

    @property
    def window_id(self) -> str:
        """``AWS::SSM::MaintenanceWindowTask.WindowId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-windowid
        """
        return self._values.get('window_id')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-description
        """
        return self._values.get('description')

    @property
    def logging_info(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.LoggingInfoProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.LoggingInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-logginginfo
        """
        return self._values.get('logging_info')

    @property
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-name
        """
        return self._values.get('name')

    @property
    def service_role_arn(self) -> typing.Optional[str]:
        """``AWS::SSM::MaintenanceWindowTask.ServiceRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-servicerolearn
        """
        return self._values.get('service_role_arn')

    @property
    def task_invocation_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnMaintenanceWindowTask.TaskInvocationParametersProperty"]]]:
        """``AWS::SSM::MaintenanceWindowTask.TaskInvocationParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskinvocationparameters
        """
        return self._values.get('task_invocation_parameters')

    @property
    def task_parameters(self) -> typing.Any:
        """``AWS::SSM::MaintenanceWindowTask.TaskParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html#cfn-ssm-maintenancewindowtask-taskparameters
        """
        return self._values.get('task_parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnMaintenanceWindowTaskProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnParameter(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnParameter"):
    """A CloudFormation ``AWS::SSM::Parameter``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::Parameter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, type: str, value: str, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, name: typing.Optional[str]=None, policies: typing.Optional[str]=None, tags: typing.Any=None, tier: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::SSM::Parameter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param type: ``AWS::SSM::Parameter.Type``.
        :param value: ``AWS::SSM::Parameter.Value``.
        :param allowed_pattern: ``AWS::SSM::Parameter.AllowedPattern``.
        :param description: ``AWS::SSM::Parameter.Description``.
        :param name: ``AWS::SSM::Parameter.Name``.
        :param policies: ``AWS::SSM::Parameter.Policies``.
        :param tags: ``AWS::SSM::Parameter.Tags``.
        :param tier: ``AWS::SSM::Parameter.Tier``.
        """
        props = CfnParameterProps(type=type, value=value, allowed_pattern=allowed_pattern, description=description, name=name, policies=policies, tags=tags, tier=tier)

        jsii.create(CfnParameter, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Type
        """
        return jsii.get(self, "attrType")

    @property
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Value
        """
        return jsii.get(self, "attrValue")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SSM::Parameter.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::SSM::Parameter.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        return jsii.set(self, "type", value)

    @property
    @jsii.member(jsii_name="value")
    def value(self) -> str:
        """``AWS::SSM::Parameter.Value``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        """
        return jsii.get(self, "value")

    @value.setter
    def value(self, value: str):
        return jsii.set(self, "value", value)

    @property
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.AllowedPattern``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        """
        return jsii.get(self, "allowedPattern")

    @allowed_pattern.setter
    def allowed_pattern(self, value: typing.Optional[str]):
        return jsii.set(self, "allowedPattern", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Policies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        """
        return jsii.get(self, "policies")

    @policies.setter
    def policies(self, value: typing.Optional[str]):
        return jsii.set(self, "policies", value)

    @property
    @jsii.member(jsii_name="tier")
    def tier(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Tier``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        """
        return jsii.get(self, "tier")

    @tier.setter
    def tier(self, value: typing.Optional[str]):
        return jsii.set(self, "tier", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnParameterProps", jsii_struct_bases=[], name_mapping={'type': 'type', 'value': 'value', 'allowed_pattern': 'allowedPattern', 'description': 'description', 'name': 'name', 'policies': 'policies', 'tags': 'tags', 'tier': 'tier'})
class CfnParameterProps():
    def __init__(self, *, type: str, value: str, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, name: typing.Optional[str]=None, policies: typing.Optional[str]=None, tags: typing.Any=None, tier: typing.Optional[str]=None):
        """Properties for defining a ``AWS::SSM::Parameter``.

        :param type: ``AWS::SSM::Parameter.Type``.
        :param value: ``AWS::SSM::Parameter.Value``.
        :param allowed_pattern: ``AWS::SSM::Parameter.AllowedPattern``.
        :param description: ``AWS::SSM::Parameter.Description``.
        :param name: ``AWS::SSM::Parameter.Name``.
        :param policies: ``AWS::SSM::Parameter.Policies``.
        :param tags: ``AWS::SSM::Parameter.Tags``.
        :param tier: ``AWS::SSM::Parameter.Tier``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html
        """
        self._values = {
            'type': type,
            'value': value,
        }
        if allowed_pattern is not None: self._values["allowed_pattern"] = allowed_pattern
        if description is not None: self._values["description"] = description
        if name is not None: self._values["name"] = name
        if policies is not None: self._values["policies"] = policies
        if tags is not None: self._values["tags"] = tags
        if tier is not None: self._values["tier"] = tier

    @property
    def type(self) -> str:
        """``AWS::SSM::Parameter.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-type
        """
        return self._values.get('type')

    @property
    def value(self) -> str:
        """``AWS::SSM::Parameter.Value``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-value
        """
        return self._values.get('value')

    @property
    def allowed_pattern(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.AllowedPattern``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-allowedpattern
        """
        return self._values.get('allowed_pattern')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-description
        """
        return self._values.get('description')

    @property
    def name(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-name
        """
        return self._values.get('name')

    @property
    def policies(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Policies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-policies
        """
        return self._values.get('policies')

    @property
    def tags(self) -> typing.Any:
        """``AWS::SSM::Parameter.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tags
        """
        return self._values.get('tags')

    @property
    def tier(self) -> typing.Optional[str]:
        """``AWS::SSM::Parameter.Tier``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html#cfn-ssm-parameter-tier
        """
        return self._values.get('tier')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnParameterProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnPatchBaseline(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline"):
    """A CloudFormation ``AWS::SSM::PatchBaseline``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::PatchBaseline
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, approval_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuleGroupProperty"]]]=None, approved_patches: typing.Optional[typing.List[str]]=None, approved_patches_compliance_level: typing.Optional[str]=None, approved_patches_enable_non_security: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None, global_filters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PatchFilterGroupProperty"]]]=None, operating_system: typing.Optional[str]=None, patch_groups: typing.Optional[typing.List[str]]=None, rejected_patches: typing.Optional[typing.List[str]]=None, rejected_patches_action: typing.Optional[str]=None, sources: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PatchSourceProperty"]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::SSM::PatchBaseline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param name: ``AWS::SSM::PatchBaseline.Name``.
        :param approval_rules: ``AWS::SSM::PatchBaseline.ApprovalRules``.
        :param approved_patches: ``AWS::SSM::PatchBaseline.ApprovedPatches``.
        :param approved_patches_compliance_level: ``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.
        :param approved_patches_enable_non_security: ``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.
        :param description: ``AWS::SSM::PatchBaseline.Description``.
        :param global_filters: ``AWS::SSM::PatchBaseline.GlobalFilters``.
        :param operating_system: ``AWS::SSM::PatchBaseline.OperatingSystem``.
        :param patch_groups: ``AWS::SSM::PatchBaseline.PatchGroups``.
        :param rejected_patches: ``AWS::SSM::PatchBaseline.RejectedPatches``.
        :param rejected_patches_action: ``AWS::SSM::PatchBaseline.RejectedPatchesAction``.
        :param sources: ``AWS::SSM::PatchBaseline.Sources``.
        :param tags: ``AWS::SSM::PatchBaseline.Tags``.
        """
        props = CfnPatchBaselineProps(name=name, approval_rules=approval_rules, approved_patches=approved_patches, approved_patches_compliance_level=approved_patches_compliance_level, approved_patches_enable_non_security=approved_patches_enable_non_security, description=description, global_filters=global_filters, operating_system=operating_system, patch_groups=patch_groups, rejected_patches=rejected_patches, rejected_patches_action=rejected_patches_action, sources=sources, tags=tags)

        jsii.create(CfnPatchBaseline, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::SSM::PatchBaseline.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::SSM::PatchBaseline.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="approvalRules")
    def approval_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuleGroupProperty"]]]:
        """``AWS::SSM::PatchBaseline.ApprovalRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        """
        return jsii.get(self, "approvalRules")

    @approval_rules.setter
    def approval_rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RuleGroupProperty"]]]):
        return jsii.set(self, "approvalRules", value)

    @property
    @jsii.member(jsii_name="approvedPatches")
    def approved_patches(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.ApprovedPatches``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        """
        return jsii.get(self, "approvedPatches")

    @approved_patches.setter
    def approved_patches(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "approvedPatches", value)

    @property
    @jsii.member(jsii_name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        """
        return jsii.get(self, "approvedPatchesComplianceLevel")

    @approved_patches_compliance_level.setter
    def approved_patches_compliance_level(self, value: typing.Optional[str]):
        return jsii.set(self, "approvedPatchesComplianceLevel", value)

    @property
    @jsii.member(jsii_name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        """
        return jsii.get(self, "approvedPatchesEnableNonSecurity")

    @approved_patches_enable_non_security.setter
    def approved_patches_enable_non_security(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "approvedPatchesEnableNonSecurity", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="globalFilters")
    def global_filters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PatchFilterGroupProperty"]]]:
        """``AWS::SSM::PatchBaseline.GlobalFilters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        """
        return jsii.get(self, "globalFilters")

    @global_filters.setter
    def global_filters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PatchFilterGroupProperty"]]]):
        return jsii.set(self, "globalFilters", value)

    @property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.OperatingSystem``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        """
        return jsii.get(self, "operatingSystem")

    @operating_system.setter
    def operating_system(self, value: typing.Optional[str]):
        return jsii.set(self, "operatingSystem", value)

    @property
    @jsii.member(jsii_name="patchGroups")
    def patch_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.PatchGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        """
        return jsii.get(self, "patchGroups")

    @patch_groups.setter
    def patch_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "patchGroups", value)

    @property
    @jsii.member(jsii_name="rejectedPatches")
    def rejected_patches(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.RejectedPatches``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        """
        return jsii.get(self, "rejectedPatches")

    @rejected_patches.setter
    def rejected_patches(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "rejectedPatches", value)

    @property
    @jsii.member(jsii_name="rejectedPatchesAction")
    def rejected_patches_action(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.RejectedPatchesAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        """
        return jsii.get(self, "rejectedPatchesAction")

    @rejected_patches_action.setter
    def rejected_patches_action(self, value: typing.Optional[str]):
        return jsii.set(self, "rejectedPatchesAction", value)

    @property
    @jsii.member(jsii_name="sources")
    def sources(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PatchSourceProperty"]]]]]:
        """``AWS::SSM::PatchBaseline.Sources``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        """
        return jsii.get(self, "sources")

    @sources.setter
    def sources(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PatchSourceProperty"]]]]]):
        return jsii.set(self, "sources", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline.PatchFilterGroupProperty", jsii_struct_bases=[], name_mapping={'patch_filters': 'patchFilters'})
    class PatchFilterGroupProperty():
        def __init__(self, *, patch_filters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.PatchFilterProperty"]]]]]=None):
            """
            :param patch_filters: ``CfnPatchBaseline.PatchFilterGroupProperty.PatchFilters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html
            """
            self._values = {
            }
            if patch_filters is not None: self._values["patch_filters"] = patch_filters

        @property
        def patch_filters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.PatchFilterProperty"]]]]]:
            """``CfnPatchBaseline.PatchFilterGroupProperty.PatchFilters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html#cfn-ssm-patchbaseline-patchfiltergroup-patchfilters
            """
            return self._values.get('patch_filters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PatchFilterGroupProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline.PatchFilterProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'values': 'values'})
    class PatchFilterProperty():
        def __init__(self, *, key: typing.Optional[str]=None, values: typing.Optional[typing.List[str]]=None):
            """
            :param key: ``CfnPatchBaseline.PatchFilterProperty.Key``.
            :param values: ``CfnPatchBaseline.PatchFilterProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html
            """
            self._values = {
            }
            if key is not None: self._values["key"] = key
            if values is not None: self._values["values"] = values

        @property
        def key(self) -> typing.Optional[str]:
            """``CfnPatchBaseline.PatchFilterProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-key
            """
            return self._values.get('key')

        @property
        def values(self) -> typing.Optional[typing.List[str]]:
            """``CfnPatchBaseline.PatchFilterProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html#cfn-ssm-patchbaseline-patchfilter-values
            """
            return self._values.get('values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PatchFilterProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline.PatchSourceProperty", jsii_struct_bases=[], name_mapping={'configuration': 'configuration', 'name': 'name', 'products': 'products'})
    class PatchSourceProperty():
        def __init__(self, *, configuration: typing.Optional[str]=None, name: typing.Optional[str]=None, products: typing.Optional[typing.List[str]]=None):
            """
            :param configuration: ``CfnPatchBaseline.PatchSourceProperty.Configuration``.
            :param name: ``CfnPatchBaseline.PatchSourceProperty.Name``.
            :param products: ``CfnPatchBaseline.PatchSourceProperty.Products``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html
            """
            self._values = {
            }
            if configuration is not None: self._values["configuration"] = configuration
            if name is not None: self._values["name"] = name
            if products is not None: self._values["products"] = products

        @property
        def configuration(self) -> typing.Optional[str]:
            """``CfnPatchBaseline.PatchSourceProperty.Configuration``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-configuration
            """
            return self._values.get('configuration')

        @property
        def name(self) -> typing.Optional[str]:
            """``CfnPatchBaseline.PatchSourceProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-name
            """
            return self._values.get('name')

        @property
        def products(self) -> typing.Optional[typing.List[str]]:
            """``CfnPatchBaseline.PatchSourceProperty.Products``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html#cfn-ssm-patchbaseline-patchsource-products
            """
            return self._values.get('products')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PatchSourceProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline.RuleGroupProperty", jsii_struct_bases=[], name_mapping={'patch_rules': 'patchRules'})
    class RuleGroupProperty():
        def __init__(self, *, patch_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.RuleProperty"]]]]]=None):
            """
            :param patch_rules: ``CfnPatchBaseline.RuleGroupProperty.PatchRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html
            """
            self._values = {
            }
            if patch_rules is not None: self._values["patch_rules"] = patch_rules

        @property
        def patch_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.RuleProperty"]]]]]:
            """``CfnPatchBaseline.RuleGroupProperty.PatchRules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html#cfn-ssm-patchbaseline-rulegroup-patchrules
            """
            return self._values.get('patch_rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleGroupProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaseline.RuleProperty", jsii_struct_bases=[], name_mapping={'approve_after_days': 'approveAfterDays', 'compliance_level': 'complianceLevel', 'enable_non_security': 'enableNonSecurity', 'patch_filter_group': 'patchFilterGroup'})
    class RuleProperty():
        def __init__(self, *, approve_after_days: typing.Optional[jsii.Number]=None, compliance_level: typing.Optional[str]=None, enable_non_security: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, patch_filter_group: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.PatchFilterGroupProperty"]]]=None):
            """
            :param approve_after_days: ``CfnPatchBaseline.RuleProperty.ApproveAfterDays``.
            :param compliance_level: ``CfnPatchBaseline.RuleProperty.ComplianceLevel``.
            :param enable_non_security: ``CfnPatchBaseline.RuleProperty.EnableNonSecurity``.
            :param patch_filter_group: ``CfnPatchBaseline.RuleProperty.PatchFilterGroup``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html
            """
            self._values = {
            }
            if approve_after_days is not None: self._values["approve_after_days"] = approve_after_days
            if compliance_level is not None: self._values["compliance_level"] = compliance_level
            if enable_non_security is not None: self._values["enable_non_security"] = enable_non_security
            if patch_filter_group is not None: self._values["patch_filter_group"] = patch_filter_group

        @property
        def approve_after_days(self) -> typing.Optional[jsii.Number]:
            """``CfnPatchBaseline.RuleProperty.ApproveAfterDays``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-approveafterdays
            """
            return self._values.get('approve_after_days')

        @property
        def compliance_level(self) -> typing.Optional[str]:
            """``CfnPatchBaseline.RuleProperty.ComplianceLevel``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-compliancelevel
            """
            return self._values.get('compliance_level')

        @property
        def enable_non_security(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnPatchBaseline.RuleProperty.EnableNonSecurity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-enablenonsecurity
            """
            return self._values.get('enable_non_security')

        @property
        def patch_filter_group(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.PatchFilterGroupProperty"]]]:
            """``CfnPatchBaseline.RuleProperty.PatchFilterGroup``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html#cfn-ssm-patchbaseline-rule-patchfiltergroup
            """
            return self._values.get('patch_filter_group')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnPatchBaselineProps", jsii_struct_bases=[], name_mapping={'name': 'name', 'approval_rules': 'approvalRules', 'approved_patches': 'approvedPatches', 'approved_patches_compliance_level': 'approvedPatchesComplianceLevel', 'approved_patches_enable_non_security': 'approvedPatchesEnableNonSecurity', 'description': 'description', 'global_filters': 'globalFilters', 'operating_system': 'operatingSystem', 'patch_groups': 'patchGroups', 'rejected_patches': 'rejectedPatches', 'rejected_patches_action': 'rejectedPatchesAction', 'sources': 'sources', 'tags': 'tags'})
class CfnPatchBaselineProps():
    def __init__(self, *, name: str, approval_rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.RuleGroupProperty"]]]=None, approved_patches: typing.Optional[typing.List[str]]=None, approved_patches_compliance_level: typing.Optional[str]=None, approved_patches_enable_non_security: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None, global_filters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.PatchFilterGroupProperty"]]]=None, operating_system: typing.Optional[str]=None, patch_groups: typing.Optional[typing.List[str]]=None, rejected_patches: typing.Optional[typing.List[str]]=None, rejected_patches_action: typing.Optional[str]=None, sources: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.PatchSourceProperty"]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::SSM::PatchBaseline``.

        :param name: ``AWS::SSM::PatchBaseline.Name``.
        :param approval_rules: ``AWS::SSM::PatchBaseline.ApprovalRules``.
        :param approved_patches: ``AWS::SSM::PatchBaseline.ApprovedPatches``.
        :param approved_patches_compliance_level: ``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.
        :param approved_patches_enable_non_security: ``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.
        :param description: ``AWS::SSM::PatchBaseline.Description``.
        :param global_filters: ``AWS::SSM::PatchBaseline.GlobalFilters``.
        :param operating_system: ``AWS::SSM::PatchBaseline.OperatingSystem``.
        :param patch_groups: ``AWS::SSM::PatchBaseline.PatchGroups``.
        :param rejected_patches: ``AWS::SSM::PatchBaseline.RejectedPatches``.
        :param rejected_patches_action: ``AWS::SSM::PatchBaseline.RejectedPatchesAction``.
        :param sources: ``AWS::SSM::PatchBaseline.Sources``.
        :param tags: ``AWS::SSM::PatchBaseline.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html
        """
        self._values = {
            'name': name,
        }
        if approval_rules is not None: self._values["approval_rules"] = approval_rules
        if approved_patches is not None: self._values["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None: self._values["approved_patches_compliance_level"] = approved_patches_compliance_level
        if approved_patches_enable_non_security is not None: self._values["approved_patches_enable_non_security"] = approved_patches_enable_non_security
        if description is not None: self._values["description"] = description
        if global_filters is not None: self._values["global_filters"] = global_filters
        if operating_system is not None: self._values["operating_system"] = operating_system
        if patch_groups is not None: self._values["patch_groups"] = patch_groups
        if rejected_patches is not None: self._values["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None: self._values["rejected_patches_action"] = rejected_patches_action
        if sources is not None: self._values["sources"] = sources
        if tags is not None: self._values["tags"] = tags

    @property
    def name(self) -> str:
        """``AWS::SSM::PatchBaseline.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-name
        """
        return self._values.get('name')

    @property
    def approval_rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.RuleGroupProperty"]]]:
        """``AWS::SSM::PatchBaseline.ApprovalRules``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvalrules
        """
        return self._values.get('approval_rules')

    @property
    def approved_patches(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.ApprovedPatches``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatches
        """
        return self._values.get('approved_patches')

    @property
    def approved_patches_compliance_level(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.ApprovedPatchesComplianceLevel``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchescompliancelevel
        """
        return self._values.get('approved_patches_compliance_level')

    @property
    def approved_patches_enable_non_security(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::SSM::PatchBaseline.ApprovedPatchesEnableNonSecurity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity
        """
        return self._values.get('approved_patches_enable_non_security')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-description
        """
        return self._values.get('description')

    @property
    def global_filters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnPatchBaseline.PatchFilterGroupProperty"]]]:
        """``AWS::SSM::PatchBaseline.GlobalFilters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-globalfilters
        """
        return self._values.get('global_filters')

    @property
    def operating_system(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.OperatingSystem``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-operatingsystem
        """
        return self._values.get('operating_system')

    @property
    def patch_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.PatchGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-patchgroups
        """
        return self._values.get('patch_groups')

    @property
    def rejected_patches(self) -> typing.Optional[typing.List[str]]:
        """``AWS::SSM::PatchBaseline.RejectedPatches``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatches
        """
        return self._values.get('rejected_patches')

    @property
    def rejected_patches_action(self) -> typing.Optional[str]:
        """``AWS::SSM::PatchBaseline.RejectedPatchesAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-rejectedpatchesaction
        """
        return self._values.get('rejected_patches_action')

    @property
    def sources(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPatchBaseline.PatchSourceProperty"]]]]]:
        """``AWS::SSM::PatchBaseline.Sources``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-sources
        """
        return self._values.get('sources')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::SSM::PatchBaseline.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html#cfn-ssm-patchbaseline-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnPatchBaselineProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnResourceDataSync(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.CfnResourceDataSync"):
    """A CloudFormation ``AWS::SSM::ResourceDataSync``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
    cloudformationResource:
    :cloudformationResource:: AWS::SSM::ResourceDataSync
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, bucket_name: str, bucket_region: str, sync_format: str, sync_name: str, bucket_prefix: typing.Optional[str]=None, kms_key_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::SSM::ResourceDataSync``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param bucket_name: ``AWS::SSM::ResourceDataSync.BucketName``.
        :param bucket_region: ``AWS::SSM::ResourceDataSync.BucketRegion``.
        :param sync_format: ``AWS::SSM::ResourceDataSync.SyncFormat``.
        :param sync_name: ``AWS::SSM::ResourceDataSync.SyncName``.
        :param bucket_prefix: ``AWS::SSM::ResourceDataSync.BucketPrefix``.
        :param kms_key_arn: ``AWS::SSM::ResourceDataSync.KMSKeyArn``.
        """
        props = CfnResourceDataSyncProps(bucket_name=bucket_name, bucket_region=bucket_region, sync_format=sync_format, sync_name=sync_name, bucket_prefix=bucket_prefix, kms_key_arn=kms_key_arn)

        jsii.create(CfnResourceDataSync, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> str:
        """``AWS::SSM::ResourceDataSync.BucketName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        """
        return jsii.get(self, "bucketName")

    @bucket_name.setter
    def bucket_name(self, value: str):
        return jsii.set(self, "bucketName", value)

    @property
    @jsii.member(jsii_name="bucketRegion")
    def bucket_region(self) -> str:
        """``AWS::SSM::ResourceDataSync.BucketRegion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        """
        return jsii.get(self, "bucketRegion")

    @bucket_region.setter
    def bucket_region(self, value: str):
        return jsii.set(self, "bucketRegion", value)

    @property
    @jsii.member(jsii_name="syncFormat")
    def sync_format(self) -> str:
        """``AWS::SSM::ResourceDataSync.SyncFormat``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        """
        return jsii.get(self, "syncFormat")

    @sync_format.setter
    def sync_format(self, value: str):
        return jsii.set(self, "syncFormat", value)

    @property
    @jsii.member(jsii_name="syncName")
    def sync_name(self) -> str:
        """``AWS::SSM::ResourceDataSync.SyncName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        """
        return jsii.get(self, "syncName")

    @sync_name.setter
    def sync_name(self, value: str):
        return jsii.set(self, "syncName", value)

    @property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> typing.Optional[str]:
        """``AWS::SSM::ResourceDataSync.BucketPrefix``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        """
        return jsii.get(self, "bucketPrefix")

    @bucket_prefix.setter
    def bucket_prefix(self, value: typing.Optional[str]):
        return jsii.set(self, "bucketPrefix", value)

    @property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[str]:
        """``AWS::SSM::ResourceDataSync.KMSKeyArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        """
        return jsii.get(self, "kmsKeyArn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "kmsKeyArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.CfnResourceDataSyncProps", jsii_struct_bases=[], name_mapping={'bucket_name': 'bucketName', 'bucket_region': 'bucketRegion', 'sync_format': 'syncFormat', 'sync_name': 'syncName', 'bucket_prefix': 'bucketPrefix', 'kms_key_arn': 'kmsKeyArn'})
class CfnResourceDataSyncProps():
    def __init__(self, *, bucket_name: str, bucket_region: str, sync_format: str, sync_name: str, bucket_prefix: typing.Optional[str]=None, kms_key_arn: typing.Optional[str]=None):
        """Properties for defining a ``AWS::SSM::ResourceDataSync``.

        :param bucket_name: ``AWS::SSM::ResourceDataSync.BucketName``.
        :param bucket_region: ``AWS::SSM::ResourceDataSync.BucketRegion``.
        :param sync_format: ``AWS::SSM::ResourceDataSync.SyncFormat``.
        :param sync_name: ``AWS::SSM::ResourceDataSync.SyncName``.
        :param bucket_prefix: ``AWS::SSM::ResourceDataSync.BucketPrefix``.
        :param kms_key_arn: ``AWS::SSM::ResourceDataSync.KMSKeyArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html
        """
        self._values = {
            'bucket_name': bucket_name,
            'bucket_region': bucket_region,
            'sync_format': sync_format,
            'sync_name': sync_name,
        }
        if bucket_prefix is not None: self._values["bucket_prefix"] = bucket_prefix
        if kms_key_arn is not None: self._values["kms_key_arn"] = kms_key_arn

    @property
    def bucket_name(self) -> str:
        """``AWS::SSM::ResourceDataSync.BucketName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketname
        """
        return self._values.get('bucket_name')

    @property
    def bucket_region(self) -> str:
        """``AWS::SSM::ResourceDataSync.BucketRegion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketregion
        """
        return self._values.get('bucket_region')

    @property
    def sync_format(self) -> str:
        """``AWS::SSM::ResourceDataSync.SyncFormat``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncformat
        """
        return self._values.get('sync_format')

    @property
    def sync_name(self) -> str:
        """``AWS::SSM::ResourceDataSync.SyncName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-syncname
        """
        return self._values.get('sync_name')

    @property
    def bucket_prefix(self) -> typing.Optional[str]:
        """``AWS::SSM::ResourceDataSync.BucketPrefix``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-bucketprefix
        """
        return self._values.get('bucket_prefix')

    @property
    def kms_key_arn(self) -> typing.Optional[str]:
        """``AWS::SSM::ResourceDataSync.KMSKeyArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html#cfn-ssm-resourcedatasync-kmskeyarn
        """
        return self._values.get('kms_key_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnResourceDataSyncProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-ssm.IParameter")
class IParameter(aws_cdk.core.IResource, jsii.compat.Protocol):
    """An SSM Parameter reference."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IParameterProxy

    @property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> str:
        """The ARN of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> str:
        """The name of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> str:
        """The type of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        """
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        """
        ...


class _IParameterProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """An SSM Parameter reference."""
    __jsii_type__ = "@aws-cdk/aws-ssm.IParameter"
    @property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> str:
        """The ARN of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "parameterArn")

    @property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> str:
        """The name of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "parameterName")

    @property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> str:
        """The type of the SSM Parameter resource.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "parameterType")

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: the role to be granted read-only access to the parameter.
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: the role to be granted write access to the parameter.
        """
        return jsii.invoke(self, "grantWrite", [grantee])


@jsii.interface(jsii_type="@aws-cdk/aws-ssm.IStringListParameter")
class IStringListParameter(IParameter, jsii.compat.Protocol):
    """A StringList SSM Parameter."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IStringListParameterProxy

    @property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[str]:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        attribute:
        :attribute:: Value
        """
        ...


class _IStringListParameterProxy(jsii.proxy_for(IParameter)):
    """A StringList SSM Parameter."""
    __jsii_type__ = "@aws-cdk/aws-ssm.IStringListParameter"
    @property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[str]:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).

        attribute:
        :attribute:: Value
        """
        return jsii.get(self, "stringListValue")


@jsii.interface(jsii_type="@aws-cdk/aws-ssm.IStringParameter")
class IStringParameter(IParameter, jsii.compat.Protocol):
    """A String SSM Parameter."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IStringParameterProxy

    @property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> str:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        attribute:
        :attribute:: Value
        """
        ...


class _IStringParameterProxy(jsii.proxy_for(IParameter)):
    """A String SSM Parameter."""
    __jsii_type__ = "@aws-cdk/aws-ssm.IStringParameter"
    @property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> str:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.

        attribute:
        :attribute:: Value
        """
        return jsii.get(self, "stringValue")


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.ParameterOptions", jsii_struct_bases=[], name_mapping={'allowed_pattern': 'allowedPattern', 'description': 'description', 'parameter_name': 'parameterName'})
class ParameterOptions():
    def __init__(self, *, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, parameter_name: typing.Optional[str]=None):
        """Properties needed to create a new SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        """
        self._values = {
        }
        if allowed_pattern is not None: self._values["allowed_pattern"] = allowed_pattern
        if description is not None: self._values["description"] = description
        if parameter_name is not None: self._values["parameter_name"] = parameter_name

    @property
    def allowed_pattern(self) -> typing.Optional[str]:
        """A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\d+$``

        default
        :default: no validation is performed
        """
        return self._values.get('allowed_pattern')

    @property
    def description(self) -> typing.Optional[str]:
        """Information about the parameter that you want to add to the system.

        default
        :default: none
        """
        return self._values.get('description')

    @property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter.

        default
        :default: - a name will be generated by CloudFormation
        """
        return self._values.get('parameter_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ParameterOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ssm.ParameterType")
class ParameterType(enum.Enum):
    """SSM parameter type."""
    STRING = "STRING"
    """String."""
    SECURE_STRING = "SECURE_STRING"
    """Secure String Parameter Store uses an AWS Key Management Service (KMS) customer master key (CMK) to encrypt the parameter value."""
    STRING_LIST = "STRING_LIST"
    """String List."""
    AWS_EC2_IMAGE_ID = "AWS_EC2_IMAGE_ID"
    """An Amazon EC2 image ID, such as ami-0ff8a91507f77f867."""

@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.SecureStringParameterAttributes", jsii_struct_bases=[], name_mapping={'parameter_name': 'parameterName', 'version': 'version', 'encryption_key': 'encryptionKey'})
class SecureStringParameterAttributes():
    def __init__(self, *, parameter_name: str, version: jsii.Number, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None):
        """
        :param parameter_name: The name of the parameter store value.
        :param version: The version number of the value you wish to retrieve. This is required for secure strings.
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        """
        self._values = {
            'parameter_name': parameter_name,
            'version': version,
        }
        if encryption_key is not None: self._values["encryption_key"] = encryption_key

    @property
    def parameter_name(self) -> str:
        """The name of the parameter store value."""
        return self._values.get('parameter_name')

    @property
    def version(self) -> jsii.Number:
        """The version number of the value you wish to retrieve.

        This is required for secure strings.
        """
        return self._values.get('version')

    @property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        """The encryption key that is used to encrypt this parameter.

        default
        :default: - default master key
        """
        return self._values.get('encryption_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SecureStringParameterAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IStringListParameter, IParameter)
class StringListParameter(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.StringListParameter"):
    """Creates a new StringList SSM Parameter.

    resource:
    :resource:: AWS::SSM::Parameter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, string_list_value: typing.List[str], allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, parameter_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        """
        props = StringListParameterProps(string_list_value=string_list_value, allowed_pattern=allowed_pattern, description=description, parameter_name=parameter_name)

        jsii.create(StringListParameter, self, [scope, id, props])

    @jsii.member(jsii_name="fromStringListParameterName")
    @classmethod
    def from_string_list_parameter_name(cls, scope: aws_cdk.core.Construct, id: str, string_list_parameter_name: str) -> "IStringListParameter":
        """Imports an external parameter of type string list.

        :param scope: -
        :param id: -
        :param string_list_parameter_name: -
        """
        return jsii.sinvoke(cls, "fromStringListParameterName", [scope, id, string_list_parameter_name])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        """
        return jsii.invoke(self, "grantWrite", [grantee])

    @property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> str:
        """The ARN of the SSM Parameter resource."""
        return jsii.get(self, "parameterArn")

    @property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> str:
        """The name of the SSM Parameter resource."""
        return jsii.get(self, "parameterName")

    @property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> str:
        """The type of the SSM Parameter resource."""
        return jsii.get(self, "parameterType")

    @property
    @jsii.member(jsii_name="stringListValue")
    def string_list_value(self) -> typing.List[str]:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value. Values in the array
        cannot contain commas (``,``).
        """
        return jsii.get(self, "stringListValue")

    @property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        return jsii.get(self, "encryptionKey")


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.StringListParameterProps", jsii_struct_bases=[ParameterOptions], name_mapping={'allowed_pattern': 'allowedPattern', 'description': 'description', 'parameter_name': 'parameterName', 'string_list_value': 'stringListValue'})
class StringListParameterProps(ParameterOptions):
    def __init__(self, *, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, parameter_name: typing.Optional[str]=None, string_list_value: typing.List[str]):
        """Properties needed to create a StringList SSM Parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param string_list_value: The values of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        """
        self._values = {
            'string_list_value': string_list_value,
        }
        if allowed_pattern is not None: self._values["allowed_pattern"] = allowed_pattern
        if description is not None: self._values["description"] = description
        if parameter_name is not None: self._values["parameter_name"] = parameter_name

    @property
    def allowed_pattern(self) -> typing.Optional[str]:
        """A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\d+$``

        default
        :default: no validation is performed
        """
        return self._values.get('allowed_pattern')

    @property
    def description(self) -> typing.Optional[str]:
        """Information about the parameter that you want to add to the system.

        default
        :default: none
        """
        return self._values.get('description')

    @property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter.

        default
        :default: - a name will be generated by CloudFormation
        """
        return self._values.get('parameter_name')

    @property
    def string_list_value(self) -> typing.List[str]:
        """The values of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        """
        return self._values.get('string_list_value')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StringListParameterProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IStringParameter, IParameter)
class StringParameter(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ssm.StringParameter"):
    """Creates a new String SSM Parameter.

    resource:
    :resource:: AWS::SSM::Parameter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, string_value: str, type: typing.Optional["ParameterType"]=None, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, parameter_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        """
        props = StringParameterProps(string_value=string_value, type=type, allowed_pattern=allowed_pattern, description=description, parameter_name=parameter_name)

        jsii.create(StringParameter, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecureStringParameterAttributes")
    @classmethod
    def from_secure_string_parameter_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, parameter_name: str, version: jsii.Number, encryption_key: typing.Optional[aws_cdk.aws_kms.IKey]=None) -> "IStringParameter":
        """Imports a secure string parameter from the SSM parameter store.

        :param scope: -
        :param id: -
        :param attrs: -
        :param parameter_name: The name of the parameter store value.
        :param version: The version number of the value you wish to retrieve. This is required for secure strings.
        :param encryption_key: The encryption key that is used to encrypt this parameter. Default: - default master key
        """
        attrs = SecureStringParameterAttributes(parameter_name=parameter_name, version=version, encryption_key=encryption_key)

        return jsii.sinvoke(cls, "fromSecureStringParameterAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromStringParameterAttributes")
    @classmethod
    def from_string_parameter_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, parameter_name: str, type: typing.Optional["ParameterType"]=None, version: typing.Optional[jsii.Number]=None) -> "IStringParameter":
        """Imports an external string parameter with name and optional version.

        :param scope: -
        :param id: -
        :param attrs: -
        :param parameter_name: The name of the parameter store value.
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.
        """
        attrs = StringParameterAttributes(parameter_name=parameter_name, type=type, version=version)

        return jsii.sinvoke(cls, "fromStringParameterAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromStringParameterName")
    @classmethod
    def from_string_parameter_name(cls, scope: aws_cdk.core.Construct, id: str, string_parameter_name: str) -> "IStringParameter":
        """Imports an external string parameter by name.

        :param scope: -
        :param id: -
        :param string_parameter_name: -
        """
        return jsii.sinvoke(cls, "fromStringParameterName", [scope, id, string_parameter_name])

    @jsii.member(jsii_name="valueForSecureStringParameter")
    @classmethod
    def value_for_secure_string_parameter(cls, scope: aws_cdk.core.Construct, parameter_name: str, version: jsii.Number) -> str:
        """Returns a token that will resolve (during deployment).

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (required for secure strings).
        """
        return jsii.sinvoke(cls, "valueForSecureStringParameter", [scope, parameter_name, version])

    @jsii.member(jsii_name="valueForStringParameter")
    @classmethod
    def value_for_string_parameter(cls, scope: aws_cdk.core.Construct, parameter_name: str, version: typing.Optional[jsii.Number]=None) -> str:
        """Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        """
        return jsii.sinvoke(cls, "valueForStringParameter", [scope, parameter_name, version])

    @jsii.member(jsii_name="valueForTypedStringParameter")
    @classmethod
    def value_for_typed_string_parameter(cls, scope: aws_cdk.core.Construct, parameter_name: str, type: typing.Optional["ParameterType"]=None, version: typing.Optional[jsii.Number]=None) -> str:
        """Returns a token that will resolve (during deployment) to the string value of an SSM string parameter.

        :param scope: Some scope within a stack.
        :param parameter_name: The name of the SSM parameter.
        :param type: The type of the SSM parameter.
        :param version: The parameter version (recommended in order to ensure that the value won't change during deployment).
        """
        return jsii.sinvoke(cls, "valueForTypedStringParameter", [scope, parameter_name, type, version])

    @jsii.member(jsii_name="valueFromLookup")
    @classmethod
    def value_from_lookup(cls, scope: aws_cdk.core.Construct, parameter_name: str) -> str:
        """Reads the value of an SSM parameter during synthesis through an environmental context provider.

        Requires that the stack this scope is defined in will have explicit
        account/region information. Otherwise, it will fail during synthesis.

        :param scope: -
        :param parameter_name: -
        """
        return jsii.sinvoke(cls, "valueFromLookup", [scope, parameter_name])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants read (DescribeParameter, GetParameter, GetParameterHistory) permissions on the SSM Parameter.

        :param grantee: -
        """
        return jsii.invoke(self, "grantRead", [grantee])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grants write (PutParameter) permissions on the SSM Parameter.

        :param grantee: -
        """
        return jsii.invoke(self, "grantWrite", [grantee])

    @property
    @jsii.member(jsii_name="parameterArn")
    def parameter_arn(self) -> str:
        """The ARN of the SSM Parameter resource."""
        return jsii.get(self, "parameterArn")

    @property
    @jsii.member(jsii_name="parameterName")
    def parameter_name(self) -> str:
        """The name of the SSM Parameter resource."""
        return jsii.get(self, "parameterName")

    @property
    @jsii.member(jsii_name="parameterType")
    def parameter_type(self) -> str:
        """The type of the SSM Parameter resource."""
        return jsii.get(self, "parameterType")

    @property
    @jsii.member(jsii_name="stringValue")
    def string_value(self) -> str:
        """The parameter value.

        Value must not nest another parameter. Do not use {{}} in the value.
        """
        return jsii.get(self, "stringValue")

    @property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        return jsii.get(self, "encryptionKey")


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.StringParameterAttributes", jsii_struct_bases=[], name_mapping={'parameter_name': 'parameterName', 'type': 'type', 'version': 'version'})
class StringParameterAttributes():
    def __init__(self, *, parameter_name: str, type: typing.Optional["ParameterType"]=None, version: typing.Optional[jsii.Number]=None):
        """
        :param parameter_name: The name of the parameter store value.
        :param type: The type of the string parameter. Default: ParameterType.STRING
        :param version: The version number of the value you wish to retrieve. Default: The latest version will be retrieved.
        """
        self._values = {
            'parameter_name': parameter_name,
        }
        if type is not None: self._values["type"] = type
        if version is not None: self._values["version"] = version

    @property
    def parameter_name(self) -> str:
        """The name of the parameter store value."""
        return self._values.get('parameter_name')

    @property
    def type(self) -> typing.Optional["ParameterType"]:
        """The type of the string parameter.

        default
        :default: ParameterType.STRING
        """
        return self._values.get('type')

    @property
    def version(self) -> typing.Optional[jsii.Number]:
        """The version number of the value you wish to retrieve.

        default
        :default: The latest version will be retrieved.
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StringParameterAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ssm.StringParameterProps", jsii_struct_bases=[ParameterOptions], name_mapping={'allowed_pattern': 'allowedPattern', 'description': 'description', 'parameter_name': 'parameterName', 'string_value': 'stringValue', 'type': 'type'})
class StringParameterProps(ParameterOptions):
    def __init__(self, *, allowed_pattern: typing.Optional[str]=None, description: typing.Optional[str]=None, parameter_name: typing.Optional[str]=None, string_value: str, type: typing.Optional["ParameterType"]=None):
        """Properties needed to create a String SSM parameter.

        :param allowed_pattern: A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``^\d+$`` Default: no validation is performed
        :param description: Information about the parameter that you want to add to the system. Default: none
        :param parameter_name: The name of the parameter. Default: - a name will be generated by CloudFormation
        :param string_value: The value of the parameter. It may not reference another parameter and ``{{}}`` cannot be used in the value.
        :param type: The type of the string parameter. Default: ParameterType.STRING
        """
        self._values = {
            'string_value': string_value,
        }
        if allowed_pattern is not None: self._values["allowed_pattern"] = allowed_pattern
        if description is not None: self._values["description"] = description
        if parameter_name is not None: self._values["parameter_name"] = parameter_name
        if type is not None: self._values["type"] = type

    @property
    def allowed_pattern(self) -> typing.Optional[str]:
        """A regular expression used to validate the parameter value.

        For example, for String types with values restricted to
        numbers, you can specify the following: ``^\d+$``

        default
        :default: no validation is performed
        """
        return self._values.get('allowed_pattern')

    @property
    def description(self) -> typing.Optional[str]:
        """Information about the parameter that you want to add to the system.

        default
        :default: none
        """
        return self._values.get('description')

    @property
    def parameter_name(self) -> typing.Optional[str]:
        """The name of the parameter.

        default
        :default: - a name will be generated by CloudFormation
        """
        return self._values.get('parameter_name')

    @property
    def string_value(self) -> str:
        """The value of the parameter.

        It may not reference another parameter and ``{{}}`` cannot be used in the value.
        """
        return self._values.get('string_value')

    @property
    def type(self) -> typing.Optional["ParameterType"]:
        """The type of the string parameter.

        default
        :default: ParameterType.STRING
        """
        return self._values.get('type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'StringParameterProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnAssociation", "CfnAssociationProps", "CfnDocument", "CfnDocumentProps", "CfnMaintenanceWindow", "CfnMaintenanceWindowProps", "CfnMaintenanceWindowTarget", "CfnMaintenanceWindowTargetProps", "CfnMaintenanceWindowTask", "CfnMaintenanceWindowTaskProps", "CfnParameter", "CfnParameterProps", "CfnPatchBaseline", "CfnPatchBaselineProps", "CfnResourceDataSync", "CfnResourceDataSyncProps", "IParameter", "IStringListParameter", "IStringParameter", "ParameterOptions", "ParameterType", "SecureStringParameterAttributes", "StringListParameter", "StringListParameterProps", "StringParameter", "StringParameterAttributes", "StringParameterProps", "__jsii_assembly__"]

publication.publish()
