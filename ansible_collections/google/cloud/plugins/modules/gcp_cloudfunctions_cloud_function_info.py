#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_cloudfunctions_cloud_function_info
description:
- Gather info for GCP CloudFunction
short_description: Gather info for GCP CloudFunction
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  location:
    description:
    - The location of this cloud function.
    required: true
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: get info on a cloud function
  gcp_cloudfunctions_cloud_function_info:
    location: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    name:
      description:
      - A user-defined name of the function. Function names must be unique globally
        and match pattern `projects/*/locations/*/functions/*`.
      returned: success
      type: str
    description:
      description:
      - User-provided description of a function.
      returned: success
      type: str
    status:
      description:
      - Status of the function deployment.
      returned: success
      type: str
    entryPoint:
      description:
      - The name of the function (as defined in source code) that will be executed.
      - Defaults to the resource name suffix, if not specified. For backward compatibility,
        if function with given name is not found, then the system will try to use
        function named "function". For Node.js this is name of a function exported
        by the module specified in source_location.
      returned: success
      type: str
    runtime:
      description:
      - The runtime in which the function is going to run. If empty, defaults to Node.js
        6.
      returned: success
      type: str
    timeout:
      description:
      - The function execution timeout. Execution is considered failed and can be
        terminated if the function is not completed at the end of the timeout period.
        Defaults to 60 seconds.
      returned: success
      type: str
    availableMemoryMb:
      description:
      - The amount of memory in MB available for a function.
      returned: success
      type: int
    serviceAccountEmail:
      description:
      - The email of the service account for this function.
      returned: success
      type: str
    updateTime:
      description:
      - The last update timestamp of a Cloud Function.
      returned: success
      type: str
    versionId:
      description:
      - The version identifier of the Cloud Function. Each deployment attempt results
        in a new version of a function being created.
      returned: success
      type: str
    labels:
      description:
      - A set of key/value label pairs associated with this Cloud Function.
      returned: success
      type: dict
    environmentVariables:
      description:
      - Environment variables that shall be available during function execution.
      returned: success
      type: dict
    sourceArchiveUrl:
      description:
      - The Google Cloud Storage URL, starting with gs://, pointing to the zip archive
        which contains the function.
      returned: success
      type: str
    sourceUploadUrl:
      description:
      - The Google Cloud Storage signed URL used for source uploading.
      returned: success
      type: str
    sourceRepository:
      description:
      - The source repository where a function is hosted.
      returned: success
      type: complex
      contains:
        url:
          description:
          - The URL pointing to the hosted repository where the function is defined
            .
          returned: success
          type: str
        deployedUrl:
          description:
          - The URL pointing to the hosted repository where the function were defined
            at the time of deployment.
          returned: success
          type: str
    httpsTrigger:
      description:
      - An HTTPS endpoint type of source that can be triggered via URL.
      returned: success
      type: complex
      contains:
        url:
          description:
          - The deployed url for the function.
          returned: success
          type: str
    eventTrigger:
      description:
      - An HTTPS endpoint type of source that can be triggered via URL.
      returned: success
      type: complex
      contains:
        eventType:
          description:
          - 'The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change`
            and `providers/cloud.pubsub/eventTypes/topic.publish`.'
          returned: success
          type: str
        resource:
          description:
          - The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket.`
            .
          returned: success
          type: str
        service:
          description:
          - The hostname of the service that should be observed.
          returned: success
          type: str
    location:
      description:
      - The location of this cloud function.
      returned: success
      type: str
    trigger_http:
      description:
      - Use HTTP to trigger this function.
      returned: success
      type: bool
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(location=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    return "https://cloudfunctions.googleapis.com/v1/projects/{project}/locations/{location}/functions".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'cloudfunctions')
    return auth.list(link, return_if_object, array_name='functions')


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
