# 1. ZTA Component Definitions 

## Policy Engine (PA) - The Brain
The Policy Engine (PE) is the key decision-maker in a Zero Trust Architecture. It determines whether access should be granted, denied, or revoked based on available security signals such as user identity, device type, geographic location, behavioral patterns, and threat intelligence. The PE evaluates these factors against a defined set of security policies and produces a real-time “trust verdict.” While it does not directly enforce access, it provides the authorization decision that other components execute. I think of the PE as a genius sitting in a chair with all the relevant information laid out in front of it, empowered to make informed decisions that protect the security of a service.

## Policy Administrator (PA) - The Rulesetter

The Policy Administrator is the bridge in communication for the "Brain" (Policy Engine) and the "Door" (Policy Enforcement Point). Once the PE makes a decision whether a request is valid or not, the PA translates the verdict into instructions for the PEP to allow or deny access. The PA manages session tokens, credentials, and configurations needed to operationalize the PE's ruling. Think of someone translating a list of rules from a higher-up in a company and putting it neatly into one document per department of the company. 
## Policy Enforcement Point (PEP) - The Rule Setter


The Policy Enforcement Point is the physical checkpoint that allows/denies traffic from users or devices and the requested resource (such as a web application or database). There is no thought process involved with the PEP; it simply acts based on instructions from the PA, which are orders decided upon by the PE. Every single request is processed through the PEP, making it the perfect boundary for Zero Trust's "never trust, always verify" principle.
# 2. Core Principle Application 
Principle chosen: Verify explicitly
The PE never assumes trust based on a single factor. It actively checks every available signal on every request to ensure nothing is left unverified. 

Example — Water Treatment Facility:
Supervisor Henry attempts to access chemical dosing control data at 11:45 PM from an off-site IP on a personal laptop. Even though his credentials are valid, the PE checks everything:
| Signal | Finding | Result |
|---|---|---|
| User Identity | Valid credentials | ✅ Pass |
| Location | Unknown off-site IP | ⚠️ Suspicious |
| Time of Access | Outside normal shift hours | ⚠️ Anomalous |
| Device Health | Unregistered personal laptop | ❌ Fail |
PE Decision → DENY. Even though the user credentials are valid, the combination of a suspicious IP address location, unusual timing, and an unregistered device leads us to deny the request.  This scenario exemplifies the principle in Verify Explicitly that trust isn't granted based upon one successful check. Access is granted only when all signals meet the policy standards. 

# 3. Simplified Policy Table 

**Target Resource:** HR Employee PII Database — Golden State Water Treatment Facility  

| Policy Requirement (Signal) | Condition to Be Met by User | Action if Condition is Met | Action if Condition Fails |
|---|---|---|---|
| User Identity | User must pass MFA and hold an active HR or Payroll role in the directory. | ✅ Identity verified — proceed to next signal. | 🚫 Deny Access — failed MFA, suspended account, or no HR role. |
| Device Posture | Device must be company-managed (MDM enrolled), fully patched, and running active endpoint protection. | ✅ Device compliant — proceed to next signal. | 🚫 Deny Access — personal/unregistered device, outdated OS, or missing antivirus. |
| Network Context | Request must come from the facility's internal network or approved VPN during business hours (6 AM–7 PM PST). | ✅ All signals verified — PA instructs PEP to grant access. | 🚫 Deny Access — off-network without VPN, foreign IP, or outside business hours. |

# 4. Submission Details 

# Git Repository Metadata

Project: Lab 6 - Zero Trust Policy  

Filename: ZT-Policy-Profile.md      

Commit Message: Lab 6 - Zero Trust Policy Profile for IT335 Corporate Cybersecurity with Dr. Safi Mojidi
Github URL - https://github.com/hens18/github-portfolio  
