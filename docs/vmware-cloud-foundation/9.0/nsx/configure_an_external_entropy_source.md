---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/configure-an-external-entropy-source.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Configure an External Entropy Source
---

# Configure an External Entropy Source

You can configure an external entropy source to generate random numbers for cryptographic operations. The external entropy source can be used to satisfy one of the requirements of EAL4.

- vSphere 8.0 or later.
- The ESX host where NSX Manager is running is configured to activate the correct entropy source. For more information, see Controlling ESX Entropy.

After the ESX host is configured with an external entropy source, NSX will automatically obtain entropy data from ESX. No configuration on NSX is required.

The external entropy will impact the functions related to random number generation and cryptographic operation mentioned in Common Criteria Compliance.

1. Log in to vCenter from vSphere Client.
2. Browse to the NSX Manager VM.
3. Shut down the VM.
4. Right-click the VM and click Edit Settings.
5. Select VM Options.
6. Click Advanced and click Edit Configuration.
7. Set the isolation.tools.getEntropy.disable parameter to FALSE.
8. Click OK.