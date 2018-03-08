#!/bin/sh

aws lambda invoke \
--function-name StartEC2Instances \
--invocation-type Event \
--region us-west-1 \
lambda_outfile.txt