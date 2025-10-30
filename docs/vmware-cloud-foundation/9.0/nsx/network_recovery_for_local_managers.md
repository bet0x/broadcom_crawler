---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/working-with-site-recovery-manager-and-federation/perform-network-recovery.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Network Recovery for Local Managers
---

# Network Recovery for Local Managers

If a Local Manager is lost, you can recover networking configurations from it using
the auto-detected Network Recovery option in the Global Manager.

You must have at least one stretched
tier-0 or tier-1 gateway set up designating a Location Manager as primary. The loss
of this primary Location Manager for the tier-0 or tier-1 gateway triggers the
option of network recovery in the Global Manager.

- The Global Manager detects the
  loss of connection and prompts you to perform Network
  Recovery.
- In the first step of recovery,
  you recover the tier-0 gateway. You can change the preferred primary
  location if you want it to be different from the one you set in the fallback
  preference.
- In the second step, you select
  a preferred primary location for tier-1 gateways that have a subset of the
  span of the locations covered by the tier-0 network. The preferred primary
  location for such tier-1 gateways would be different from tier-0 gateways
  and you must either accept the fallback preference established by the tier-0
  gateway, or elect not to move the gateway.
- In the final step, you can view
  the list of networking constructs that cannot be recovered because they do
  not have a secondary location configured.

If you have a tier-0 and tier-1
gateway set up using a Location Manager as primary, but the tier-0 and
tier-1 gateway do not have any services attached to them, for example,
tier-0 and tier-1 without NAT and firewall, then the data plane traffic
still works after the loss of the primary Location Manager. For
tier-0/tier-1 configuration without service, Network Recovery is not
mandatory for the recovery of data plane, even though the Network Recovery
option appears in the Global Manager.

1. From your browser, log in with
   admin privileges to the active Global Manager at
   https://<global-manager-ip-address>.
2. Select SystemLocation Manager.
3. A banner appears on this page
   noting the location that is down. Click Network Recovery
   on the banner and start the workflow for Location Disaster
   Recovery in the following steps.
4. Tier-0
   Gateways: For each tier-0 gateway that has the failed location
   set as primary, you have the option to select a new primary location. This new
   primary location can be different from the fallback preference you elected when
   creating the tier-0 gateway. You can also elect to not move the tier-0 gateway.
   Click Apply Configuration for each tier-0 gateway after
   selecting a new primary location or retaining the priority set earlier.
5. Click Next.
6. Tier-1 A/S gateways are listed for recovery only if their span differs from the
   span of the tier-0 gateway. If tier-1 A/S gateways follow the same span as the
   tier-0 gateway, the same locations are selected to be primary as for tier-0
   gateways. For a different span, you can either select a different location as
   primary or elect to not move the tier-1 gateway at all.
7. After you make your selections
   for each tier-1 gateway, click Accept and
   Next to proceed.
8. Under Single Location
   Entities you can see a list of tier-0 and tier-1 gateways that
   cannot be moved to a new primary location because they exist only in the failed
   location. Click Next to proceed.

The stretched tier-0 and tier-1 gateways are moved to the new location which that you
designated as primary.

For more details, go to the [Broadcom Communities discussion forum](https://community.broadcom.com/vmware-cloud-foundation/blogs/dimitri-desmidt/2024/04/14/nsx-t-multi-location-design-guide-federation-multisite) to review the NSX Multi-Location Design Guide, section 4.4.2, Data Plane
Recovery.