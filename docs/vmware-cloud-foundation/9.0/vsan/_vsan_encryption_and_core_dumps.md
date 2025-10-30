---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/vsan-encryption-and-core-dumps.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN >   vSAN Encryption and Core Dumps
---

# vSAN Encryption and Core Dumps

If your vSAN cluster uses data-at-rest encryption, and if an error occurs on the ESX host, the resulting core dump is encrypted to protect data.

Core dumps that are included in the vm-support package are also encrypted.

Core dumps can contain sensitive information. Follow your organization's data security and privacy policy when handling core dumps.

## Core Dumps on ESX Hosts

When an ESX host crashes, an encrypted core dump is generated and the host reboots. The core dump is encrypted with the host key that is in the ESX key cache. What you can do next depends on several factors.

- In most cases, vCenter retrieves the key for the ESX host from the KMS and attempts to push the key to the ESX host after reboot. If the operation is successful, you can generate the vm-support package and you can decrypt or re-encrypt the core dump.
- If vCenter cannot connect to the ESX host, you might be able to retrieve the key from the KMS.
- If the host used a custom key, and that key differs from the key that vCenter pushes to the ESX host, you cannot manipulate the core dump. Avoid using custom keys.

## Core Dumps and vm-support Packages

When you contact Broadcom Technical Support because of a serious error, your support representative usually asks you to generate a vm-support package. The package includes log files and other information, including core dumps. If support representatives cannot resolve the issues by looking at log files and other information, you can decrypt the core dumps to make relevant information available. Follow your organization's security and privacy policy to protect sensitive information, such as host keys.

## Core Dumps on vCenter Systems

A core dump on a vCenter system is not encrypted. vCenter already contains potentially sensitive information. At the minimum, ensure that the vCenter is protected. You also might consider turning off core dumps for the vCenter system. Other information in log files can help determine the problem.