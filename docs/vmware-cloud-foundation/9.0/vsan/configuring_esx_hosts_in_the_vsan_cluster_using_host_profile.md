---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/administering-vmware-vsan/expanding-and-managing-a-vsan-cluster/expanding-a-vsan-cluster/configuring-hosts-in-the-vsan-cluster-using-host-profile.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Configuring ESX Hosts in the vSAN Cluster Using Host Profile
---

# Configuring ESX Hosts in the vSAN Cluster Using Host Profile

When you have multiple ESX hosts in the vSAN cluster, you can use a host profile of an existing vSAN host to configure the ESX hosts in the vSAN cluster.

- Verify that the ESX host is in maintenance mode.
- Verify that the hardware components, drivers, firmware, and storage I/O controllers are listed in the Broadcom Compatibility Guide at <https://compatibilityguide.broadcom.com/>.

The host profile includes information about storage configuration, network configuration, and other characteristics of the ESX host. If you are planning to create a vSphere cluster with many ESX hosts, use the host profile feature. Host profiles enable you to add more than one ESX host at a time to the vSAN cluster.

1. Create an ESX host profile.
   1. Navigate to Policies and Profiles, then click Host Profiles in the vSphere Client.
   2. Click the Extract Host Profile icon.
   3. On the Select the host dialog, select the ESX host you intend to use as the reference ESX host and click Next.

      The selected ESX host must be an active host.
   4. On the Name and description dialog, enter a name for the new profile and click Finish.
   5. Review the summary information for the new host profile and click Finish.
2. Attach the ESX host to the intended host profile.
   1. From the Profile list in the Host Profiles view, select the host profile to be applied to the ESX host.
   2. Click the Attach/Detach Hosts and clusters to a host profile icon (![Attach the host profile](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6da1cf95-8c92-4ae1-984b-c552f7d22bef.original.png)).
   3. Select the host from the expanded list and click Attach to attach the host to the profile. 

      The host is added to the Attached Entities list.
   4. Click Next.
   5. Click Finish to complete the attachment of the host to the profile.
3. Detach the referenced vSAN host from the host profile. 

   When a host profile is attached to a cluster, the host or hosts within that cluster are also attached to the host profile. However, when the host profile is detached from the cluster, the association between the host or hosts in the cluster and that of the host profile remains intact.

   1. From the Profile List in the Host Profiles view, select the host profile to be detached from a host or cluster.
   2. Click the Attach/Detach Hosts and clusters to a host profile icon (![Attach the host profile](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/6da1cf95-8c92-4ae1-984b-c552f7d22bef.original.png)).
   3. Select the host or cluster from the expanded list and click Detach.
   4. Click Detach All to detach all the listed hosts and clusters from the profile.
   5. Click Next.
   6. Click Finish to complete the detachment of the host from the host profile.
4. Verify the compliance of the vSAN host to its attached host profile and determine if any configuration parameters on the host are different from those specified in the host profile. 
   1. Navigate to a host profile. 

      The Objects tab lists all host profiles, the number of hosts attached to that host profile, and the summarized results of the last compliance check.
   2. Click the Check Host Profile Compliance icon (![Check the compliance](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/f1881d15-6db5-4542-8189-6e86f7586869.original.png)). 

      To view specific details about which parameters differ between the host that failed compliance and the host profile, click the Monitor tab and select the Compliance view. Expand the object hierarchy and select the non-compliant host. The parameters that differ are displayed in the Compliance window, below the hierarchy.

      If compliance fails, use the Remediate action to apply the host profile settings to the host. This action changes all host profile-managed parameters to the values that are contained in the host profile attached to the host.
   3. To view specific details about which parameters differ between the host that failed compliance and the host profile, click the Monitor tab and select the Compliance view.
   4. Expand the object hierarchy and select the failing host. 

      The parameters that differ are displayed in the Compliance window, below the hierarchy.
5. Remediate the host to fix compliance errors. 
   1. Select the Monitor tab and click Compliance.
   2. Right-click the host or hosts to remediate and select All vCenter ActionsHost ProfilesRemediate. 

      You can update or change the user input parameters for the host profiles policies by customizing the host.
   3. Click Next.
   4. Review the tasks that are necessary to remediate the host profile and click Finish.

   The host is part of the vSAN cluster and its resources are accessible to the vSAN cluster. The host can also access all existing vSAN storage I/O policies in the vSAN cluster.