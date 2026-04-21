# Phishing Triage Automation Artifacts – AI Pipeline

This directory contains sanitized and redacted artifacts collected during the automated phishing triage investigation documented in:
**[phishing-triage-ai/README.md](../README.md)**

All indicators have been defanged and sensitive details (such as API keys and personal metadata) have been redacted to preserve forensic and educational value while preventing accidental execution or exposure.

## Evidence & Artifacts Included

- **Workflow Orchestration:** Visual evidence of the n8n logic gates and node connections.
- **Tunneling & Webhook Logs:** Sanitized terminal output from ngrok and AgentMail showing the live POST requests.
- **AI Security Verdicts:** Redacted JSON payloads from Gemini AI showing the logic used to flag "test" phishing scenarios.
- **Automated Audit Log:** Screenshots of the centralized Google Sheet reflecting the final triaged output.

## Forensic Note
These artifacts demonstrate the transition from the manual forensic methods used in the **[Yahoo Storage Scam Lab](../../incident-response/phishing-email-analysis-yahoo-storage.md)** to a fully automated SecOps pipeline.
