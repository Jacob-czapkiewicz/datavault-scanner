

import re


RULES = [
    {
        "id": "aws-access-key",
        "name": "AWS access key",
        "pattern": re.compile(r"AKIA[0-9A-Z]{16}"),
        "severity": "HIGH",
    },
    {
        "id": "github-token",
        "name": "GitHub token",
        "pattern": re.compile(r"ghp_[0-9a-zA-Z]{36}"),
        "severity": "HIGH",
    },
    {
        "id": "private-key",
        "name": "Private key",
        "pattern": re.compile(r"^-----BEGIN .*PRIVATE KEY-----$"),
        "severity": "HIGH",
    },
    {
        "id": "password",
        "name": "Password",
        "pattern": re.compile(r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]+['\"]"),
        "severity": "MEDIUM",
    }

]