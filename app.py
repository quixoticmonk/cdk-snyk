#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_snyk.cdk_snyk_stack import CdkSnykStack


app = cdk.App()
CdkSnykStack(app, "CdkSnykStack")

app.synth()
