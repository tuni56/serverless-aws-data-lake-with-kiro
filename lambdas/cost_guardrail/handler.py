from checks.athena import check_athena
from checks.glue import check_glue
from checks.s3 import check_s3

def handler(event, context):
    findings = []

    findings.extend(check_athena())
    findings.extend(check_glue())
    findings.extend(check_s3())

    if findings:
        print("⚠️ Cost guardrail findings:")
        for f in findings:
            print(f)
    else:
        print("✅ All cost guardrails passed")

    return {
        "status": "OK" if not findings else "WARN",
        "findings": findings
    }
