# Phishing Email Analysis – Yahoo Storage Scam

## Overview
This lab documents the analysis of a suspected phishing email impersonating Yahoo, using email header analysis and URL investigation tools.

## Email Summary
- Email Type: Phishing (Credential Harvesting)
- Attack Vector: Email
- Impersonated Brand: Yahoo
- User Impact: Account compromise risk

## Tools Used
- MXToolbox (Email Header Analysis)
- urlscan.io (URL behavior analysis)
- Manual inspection

## Analysis Performed
- Reviewed sender address and email content
- Analyzed SPF authentication results
- Investigated embedded URL behavior
- Identified social engineering techniques

## Key Findings
- Sender domain not associated with Yahoo
- SPF authentication failure for sending IP
- Obfuscated third-party URL unrelated to Yahoo
- Social engineering using urgency and fear
- Landing page behavior designed to evade detection

## Verdict
This email was classified as **malicious phishing** based on multiple authentication failures, domain impersonation, and deceptive URL behavior.

## Recommended Response
- Block sender domain and IP
- Remove email from inbox
- Educate users on phishing indicators
- Monitor for similar campaigns

## Data Handling & Redaction
All headers, IP addresses, message IDs, and recipient identifiers have been
partially redacted to protect user privacy while preserving forensic value.

## Indicator Sanitization (Defanging)
All URLs and domains in this report have been intentionally defanged
(e.g., `example[.]com`) to prevent accidental clicks or execution.

This is a standard incident response practice used to safely share
indicators of compromise (IOCs) in reports and public repositories.

## Evidence
Artifacts for this incident are stored in:
incident-response/artifacts/phishing-yahoo-storage/

