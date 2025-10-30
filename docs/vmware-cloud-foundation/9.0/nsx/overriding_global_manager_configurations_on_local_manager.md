---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overriding-gm-config-on-lm.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Overriding Global Manager Configurations on Local Manager
---

# Overriding Global Manager Configurations on Local Manager

When you create an object from Global Manager, the same configuration is propagated to all relevant locations.
You can override some Global Manager
configurations on a Local Manager.

To override a configuration, click the three
dots menu (![Three vertical dots](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) next to the configuration, and click Edit. If
the Edit menu item is dimmed, you cannot override this
configuration.

If a configuration is overridden, you see
this icon in the status column on both Global Manager and Local Manager:
![Shows icon with three lines in a red box](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/aaa92a7e-add3-419b-b93f-2e2f7c01b0e4.original.png).

To remove an override, click the three dots
menu (![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/7504cc2e-f1d9-49a4-8e3d-c53a8d1e944b.original.png)) next to the configuration, and click Revert.
The configuration from Global Manager is
restored.

If you override a configuration from
Global Manager on a Local Manager, and then you delete the configuration
from the Global Manager, the configuration
persists on the Local Manager. When you
revert the configuration, the configuration is deleted from Local Manager.

You can get a list of all configurations that
have been overridden. Make this API request to the Global Manager: GET
https://<global-mgr>/global-manager/api/v1/global-infra/overridden-resources.

## Gateway Configurations

Gateway configurations are found in NetworkingTier-0 Gateways.

You can modify the following gateway
configurations:

- Tier-0 Gateway BGP
  Configuration
- Tier-0 Gateway Interfaces

## Profile Configurations

Profile configurations on Global Manager are used in all Local Managers.
There is no span setting for a profile configuration.

You can override the following global
profile configurations from Local Manager:

- Segment Profiles: NetworkingSegmentsSegment Profiles
  - IP Discovery
    Profiles
  - MAC Discovery
    Profiles
  - QoS Profiles
  - Segment Security
    Profiles
  - SpoofGuard
    Profiles
- Networking Profiles: NetworkingNetworking Profiles
  - IPv6 DAD Profiles
  - IPv6 ND Profiles
  - Gateway QoS
    Profiles
  - BFD Profiles
- Context Profiles: Inventory Profiles
- Security Profiles: SecurityGeneral Settings Firewall
  - Firewall Session Timer
    Profile
  - Edge Gateway Flood
    Protection Profiles
  - Firewall Flood
    Protection Profiles
  - DNS Security
    Profiles
  - CPU and Memory
    Threshold Profiles are API only:
    - Override with
      PUT/PATCH
      https://<local-manager>/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/<id>?override=true.
    - Revert with
      DELETE
      https://<local-manager>/policy/api/v1/global-infra/settings/firewall/cpu-mem-thresholds-profiles/<id>?override=true.