# AI-Powered Phishing Triage Automation

## 🔄 Overview & Evolution
This project demonstrates the transition from manual security analysis to automated **Security Operations (SecOps)** orchestration. 

I took the forensic logic from my **[Manual Yahoo Phishing Lab](https://github.com/chris12x1/cybersecurity-projects/blob/main/incident-response/phishing-email-analysis-yahoo-storage.md)**—where I analyzed SPF/DKIM failures and social engineering—and engineered a scalable pipeline to handle these tasks automatically using AI.

---

## 🛠️ The Tech Stack
- **Orchestration:** n8n  
- **AI Engine:** Gemini AI (LLM)  
- **Webhooks & Tunneling:** AgentMail & ngrok  
- **Data Logging:** Google Sheets API  

---

## 🔄 The Automated Workflow
1. **Ingestion:** Captures incoming suspicious emails via an **ngrok** tunnel and **AgentMail** webhook.
2. **Parsing:** Automatically extracts the Sender, Subject, and Body from the raw email payload.
3. **AI Analysis:** **Gemini AI** evaluates the content for red flags (Urgency, Credential Harvesting, Phishing intent).
4. **Final Triage:** The system assigns a "Suspicious" flag and writes the detailed analysis to a centralized Google Sheet.



---

## 🧠 Logic Integration
The automation is programmed to look for the same indicators identified in my manual investigations:
- **Brand Impersonation:** Flagging discrepancies between sender alias and domain.
- **Urgency Tactics:** Detecting fear-based social engineering (e.g., "Subscription Expired").
- **Audit Logging:** Creating a repeatable, machine-readable record for incident response.

---

## 📊 Evidence & Artifacts
Technical logs, workflow screenshots, and sample analysis results are documented here:
[View Automation Artifacts](https://github.com/chris12x1/cybersecurity-projects/tree/main/secops-automation/artifacts/phishing-triage-ai)
