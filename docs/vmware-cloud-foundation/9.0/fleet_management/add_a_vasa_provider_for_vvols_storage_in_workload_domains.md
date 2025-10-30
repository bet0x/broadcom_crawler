---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/configuring-managemnet-appliances/add-a-vasa-provider.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Add a VASA Provider for vVols Storage in Workload Domains
---

# Add a VASA Provider for vVols Storage in Workload Domains

To use vVols storage for workload domains, you must add a VASA provider.

Before you add the VASA provider details in the VCF Operations console, ensure that you have set up the VASA provider. For information about setting up a VASA provider, see the vSphere Storage documentation.

Starting with VMware Cloud Foundation 9.0 and vSphere Foundation 9.0, the vSphere Virtual Volumes capability, also known as vVols, is deprecated and will be removed in a future release of VMware Cloud Foundation and vSphere Foundation. Support for vSphere Virtual Volumes will continue for critical bug fixes only for versions of vSphere 8.x, VMware Cloud Foundation and vSphere Foundation 5.x, and other supported versions until end-of-support for the respective release.

1. In VCF Operations, select AdministrationSDDC ManagerStorage Settings.
2. Click Add VASA Provider.
3. Enter a name for the VASA provider.
4. Enter a URL for the VASA provider.
5. Enter VASA provider user credentials.
6. Enter VASA provider storage container details.
7. Click Save.

   You can add additional VASA user credentials and storage containers.