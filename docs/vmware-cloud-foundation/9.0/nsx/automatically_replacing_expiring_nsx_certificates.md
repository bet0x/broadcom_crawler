---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/automatically-replacing-expiring-certificates.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Automatically Replacing Expiring NSX Certificates
---

# Automatically Replacing Expiring NSX Certificates

Some self-signed appliance certificates are replaced before their expiry.

A background task in the NSX Manager scans the list of certificates stored in Corfu and identifies all the appliance certificates that have expired or are due to expire within a period of 31 days. This task then constructs and runs a batch certificate replace operation that will replace all of the expired or the expiring certificates.

The automatic replacement task will not perform replacements in case of the following conflicting operations:

- Backup & restore
- Upgrade
- Rollback
- Addition of a new transport node (host or edge)
- Addition of a new manager node

Note that APH\_TN or CCP certificates are not replaced during the automatic certificate replacement.

You can also manually initiate the replacement of expiring certificates by running the following API.

POST /api/v1/trust-management/certificates/action/renew-appliance-certificates

By default, the automated certificate replacement performs its first check for expired certificates 10 minutes after proton startup and then repeats the check after every 24 hours

## Turning off Automatic Certificate Replacement

By default, the automatic certificate replacement policy is enabled. To turn off the replacement policy, add the following fields to the /policy/api/v1/infra/security-global-config API.

```
PUT /policy/api/v1/infra/security-global-config
{
    ... (existing properties)
    "automatic_appliance_certificate_replacement_enabled": false,
    "automatic_appliance_certificate_replacement_lead_time": 31  # in days
}
```