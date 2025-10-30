---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/set-up-the-kms-cluster/set-the-default-kms-cluster-using-the-vsphere-client.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Set the Default Key Provider Using the vSphere Client
---

# Set the Default Key Provider Using the vSphere Client

You can use the vSphere Client to set the default key provider at the vCenter level.

As a best practice, verify that the Connection Status in the Key Providers tab shows Active and a green check mark.

You must set the default key provider if you do not make the first key provider the default, or if your environment uses multiple key providers and you remove the default one.

1. Navigate to vCenter.
2. Click the Configure tab.
3. Under Security, select Key Providers.
4. Select the key provider.
5. Click Set as Default.

   A confirmation dialog box appears.
6. Click Set as Default. 

   The key provider displays as the current default.