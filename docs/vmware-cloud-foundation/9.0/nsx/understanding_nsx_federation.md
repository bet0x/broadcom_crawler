---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/overview-of-federation/understanding-federation.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Understanding NSX Federation
---

# Understanding NSX Federation

In NSX Federation, you make configuration changes on the active Global Manager. The active Global Manager then synchronizes the changes with the relevant Local Managers and the standby Global Manager, if you have one. Local Managers also sync some information with each other and to the Global Manager.

## Making Changes on Global Manager

The Global Manager provides a user interface similar to the NSX Manager interface.

If you choose, you can configure all objects on the Global Manager, independent of span.

The Global Manager syncs a configuration with a Local Manager only if the configuration is relevant to that location. For example, if you create a tier-0 gateway and add it to Location 1, Location 2, and Location 3, the configuration gets synchronized with all three Local Managers. Local Managers can only synchronize once with Global Manager during a configuration import.

If you have a standby Global Manager, the configurations synchronize between the active Global Manager and the standby Global Manager.

![Shows a Global Manager syncing configurations with a Standby Global Manager and to three Local Manager locations connected by a tier-0 gateway.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a534871e-b7da-4790-9bd1-236dd369cb23.original.png)

If the tier-0 gateway is added only to Location 1 and Location 2, the configuration is not synced with Location 3.

![Shows a Global Manager syncing with its Standby Global Manager and only relevant Local Managers connected to its tier-0 gateway.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/cc997a81-5b91-4747-b076-4a2511cbd7d4.original.png)

## Making Changes on Local Managers

To create objects on a specific Local Manager, you use that Local Manager. These objects do not sync with the active Global Manager or any other Local Managers.

![Shows a user making UI changes on a Local Manager in Location 1 that do not get synced with the other Global Managers or Local Managers.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b90bfeec-bcea-41d7-9acd-24a115c098ab.original.png)

## Realizing Global Manager Changes on Local Managers

The Global Manager validates change against the Global Manager and the Local Manager configurations. When a Local Manager receives a configuration from the Global Manager, it realizes the configuration in the fabric nodes of that Local Manager. During this realization, errors or conflicts might get detected. To monitor configuration flow, use the NSX Federation monitoring dashboard. See [Monitoring NSX Federation Locations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui/monitoring-nsx-federation-locations.html#GUID-89b5803a-0ec9-4324-9867-7ffef1e8c6a0-en) for details.

For example, you can create a tier-0 gateway from Global Manager, and then from a Local Manager you can create and attach a tier-1 gateway to the tier-0 gateway.

![Shows a Global Manager tier-0 gateway stretched across two locations connected to a Local Manager tier-1 gateway located in Location 1.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/2e5114a0-9dca-4fd7-a010-4d30c82bd4f9.original.png)

Because Local Managers now sync their configurations to the Global Manager, the Global Manager context the tier-0 gateway now appears to be connected. You can delete the tier-0 gateway from the Global Manager, and this change gets synchronized to the Local Managers. When the changes in each location get realized, the following occurs:

- The tier-0 gateway might get deleted from the Local Manager in Location 2.
- The tier-0 gateway might get deleted from the Local Manager in Location 1.
- The tier-0 gateway gets marked for deletion on the Global Manager.

When the tier-0 disconnects from the tier-1 in Location 1, the tier-0 gets deleted from Global Manager.

Most problems are displayed on the user interface. You can also display problems using these API calls.

- On Global Manager:

  ```
  GET /global-manager/api/v1/global-infra/realized-state/alarms
  ```
- On Local Manager:

  ```
  GET /policy/api/v1/infra/realized-state/alarms
  ```