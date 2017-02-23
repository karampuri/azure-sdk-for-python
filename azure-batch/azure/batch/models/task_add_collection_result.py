# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TaskAddCollectionResult(Model):
    """The result of adding a collection of tasks to a job.

    :param value: The results of the add task collection operation.
    :type value: list of :class:`TaskAddResult
     <azure.batch.models.TaskAddResult>`
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TaskAddResult]'},
    }

    def __init__(self, value=None):
        self.value = value
