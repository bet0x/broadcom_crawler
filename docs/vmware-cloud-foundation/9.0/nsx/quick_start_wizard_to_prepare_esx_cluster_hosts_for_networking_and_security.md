---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-transport-nodes/quick-start-wizard-to-prepare-clusters-for-networking-and-security.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Quick Start Wizard to Prepare ESX Cluster hosts for Networking and Security
---

# Quick Start Wizard to Prepare ESX Cluster hosts for Networking and Security

Using the Quick Start wizard, you can configure ESX clusters for Networking and Security.

Starting with NSX 4.2.0, NSX supports only the Networking & Security deployment mode for preparing compute clusters with ESX hosts configured as transport nodes. This change delivers improvements in functionality and flexibility.

Below are the supported deployment modes:

- Pre-4.2.0: NSX supported two deployment modes:
  - Security-Only: Focused solely on security services.
  - Networking & Security: Combined networking and security services.
- NSX 4.2.0 and Later:
  - Only the Networking & Security deployment mode is supported, consolidating the previous options into a deployment mode.

  The single deployment mode allows you to configure the Distributed Firewall (DFW) on Distributed Virtual Portgroups (DVPGs) alongside network virtualization features on the same ESX host.

Default Behavior:

- Fresh NSX 4.2.0 Installation:
  - NSX on DVPG is disabled by default.
  - The cluster is automatically prepared in Networking & Security deployment mode.
  - NSX on DVPG can be manually enabled after cluster preparation.
- Upgrade Scenario (From Pre-4.2.0 Networking & Security to 4.2.0):
  - DFW on DVPG is disabled on the upgraded cluster by default.
  - NSX on DVPG can be manually enabled post-upgrade.
- Upgrade Scenario (From Pre-4.2.0 Security-Only to 4.2.0):
  - The upgraded cluster is automatically prepared for both Networking & Security services.
  - NSX on DVPG is automatically enabled.

If you activate NSX on a cluster that was earlier configured with Security-Only feature, you can now implement the following NSX features on it:

- You can create NSX segments for the clusters you created in vCenter.
- You can edit the auto created Transport Node Profile before applying it to the discovered clusters.
- You can enable NSX Overlay for the discovered clusters.
- You can configure the following NSX features on the discovered clusters using NSX UI/API.
  - Spoof Guard
  - Switch Security
  - Mac Management
  - IP Discovery
  - TraceFlow
  - ENS
  - Advanced Security features, such as DFW and IDS/IPS

Ensure that ESX host version is v7.0.3 or later if you want to use the same VDS to prepare clusters for both the use cases - Security-only or Networking and Security. To avoid issues post cluster nodes preparation, upgrade ESX host to v7.0.3 or later before preparing clusters using the same VDS.