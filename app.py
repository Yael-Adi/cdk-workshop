#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack


app = cdk.App()
CdkWorkshopStack(app, "CdkWorkshopStack",
    env=cdk.Environment(
        account=app.node.try_get_context("account") or "992382459260",
        region=app.node.try_get_context("region") or "il-central-1"
    )
)

app.synth()
