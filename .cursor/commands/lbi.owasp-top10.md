# OWASP Top 10 Security Checklist

Review and verify the application against the OWASP Top 10 security risks.

## Instructions

1. Review each category systematically
2. Mark items as PASS, FAIL, or N/A
3. Document findings and remediation steps
4. Prioritize fixes based on severity

---

## A01:2021 - Broken Access Control

Access control enforces policy so users cannot act outside their intended permissions.

### Checklist

- [ ] Deny access by default (except for public resources)
- [ ] Implement access control mechanisms once and reuse
- [ ] Model access controls enforce record ownership
- [ ] Unique application business limit requirements enforced by domain models
- [ ] Disable web server directory listing
- [ ] File metadata and backup files not in web roots
- [ ] Log access control failures and alert admins
- [ ] Rate limit API and controller access
- [ ] Invalidate JWT tokens on server after logout
- [ ] Developers and QA include functional access control tests

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A02:2021 - Cryptographic Failures

Previously known as Sensitive Data Exposure. Focus on failures related to cryptography.

### Checklist

- [ ] Classify data processed, stored, or transmitted
- [ ] Identify sensitive data per regulations (GDPR, PCI DSS, etc.)
- [ ] Don't store sensitive data unnecessarily
- [ ] Encrypt all sensitive data at rest
- [ ] Use up-to-date and strong algorithms/protocols/keys
- [ ] Encrypt all data in transit with TLS
- [ ] Disable caching for responses with sensitive data
- [ ] Apply required security controls per data classification
- [ ] Don't use legacy protocols (FTP, SMTP for sensitive data)
- [ ] Use authenticated encryption (not just encryption)
- [ ] Use cryptographically secure random functions
- [ ] Avoid deprecated hash functions (MD5, SHA1)
- [ ] Independently verify encryption configuration

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A03:2021 - Injection

User-supplied data not validated, filtered, or sanitized by the application.

### Checklist

- [ ] Use a safe API avoiding the interpreter entirely
- [ ] Use positive server-side input validation
- [ ] Escape special characters for residual dynamic queries
- [ ] Use LIMIT and other SQL controls to prevent mass disclosure
- [ ] Use parameterized queries for all database access
- [ ] Validate and sanitize all user input
- [ ] Implement Content Security Policy (CSP)
- [ ] Use ORM or prepared statements

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A04:2021 - Insecure Design

Focus on risks related to design and architectural flaws.

### Checklist

- [ ] Establish secure development lifecycle with AppSec professionals
- [ ] Use secure design patterns library
- [ ] Use threat modeling for critical flows
- [ ] Integrate security language and controls into user stories
- [ ] Integrate plausibility checks at each tier
- [ ] Write unit and integration tests for security controls
- [ ] Segregate tier layers on system and network levels
- [ ] Tenant isolation by design
- [ ] Limit resource consumption by user or service

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A05:2021 - Security Misconfiguration

Missing security hardening or improperly configured permissions.

### Checklist

- [ ] Repeatable hardening process for fast deployment
- [ ] Minimal platform without unnecessary features
- [ ] Review and update configurations for all security notes
- [ ] Segmented application architecture
- [ ] Send security directives to clients (Security Headers)
- [ ] Automated process to verify configurations
- [ ] Remove unused features and frameworks
- [ ] Proper error handling (no stack traces to users)
- [ ] Disable XML external entities (XXE)

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A06:2021 - Vulnerable and Outdated Components

Components with known vulnerabilities or unsupported software.

### Checklist

- [ ] Remove unused dependencies and features
- [ ] Continuously inventory component versions
- [ ] Monitor CVE and NVD for vulnerabilities
- [ ] Obtain components from official sources only
- [ ] Monitor unmaintained libraries
- [ ] Plan for updating/replacing old components
- [ ] Apply security patches in timely manner

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A07:2021 - Identification and Authentication Failures

Confirmation of user identity, authentication, and session management.

### Checklist

- [ ] Implement multi-factor authentication where possible
- [ ] Don't ship with default credentials
- [ ] Implement weak password checks
- [ ] Align password policies with NIST 800-63b
- [ ] Harden registration and credential recovery paths
- [ ] Limit or increasingly delay failed login attempts
- [ ] Use server-side secure session manager
- [ ] Use high entropy random session IDs
- [ ] Invalidate sessions after logout and idle timeout

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A08:2021 - Software and Data Integrity Failures

Code and infrastructure that doesn't protect against integrity violations.

### Checklist

- [ ] Use digital signatures to verify software/data
- [ ] Use trusted repositories for libraries
- [ ] Use software supply chain security tools (OWASP Dependency-Check)
- [ ] Review code and configuration changes
- [ ] Ensure CI/CD pipeline has proper segregation and access control
- [ ] Don't send unsigned or unencrypted serialized data
- [ ] Implement integrity checks for serialized data

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A09:2021 - Security Logging and Monitoring Failures

Without logging and monitoring, breaches cannot be detected.

### Checklist

- [ ] Log all login, access control, and server-side validation failures
- [ ] Generate logs in format consumed by log management solutions
- [ ] Encode log data correctly to prevent injection
- [ ] Ensure high-value transactions have audit trail
- [ ] Establish effective monitoring and alerting
- [ ] Establish incident response and recovery plan
- [ ] Use application security testing tools in CI/CD

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## A10:2021 - Server-Side Request Forgery (SSRF)

SSRF flaws occur when fetching a remote resource without validating URL.

### Checklist

- [ ] Sanitize and validate all client-supplied input data
- [ ] Enforce URL schema, port, and destination with allowlist
- [ ] Don't send raw responses to clients
- [ ] Disable HTTP redirections
- [ ] Be aware of URL consistency to avoid DNS rebinding
- [ ] Don't deploy relevant security services on fronting systems

### Findings

| Finding | Severity | Location | Status |
|---------|----------|----------|--------|
|         |          |          |        |

---

## Summary

| Category | Status | Critical Issues | Notes |
|----------|--------|-----------------|-------|
| A01 - Broken Access Control | | | |
| A02 - Cryptographic Failures | | | |
| A03 - Injection | | | |
| A04 - Insecure Design | | | |
| A05 - Security Misconfiguration | | | |
| A06 - Vulnerable Components | | | |
| A07 - Auth Failures | | | |
| A08 - Integrity Failures | | | |
| A09 - Logging Failures | | | |
| A10 - SSRF | | | |

## Next Steps

1. Address critical findings immediately
2. Create tickets for medium/high severity issues
3. Schedule review for low severity items
4. Update security documentation
5. Re-test after remediation