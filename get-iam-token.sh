#!/bin/bash

export IAM_TOKEN=`yc iam create-token`
echo "IAM_TOKEN=$IAM_TOCKEN"