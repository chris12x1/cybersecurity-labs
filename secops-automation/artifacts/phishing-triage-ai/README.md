# Phishing Triage Automation Artifacts – AI Pipeline

This directory contains sanitized and redacted artifacts collected during the automated phishing triage investigation documented in:
**[phishing-triage-ai](https://github.com/chris12x1/cybersecurity-projects/blob/main/secops-automation/phishing-triage-ai.md)**

All indicators have been defanged and sensitive details (such as API keys and personal metadata) have been redacted to preserve forensic and educational value while preventing accidental execution or exposure.

## Evidence & Artifacts Included

- **Workflow Orchestration:** Visual evidence of the n8n logic gates and node connections.
- **Tunneling & Webhook Logs:** Sanitized terminal output from ngrok and AgentMail showing the live POST requests.
- **AI Security Verdicts:** Redacted JSON payloads from Gemini AI showing the logic used to flag "test" phishing scenarios.
- **Automated Audit Log:** Screenshots of the centralized Google Sheet reflecting the final triaged output.

## Forensic Note
These artifacts demonstrate the transition from the manual forensic methods used in the **[Phishing Email Analysis – Yahoo Storage Scam](https://github.com/chris12x1/cybersecurity-projects/blob/main/incident-response/phishing-email-analysis-yahoo-storage.md)** to a fully automated SecOps pipeline.
