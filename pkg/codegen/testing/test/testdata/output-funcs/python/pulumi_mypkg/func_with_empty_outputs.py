# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'FuncWithEmptyOutputsResult',
    'AwaitableFuncWithEmptyOutputsResult',
    'func_with_empty_outputs',
    'func_with_empty_outputs_output',
]

@pulumi.output_type
class FuncWithEmptyOutputsResult:
    def __init__(__self__):
        pass

class AwaitableFuncWithEmptyOutputsResult(FuncWithEmptyOutputsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return FuncWithEmptyOutputsResult()


def func_with_empty_outputs(name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableFuncWithEmptyOutputsResult:
    """
    n/a


    :param str name: The Name of the FeatureGroup.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mypkg::funcWithEmptyOutputs', __args__, opts=opts, typ=FuncWithEmptyOutputsResult).value

    return AwaitableFuncWithEmptyOutputsResult()


@_utilities.lift_output_func(func_with_empty_outputs)
def func_with_empty_outputs_output(name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[FuncWithEmptyOutputsResult]:
    """
    n/a


    :param str name: The Name of the FeatureGroup.
    """
    ...
