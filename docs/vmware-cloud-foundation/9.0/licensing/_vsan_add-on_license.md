---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/licensing-overview/add-on-licenses-in-vcf-9-0.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing >   vSAN Add-on License
---

# vSAN Add-on License

To be able to use an add-on license, you must first assign a primary license to your vCenter instances. Add-on licenses are available for VCF and vSphere Foundation products.

This documentation includes detailed information only about the vSAN add-on. For a full list of add-on licenses for your product, contact your sales team. For licensing information for specific add-ons read their respective documentation.

## vSAN Licensing Overview

When you purchase VCF, in addition to your VMware Cloud Foundation (cores) license you receive an equivalent vSAN entitlement for tebibytes (TiBs) of total raw physical storage. You can also purchase additional storage as a separate add-on license.

## What's New?

- You can assign a vSAN TiB license to a single vCenter or multiple vCenter instance.
- vSAN license usage is based on the storage capacity in the vSAN clusters. vSAN pools the capacity of the subscriptions that you purchased and shares the allocated capacity between multiple vSAN clusters using the vSAN TiB license.
- You do not need a separate license or subscription for vSAN witness. You can deploy as many vSAN witness appliances as required. vSAN witness may not be used to run workloads not related to vSAN witness.

## vSAN TiB License

When you assign a vSAN TiB license to vCenter , the vSAN license is automatically applied to all the vSAN clusters that are managed by the vCenter . To calculate the capacity that you need for your vSAN environment, you must determine enough TiB licenses required for the total physical device capacity in TiBs on all the ESX hosts in each vSAN cluster.

The vSAN clusters reflect the total raw storage capacity available. For more information about calculating the license capacity that you need for your environment, see the Broadcom knowledge base article [95927](https://knowledge.broadcom.com/external/article?legacyId=95927).

If you have a bare metal host as a vSAN witness, perform the following:

1. Log in to the witness host.
2. Run the following command:

   ```
   esxcli vsan witness license set --enable true
   ```
3. Reboot the witness host.

## vSAN License Capacity in VMware Cloud Foundation

If you have a vSAN cluster with 3 ESX hosts, 1 CPU per host, and each host has 6 physical cores per CPU, you must purchase the subscription capacity of 16 cores per CPU as it is the required minimum license capacity. For each VCF cores that you purchase, you receive 1 TiB of vSAN capacity. With a total of 48 (3 \* 1 \* 16) physical cores per VCF cluster, you receive 48 TiB vSAN capacity. Similarly, with a total of 144 (3 \* 2 \* 24) physical cores per VCF cluster, you receive 144 TiB vSAN capacity.

| Number of ESX hosts (in vSAN cluster) | CPUs per ESX Host | Cores per CPU | Number of Core License | Entitled vSAN Capacity (TIB) |
| --- | --- | --- | --- | --- |
| 3 | 1 | 6 (minimum 16 cores required) | 48 | 48 |
| 3 | 2 | 24 | 144 | 144 |

You need to purchase vSAN add-on licenses if you need additional capacity. For capacity larger than the total entitled vSAN capacity in tebibytes, you can purchase additional vSAN capacity. When you purchase additional capacity, you receive a vSAN license.

The license use of vSAN is recalculated and updated in the following cases:

- If you assign a new license to the vSAN cluster
- If you add a new host to the vSAN cluster
- If a host is removed from the cluster
- If the total number of TiBs in a cluster changes

## vSAN License Capacity in VMware vSphere Foundation

With the VMware vSphere Foundation license, you receive 0.25 tebibyte (TiB) of vSAN storage per vSAN host physical core.

To calculate the capacity that you need for your vSAN environment, you need the total number of licensed CPU cores for each CPU on all the ESX hosts in your environment. For example, consider a vSAN cluster with 3 ESX hosts, 1 CPU per host, and each host has 8 physical cores per CPU. You can use up to 0.25 TiB of included vSAN storage per vSAN host physical core. You must purchase a vSphere Foundation license with the subscription capacity of 16 cores per CPU because it is the required minimum license capacity. With a total of 48 (3 \* 1 \* 16) physical cores per CPU, you receive 12 TiBs (0.25 TiB \* total cores in the vSAN cluster) capacity. Similarly, With a total of 128 (4 \* 2 \* 16) physical cores per CPU, you receive 32 TiBs capacity.

| Number of ESX hosts (in vSAN cluster) | CPUs per ESX Host | Cores per CPU | Number of Core License | Entitled vSAN Capacity (TiB) |
| --- | --- | --- | --- | --- |
| 3 | 1 | 8 (minimum 16 cores required) | 48 | 12 |
| 4 | 2 | 16 | 128 | 32 |

The 0.25 Tib per vSAN host physical core of license capacity pools with any vSAN capacity from any other add-on or VCF purchases. You can use this capacity to license the vSAN clusters in their vCenter instances, regardless of whether the capacity is more or less than 0.25 Tib per core.