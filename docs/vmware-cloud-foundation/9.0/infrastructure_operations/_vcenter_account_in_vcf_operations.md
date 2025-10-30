---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations >   vCenter Account in VCF Operations
---

# vCenter Account in VCF Operations

The vCenter account connects VCF Operations to vCenter instances. You collect data and metrics from those vCenter instances, monitor them, and run actions on them.

VCF Operations evaluates the data in your environment, identifying trends in object behavior, predicting possible problems and future capacity for objects in your system based on those trends, and alerting you when an object exhibits defined symptoms.

## Configuring the vCenter Account

You can configure a vCenter account in VCF Operations to connect your VCF Operations environment to your vCenter instances.

## How Adapter Credentials Work

The vCenter credentials that you use to connect VCF Operations to a vCenter instance, determines what objects VCF Operations monitors. Ensure that you configure adapters and users correctly, and to avoid some of the following issues.

- If you configure the adapter to connect to a vCenter instance with credentials that have permission to access only one of your three ESX hosts, every user who logs in to VCF Operations sees only the one ESX host, even when an individual user has privileges on all three of the ESX hosts in the vCenter.
- If the provided credentials have limited access to objects in the vCenter, even VCF Operations administrative users can run actions only on the objects for which the vCenter credentials have permissions.
- If the provided credentials have access to all the objects in the vCenter, any VCF Operations user who runs actions is using the VCF Operations credentials.

## Controlling User Access to Actions

Use the vCenter adapter to run actions on vCenter from VCF Operations. If you choose to run actions, you must control user access to the objects in your vCenter environment. You control user access for local users based on how you configure user privileges in VCF Operations. If users log in using their vCenter account, then the way their account is configured in vCenter determines their privileges.

For example, you might have a vCenter user with a read-only role in vCenter. If you give this user the VCF OperationsPower User role in vCenter rather than a more restrictive role, the user can run actions on objects because the adapter is configured with credentials that has privileges to change objects. To avoid this type of unexpected result, configure local VCF Operations users and vCenter users with the privileges you want them to have in your environment.

To configure a vCenter account, see [Configuring a vCenter Account in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vsphere/configuring-a-vcenter-server-cloud-account-in-vrealize-operations.html#GUID-8e1e3efc-9524-4684-a8a9-62563b96fe84-en).