#!/bin/bash 

echo "creating config rule 'access-keys-rotated'"
aws configservice put-config-rule --config-rule '{
    "ConfigRuleName": "access-keys-rotated",
    "Description": "A config rule that checks whether the active access keys are rotated within the number of days specified in maxAccessKeyAge. The rule is NON_COMPLIANT if the access keys have not been rotated for more than maxAccessKeyAge number of days.",
    "Source": {
        "Owner": "AWS",
        "SourceIdentifier": "ACCESS_KEYS_ROTATED",
        "SourceDetails": []
    },
    "Scope": {
        "ComplianceResourceTypes": []
    },
    "InputParameters": "{\"maxAccessKeyAge\":\"90\"}",
    "MaximumExecutionFrequency": "TwentyFour_Hours"
}'
