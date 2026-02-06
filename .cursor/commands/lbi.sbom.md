# Software Bill of Materials (SBOM) Guide

Generate and manage Software Bill of Materials for compliance and security.

## What is an SBOM?

A Software Bill of Materials is a formal, machine-readable inventory of software components and dependencies, including information about licensing and relationships.

---

## 1. Why Generate an SBOM?

### Compliance Requirements

- **Executive Order 14028**: US federal contractors must provide SBOMs
- **EU Cyber Resilience Act**: Requires software composition documentation
- **FDA Cybersecurity**: Medical device software must include SBOMs
- **PCI DSS 4.0**: Software inventory requirements

### Security Benefits

- Identify vulnerable components quickly
- Track license compliance
- Manage supply chain risks
- Enable faster incident response

---

## 2. SBOM Formats

### CycloneDX

Lightweight, security-focused format. Recommended for most use cases.

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "components": [...]
}
```

### SPDX

Comprehensive format for license compliance.

```json
{
  "spdxVersion": "SPDX-2.3",
  "documentNamespace": "...",
  "packages": [...]
}
```

---

## 3. Generating SBOMs

### Using Syft (Recommended)

```bash
# Install syft
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh

# Generate CycloneDX SBOM
syft . -o cyclonedx-json > sbom.json

# Generate SPDX SBOM
syft . -o spdx-json > sbom.spdx.json

# Scan a container image
syft alpine:latest -o cyclonedx-json
```

### Using pip-tools (Python)

```bash
# Export all dependencies
pip freeze > requirements.txt

# Generate with pip-licenses
pip install pip-licenses
pip-licenses --format=json > licenses.json
```

### Using CycloneDX Tools

```bash
# Python
pip install cyclonedx-bom
cyclonedx-py -r requirements.txt -o sbom.json

# Node.js
npm install -g @cyclonedx/cyclonedx-npm
cyclonedx-npm --output-file sbom.json
```

---

## 4. SBOM Contents

### Required Fields

| Field | Description |
|-------|-------------|
| Component Name | Name of the package/library |
| Version | Exact version number |
| Supplier | Package author/maintainer |
| Unique Identifier | purl, CPE, or SWID |

### Recommended Fields

| Field | Description |
|-------|-------------|
| License | SPDX license identifier |
| Hash | SHA-256 of the component |
| Dependencies | Direct dependencies |
| Source | Repository URL |

---

## 5. SBOM Verification

### Validate CycloneDX

```bash
# Install validator
pip install cyclonedx-python-lib

# Validate SBOM
python -c "
from cyclonedx.model.bom import Bom
from cyclonedx.parser import JsonParser
bom = JsonParser().parse_file('sbom.json')
print(f'Components: {len(bom.components)}')
"
```

### Check Against Vulnerabilities

```bash
# Using grype
grype sbom:sbom.json

# Using osv-scanner
osv-scanner --sbom=sbom.json
```

---

## 6. SBOM Integration

### CI/CD Pipeline

```yaml
# GitHub Actions example
sbom-generation:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Generate SBOM
      uses: anchore/sbom-action@v0
      with:
        format: cyclonedx-json
        output-file: sbom.json
    - name: Upload SBOM
      uses: actions/upload-artifact@v4
      with:
        name: sbom
        path: sbom.json
```

### Storage and Distribution

- Store SBOMs alongside releases
- Include in container image labels
- Publish to dependency-track or similar

---

## 7. SBOM Checklist

### Generation

- [ ] SBOM format selected (CycloneDX/SPDX)
- [ ] Generation tool installed and configured
- [ ] All dependencies included (direct and transitive)
- [ ] License information captured
- [ ] Hash/checksum included

### Validation

- [ ] SBOM passes schema validation
- [ ] All components have unique identifiers
- [ ] No placeholder or incomplete data
- [ ] Version numbers are accurate

### Process

- [ ] SBOM generation in CI/CD
- [ ] SBOM stored with releases
- [ ] SBOM shared with stakeholders
- [ ] Regular SBOM updates scheduled

### Security

- [ ] SBOM scanned for vulnerabilities
- [ ] High-risk components identified
- [ ] License conflicts resolved
- [ ] Outdated dependencies flagged

---

## 8. Resources

### Tools

- [Syft](https://github.com/anchore/syft) - SBOM generation
- [Grype](https://github.com/anchore/grype) - Vulnerability scanning
- [Dependency-Track](https://dependencytrack.org/) - SBOM management

### Standards

- [CycloneDX Specification](https://cyclonedx.org/specification/overview/)
- [SPDX Specification](https://spdx.github.io/spdx-spec/)
- [NTIA SBOM Minimum Elements](https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report.pdf)

### Guidance

- [CISA SBOM Resources](https://www.cisa.gov/sbom)
- [OWASP Software Component Verification](https://owasp.org/www-project-software-component-verification-standard/)