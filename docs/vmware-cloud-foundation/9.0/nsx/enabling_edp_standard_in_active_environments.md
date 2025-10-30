---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/host-switches/enhanced-datapath/enabling-edp-standard-in-active-environments.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enabling EDP Standard in Active Environments
---

# Enabling EDP Standard in Active Environments

Manually enable Enhanced Datapath Standard (without data path impact) on clusters that are **not** configured to use vSphere Configuration Profiles (VCP). To enable EDP Standard in VCP-enabled clusters, simply change the mode using the Transport Node Profile or Workload Do,main network settings. VCP-enabled clusters do not require the procedure below.

- Create a Transport Node Profile (TNP) with EDP Standard enabled (required), taking note of the existing Transport Node Profile settings.

  - Create an identical TNP replacement with the mode set to Enhanced Datapath - Standard.

    This new Transport Node Profile will be used to enable EDP Standard in active environments.

    Refer to [Adding a Transport Node Profile](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/add-a-transport-node-profile.html) for general TNP creation steps.
- Configure the vCenter to allow vMotion during mode transitions:

  config.vpxd.network.allowVmotionBetweenENSModes=true

  Use this setting in the vCenter where the compute cluster or TNC exists. This configuration ensures VC doesn't block any mode changes during the vMotion of workload VM's from one host to another.
- Reset previous performance configurations (required only if configurations exist). EDP Standard is designed to provide the best performance outcomes with default configurations. It’s predecessor (the default Standard mode) may host network optimizations like the following:

  ```
  esxcli system module parameters set -p "DRSS=X, RSS=Y"
  esxcli system settings advanced set -o /Mem/ShareCOSBufSize -i 32
  esxcli system settings advanced set -i 1 -o /Net/NetSchedHClkMQ
  esxcli system settings advanced set -o /Net/NetNetqLoadAvgByteCountShift -i 50
  ```

  Use the following API call after step 1, while each host is in maintenance mode, to reset any host performance settings previously configured.

  PUT https://<NSXMGR-IP>/policy/api/v1/infra/host-switch-profiles/<HPPName>

  ```
  {
     "high_performance_configs": [],
     "auto_config": 0,
     "resource_type": "PolicyHighPerformanceHostSwitchProfile"
  }
  ```

  Replace <NSXMGR-IP> with the NSX Manager IP address, and <HPPName> with a High Performance Profile identified based on your naming convention. Refer to the NSX API Guide for general information using the NSX Rest API.

To enable EDP standard in active environments, use the following procedure. The procedure below uses ESX maintenance mode to transition the mode without any impact to the network forwarding path.

You can enabling EDP Standard using the “enable\_uens” script. The script can be used instead of the manual steps in the procedure below.

The script is located in **/opt/vmware/migration-coordinator-tomcat/bin/uens-adoption/config** and can be executed from the same location. The script can be used on a single cluster, and will take its inputs from a required JSON file that you have prepared in advance. You can follow detailed instructions provided in the readme file. To run the script follow these steps:

1. Use SSH to access the NSX Manager.
2. Change to the /opt/vmware/migration-coordinator-tomcat/bin/uens-adoption/config/ directory.
3. Execute the python script, replacing the file path with the actual JSON location:

   python enable\_ens.py -f /opt/temp/sample.json

1. Open the vCenter and locate the first Transport Node ESX Host and place the ESX host in Maintenance Mode.

   Refer to [Place a Host in Maintenance Mode](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-upgrade-8-0/upgrading-esxi-hosts-upgrade/how-to-upgrade-hosts-by-using-esxcli-commands-upgrade/place-a-host-in-maintenance-mode-upgrade.html).
2. Open the NSX Manager, and navigate to SystemConfiguration - FabricHosts .
3. In the Clusters panel, click the Node vertical ellipsis to open the node options.

   ![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/911fbda9-71bd-40e5-835a-a1469c705f7f.original.png)
4. In the node options, click Configure NSX. In the Host details panel Click Next.

   ![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b3882d13-420b-4b73-9fb8-a4a62883c8da.original.png)
5. In the Prepare Host panel, click the vertical ellipsis and Edit the host switch.

   ![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/4d689f9d-a448-469e-a80b-7b2cad59a304.original.png)
6. Expand Advanced Configuration and change the mode to Enhanced Datapath - Standard.

   ![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/b45d813b-94b6-45b4-ad3a-424e97871dc3.original.png)

   You can verify the mode change was applied on the ESX shell with the command esxcfg-nics -e:

   ![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/1b1a57a2-a6af-468e-826f-bc2191255e28.original.png)
7. In the vCenter, exit **Maintenance Mode**.
8. Repeat the above steps for every host in the Transport Node cluster.
9. Replace the existing Transport Node Profile with the EDP Standard-enabled replacement identified in Prerequisites.
   1. Navigate to **SystemConfiguration - FabricHosts**
   2. In the Clusters panel, select the Cluster and click Configure NSX.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bcd0abda-7201-456b-9f78-71f70f558583.original.png)
   3. In the NSX Installation screen, select the new EDP Standard TNP and click **Save**.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/5578557c-df90-4a18-86f3-29043b676a07.original.png)
   4. The EDP Standard Transport Nodes become synchronized to the new EDP Standard TNP.

      ![](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/a4be7b3c-c672-44b6-8b09-896569ea615b.original.png)