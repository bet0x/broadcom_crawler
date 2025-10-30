---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/set-up-network-configuration-on-the-reference-host.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Set Up Network Configuration on the Reference Host
---

# Set Up Network Configuration on the Reference Host

On the reference host, a standard switch with a VMkernel adapter is created to set up
the network configuration on ESX.

This network configuration is captured in
the host profile which is extracted from the reference host. During a stateless
deployment, the host profile replicates this network configuration setting on each
target host.

1. On the ESX host, configure a vSphere Standard
   Switch (VSS) or Distributed Virtual switch (DVS) by adding a VMkernel
   adapter.
2. Verify that the newly added VSS/DVS switch is displayed in the VMkernel
   adapters page.

   ![The VMkernel Adapters page displays the added vmkernels to a VSS or DVS
                               switch.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/e1a3a022-818a-444a-bc00-de9ec4607edd.original.png)

Configure the Reference Host as a
Transport Node in NSX. See [Configure the Reference Host as a Transport Node in NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-profile-integration-with-nsx/auto-deploy-stateless-cluster/configure-the-reference-host-as-a-transport-node-in-nsx.html#GUID-43f1b620-3f58-4915-b770-189e184aa24f).