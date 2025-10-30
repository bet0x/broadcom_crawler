---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/compliance-based-configurations/common-criteria-compliance.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Common Criteria Compliance
---

# Common Criteria Compliance

NSX is designed to be EAL4+ compliant
in accordance with the Common Criteria Certification Program.

For more information about Common Criteria, see the [Common Criteria Portal](https://www.commoncriteriaportal.org).

If your environment is not compliant with
EAL4+, NSX will raise alarms. For more
information about the alarms, see the "Security Compliance Events" section in [NSX Event
Catalog](https://docs.vmware.com/en/VMware-NSX-Event-Catalog/index.html).

NSX supports the following security functional requirements:

| Requirement | Description | Auditable |
| --- | --- | --- |
| FAU\_GEN.1 | Audit data generation | Yes |
| FAU\_SAR.1 | Audit review | No |
| FAU\_STG.1 | Protected audit trail storage | No |
| FCS\_CKM.1/TLS | Cryptographic key generation (for asymmetric keys) | No |
| FCS\_COP.1/TLS.HMAC | Cryptographic operation (hashing) | No |
| FCS\_COP.1/TLS | Cryptographic operation (TLS) | No |
| FCS\_CKM.2/TLS | Cryptographic key distribution (TLS) | Yes |
| FCS\_CKM.4 | Cryptographic key destruction | No |
| FCS\_RNG.1/OSSL | Random number generation (OpenSSL) | No |
| FCS\_RNG.1/BC | Random number generation (Bouncy Castle) | No |
| FDP\_IFC.1 | Subset information flow control | No |
| FDP\_IFF.1 | Simple security attributes | Yes |
| FIA\_AFL.1 | Authentication failure handling | Yes |
| FIA\_SOS.1 | Verification of secrets | Yes |
| FIA\_UAU.2 | User authentication before any action | Yes |
| FIA\_UID.1 | Timing of identification | Yes |
| FMT\_SMR.1 | Security roles | Yes |
| FMT\_SMF.1 | Specification of management functions | Yes |
| FMT\_MOF.1 | Management of security functions behavior | No |
| FMT\_MSA.1 | Management of security attributes | No |
| FMT\_MSA.3 | Static attribute initialisation | No |
| FPT\_TDC.1 | Inter-TSF basic TSF data consistency | Yes |
| FTP\_ITC.1 | Inter-TSF trusted channel | Yes |

For each requirement, events that are
auditable will be logged. For more information about event logging, see [Log Messages and Error Codes](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/log-messages-and-error-codes.html#GUID-df9e6850-3d60-4e76-8249-c80181dad07b-en).