# Phishing Email Analysis – Yahoo Storage Scam

## Overview
This mini-project documents the investigation of a phishing email impersonating Yahoo that claims the user’s cloud storage subscription has expired. The analysis focuses on email authentication, sender legitimacy, URL behavior, and social engineering techniques commonly observed in credential-harvesting attacks.

---

## Email Summary
- **Email Type:** Phishing (Credential Harvesting)
- **Attack Vector:** Email
- **Impersonated Brand:** Yahoo
- **User Impact:** Account compromise risk
- **Sender Address (sanitized):**  
  communitybenefitagreementsensurefairoutcomes[@]glovebox-technology-limited[.]com

---

## Tools Used
- **MXToolbox** – Email header, SPF, DKIM, and DMARC analysis  
- **urlscan.io** – URL behavior and redirect analysis  
- **VirusTotal** – Reputation-based threat scanning  
- **WHOIS** – Domain registration analysis  
- **Manual inspection** – Social engineering and content review  

---

## Analysis Performed
- Reviewed sender address, subject line, and email content
- Analyzed email authentication results (SPF, DKIM, DMARC)
- Investigated embedded URL behavior and redirect chain
- Identified social engineering techniques based on urgency and fear
- Validated domain ownership and hosting infrastructure

---

## Key Findings

### Email Authentication
- **SPF:** SoftFail — sending IP not authorized
- **DKIM:** Pass — message signed by sender domain
- **DMARC:** Pass — valid DMARC policy exists

Although DKIM and DMARC passed, the email originated from a domain unrelated to Yahoo, indicating brand impersonation using a properly authenticated but malicious domain.

---

### URL & Domain Analysis
- **Primary URL (defanged):**  
  hxxps://7i7s[.]com/4ykaoY21813zuow120wiiztjxpgx128...

- Hosted behind Cloudflare with WHOIS privacy enabled
- Redirect chain included legitimate third-party domains
- No malware detected via VirusTotal

The presence of legitimate domains in the redirect chain appears to be used for obfuscation and detection evasion.

---

## Verdict
This email was classified as **malicious phishing** based on:
- Brand impersonation of Yahoo
- SPF authentication failure
- Deceptive sender domain
- Obfuscated URL structure
- Social engineering designed to create urgency and fear

---

## Recommended Response
- Block sender domain and associated IPs
- Remove the email from affected mailboxes
- Educate users on phishing indicators
- Monitor for similar impersonation campaigns

---

## Evidence & Artifacts
Screenshots and artifacts supporting this analysis are stored in the following directory:[Phishing Yahoo Artifacts](artifacts/phishing-yahoo-storage/)

