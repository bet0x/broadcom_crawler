---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Standards Compliance
---

# Standards Compliance

NSX is configured to use FIPS 140-3 validated cryptographic modules by default to comply with FIPS requirements. The modules are validated to FIPS 140-3 standards by the NIST Cryptographic Module Validation Program (CMVP).

All exceptions to FIPS compliance can be retrieved using the compliance report. See [View Compliance Status Report](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations/view-compliance-report.html#GUID-f0e52b5f-cc6d-4fa8-a92a-5288b9e78007-en) for more information.

The following validated modules are used:

- VMware VPN Crypto Module 2.0, Certificate #[4881](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4881)
- IKE: Rambus Safezone 2.0, Certificate #[4898](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4898)
- VMware Openssl 3.0.9, Certificate **#**[4861](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4861)
- VMware BouncyCastle 2.0.0, Certificate #[4986](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4986)
- VMware BoringCrypto 6.0, Certificate #[4694](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4694)

You can find more information about the cryptographic modules that VMware has validated against the FIPS 140 standard here: <https://www.vmware.com/security/certifications/fips.html>.