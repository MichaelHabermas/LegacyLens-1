# Security Audit Template

Comprehensive security audit for the project.

## Project Information

| Field | Value |
|-------|-------|
| Project Name | |
| Audit Date | |
| Auditor | |
| Version Audited | |
| Previous Audit Date | |

---

## 1. Dependency Security

### 1.1 Dependency Audit

Run dependency vulnerability scans:

```bash
# Python projects
lbi audit

# Or manually
pip-audit
safety check
```

#### Findings

| Package | Version | Vulnerability | Severity | Fix Version |
|---------|---------|---------------|----------|-------------|
|         |         |               |          |             |

### 1.2 Outdated Dependencies

| Package | Current | Latest | Risk Level |
|---------|---------|--------|------------|
|         |         |        |            |

---

## 2. Secrets Detection

### 2.1 Scan Results

Run secrets detection:

```bash
lbi security secrets-scan
```

#### Findings

| File | Line | Type | Status |
|------|------|------|--------|
|      |      |      |        |

### 2.2 Secret Management Review

- [ ] No hardcoded credentials in code
- [ ] Environment variables used for secrets
- [ ] Secrets manager integration (if applicable)
- [ ] .env files excluded from version control
- [ ] CI/CD secrets properly configured

---

## 3. Static Analysis

### 3.1 Security Scan Results

Run static analysis:

```bash
lbi security scan
```

#### Findings

| ID | Issue | File | Line | Severity |
|----|-------|------|------|----------|
|    |       |      |      |          |

### 3.2 Code Quality Issues

| Issue Type | Count | Examples |
|------------|-------|----------|
| SQL Injection Risks | | |
| XSS Vulnerabilities | | |
| Command Injection | | |
| Insecure Functions | | |

---

## 4. Authentication & Authorization

### 4.1 Authentication Review

- [ ] Password hashing uses modern algorithms (bcrypt, argon2)
- [ ] Password complexity requirements enforced
- [ ] Account lockout implemented
- [ ] MFA available/enforced
- [ ] Session management secure
- [ ] Token expiration configured
- [ ] Secure password reset flow

### 4.2 Authorization Review

- [ ] Role-based access control implemented
- [ ] Principle of least privilege followed
- [ ] API endpoints properly protected
- [ ] Admin functions restricted
- [ ] Rate limiting implemented

---

## 5. Data Protection

### 5.1 Data at Rest

- [ ] Sensitive data encrypted
- [ ] Encryption keys properly managed
- [ ] Database connections encrypted
- [ ] Backups encrypted

### 5.2 Data in Transit

- [ ] TLS 1.2+ enforced
- [ ] HSTS enabled
- [ ] Certificate valid and not expiring soon
- [ ] No mixed content

### 5.3 Data Classification

| Data Type | Classification | Protection Level |
|-----------|---------------|------------------|
| User PII | | |
| Credentials | | |
| Payment Data | | |
| Business Data | | |

---

## 6. Infrastructure Security

### 6.1 Server Configuration

- [ ] Unnecessary services disabled
- [ ] Default ports changed (if applicable)
- [ ] Firewall rules configured
- [ ] OS and software updated

### 6.2 Container Security (if applicable)

- [ ] Base images from trusted sources
- [ ] Images scanned for vulnerabilities
- [ ] No root processes in containers
- [ ] Secrets not in images

### 6.3 Cloud Security (if applicable)

- [ ] IAM policies follow least privilege
- [ ] Resources not publicly accessible by default
- [ ] Logging enabled
- [ ] Encryption enabled for storage

---

## 7. Logging & Monitoring

### 7.1 Logging Review

- [ ] Security events logged
- [ ] Logs don't contain sensitive data
- [ ] Log integrity protected
- [ ] Log retention configured

### 7.2 Monitoring Review

- [ ] Alert thresholds configured
- [ ] Security alerts routed correctly
- [ ] Incident response plan exists
- [ ] Regular log review process

---

## 8. Third-Party Integrations

| Integration | Risk Level | Last Reviewed | Notes |
|-------------|------------|---------------|-------|
|             |            |               |       |

---

## 9. Compliance

### 9.1 Regulatory Requirements

| Regulation | Applicable | Status | Notes |
|------------|-----------|--------|-------|
| GDPR | | | |
| PCI DSS | | | |
| HIPAA | | | |
| SOC 2 | | | |

### 9.2 Internal Policies

- [ ] Security policy documented
- [ ] Development guidelines followed
- [ ] Change management process in place
- [ ] Security training completed

---

## 10. Summary

### 10.1 Risk Summary

| Risk Level | Count |
|------------|-------|
| Critical | |
| High | |
| Medium | |
| Low | |

### 10.2 Top Issues

1.
2.
3.
4.
5.

### 10.3 Recommendations

1.
2.
3.

---

## 11. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Auditor | | | |
| Tech Lead | | | |
| Security Lead | | | |

---

## Appendix

### A. Tools Used

- lbi security scan
- lbi audit
- lbi security secrets-scan
- (other tools)

### B. References

- OWASP Top 10
- CWE/SANS Top 25
- NIST Guidelines