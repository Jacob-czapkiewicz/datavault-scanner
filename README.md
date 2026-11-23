# DataVault Security Scanner

A command-line tool that finds security problems in code folders and in your own AWS account, and saves every scan to a SQL database.

> **Status: in progress.** DataVault is being built in stages, with a tagged release at the end of each one. The first release, v0.1, will find hard-coded secrets in a folder.

## About this project

I'm building DataVault to learn software engineering and cloud security in practice:
Python packaging, command-line tools, SQL database design, automated testing and the
AWS SDK. It's developed in stages over 16 weeks, with a tagged release at the end of each stage.

## What works today

- Walks a folder and all of its subfolders
- Skips folders that never need scanning: `.git`, `venv`, `__pycache__` and `node_modules`
- Skips files over 1 MB and binary files such as images
- Reads text files in any encoding without crashing
- Reports files it can't open (for example, permission denied) and carries on with the scan

## Roadmap

| Version | Feature | Status |
|---|---|---|
| v0.1 | Find hard-coded secrets (AWS keys, GitHub tokens, private keys, passwords) and report the file and line | In progress |
| v0.2 | Save every scan to SQLite, with `history`, `show` and `stats` commands | Planned |
| v0.3 | Check an AWS account for public S3 buckets, IAM users without MFA, old access keys and open SSH/RDP rules | Planned |
| v0.4 | Export HTML and CSV reports, and compare two scans to see what got fixed | Planned |
| v1.0 | Polished release | Planned |

## Requirements

- Python 3.12 or newer
- No other packages yet

## Getting started

```bash
git clone https://github.com/Jacob-czapkiewicz/datavault-scanner.git
cd datavault-scanner
python3 -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
```

## Usage

For now, the folder to scan is set on line 10 of `scanner.py`. Change it to the folder you want, then run:

```bash
python scanner.py
```

Example output:

```
DataVault v0.0
Error occurred while processing /Users/jacob/Documents/datavault-test/private/locked.txt: [Errno 13] Permission denied: '/Users/jacob/Documents/datavault-test/private/locked.txt'
Total files scanned: 8
```

A command-line option for choosing the folder is coming in v0.1.

## Safety

Only scan folders and AWS accounts that you own or have permission to test.

## Licence

MIT. See [LICENSE](LICENSE).
