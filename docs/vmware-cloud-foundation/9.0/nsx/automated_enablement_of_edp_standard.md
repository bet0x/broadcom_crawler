---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-datapath/automated-enablement-of-edp-standard.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Automated Enablement of EDP Standard
---

# Automated Enablement of EDP Standard

This procedure is a supplement to [Enabling EDP Standard in Active Environments](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-datapath/enabling-edp-standard-in-active-environments.html). It provides REST API based steps for the same procedure, which can be used to enable EDP Standard in active environments without impacting the data path.

Configure the vCenter:

config.vpxd.network.allowVmotionBetweenENSModes=true

Use this setting in the vCenter where the compute cluster or TNC exists. This configuration ensures the vCenter does not block any mode changes during the vMotion of workload VM's from one host to another.

This procedure is written for technical staff experienced with operational automation. Refer to the NSX REST API Guide for general information.

In the EDP context, an active environment is defined as follows:

- ESX hosts that are already running as NSX Transport Nodes in Standard mode.
- ESX hosts without NSX, but with live workloads that cannot tolerate impact.

The procedure below explains how to enable Enhanced Data Path Standard with the NSX REST API. The procedure is written using a fictional environment with the following components:

- A vLCM or VUM NSX-enabled Transport Node Cluster named “TNC1”.
- A single host or Transport Node named “TN1” within TNC1.
- TNC1 is associated with a Transport Node Profile “TNP1” I.

In the automated procedure, once a host is placed into maintenance mode, the API is used to transition HostSwitchMode=STANDARD to HostSwitchMode-ENS\_INTERRUPT.

1. Put TN1 inside the TNC1 in ESX maintenance mode.

   If applicable - apply a High Performance Profile to reset any custom network performance configurations. See the previous topic for more details.
2. Change TN1's HostSwitchMode to ENS\_INTERRUPT by calling the TN PUT API. → this will be allowed and will mark the Host as Overridden. Since the Host's are in overridden state TNP1 attached to that TNC1 will not move the HostSwitchMode back to STANDARD on TN1.
   1. API to get all transport-nodes:

      GET https://<MP\_Endpoint>/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/
   2. API to update the transport node corresponding to TN1:

      PUT https://<MP\_Endpoint>/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-transport-node-id>
   3. GET API to verify the Mode change:

      GET https://<MP\_Endpoint>/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes/<host-transport-node-id>
3. Turn off the ESX maintenance mode on TN1.
4. Perform steps 1-3 for all TN's in that TNC1 one after the other.
5. Once all TN's within the TNC1 are updated to ENS\_INTERRUPT succesfully, make a copy of TNP1 and create TNP2 with just one change to make HostSwitchMode=ENS\_INTERRUPT for TNP2.
   1. API to GET all transport-node-profiles:

      GET https://<MP\_Endpoint>/policy/api/v1/infra/host-transport-node-profiles/
   2. Fetch the TNP Id of TNP1 and GET the config:

      GET https://<MP\_Endpoint>/policy/api/v1/infra/host-transport-node-profiles/<TNP1 ID>
   3. API to create a new TNP (TNP2):

      PUT https://<MP\_Endpoint>/policy/api/v1/infra/host-transport-node-profiles/<transport-node-profile-id> to create TNP2.
6. Update (TNC PUT API) the TNP associated with TNC1 to TNP2.
   1. API to GET all transport-node-collections:

      GET https://<MP\_Endpoint>/api/v1/infra/sites/default/enforcement-points/default/transport-node-collections/
   2. API to update TNC:

      PUT https://<MP\_Endpoint>/api/v1/infra/sites/default/enforcement-points/default/transport-node-collections/<transport-node-collections-id>

      This will try to apply TNP2 with ENS\_STANDARD, but since all TN's are already on ENS\_STANDARD this is basically a no-op and all overridden TN's will have the override flag removed.