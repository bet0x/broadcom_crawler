---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/configuration-drifts-faqs.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Configuration Drifts FAQ
---

# Configuration Drifts FAQ

This topic covers some frequently asked questions about Configuration Drifts in VCF Operations.

1. What are the prerequisites for setting up Configuration Drifts?

   1. To view the prerequisites for setting up configuration drifts, please see [Managing Configuration Templates in VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/what-is-configuration-management/creating-a-configuration-template.html#GUID-5c970def-f515-4db6-b6dd-d529e5170f8b-en).
2. When does Configuration Template creation fail?

   1. Configuration Template creation can fail if the template size exceeds 9 MB. You can copy the desired state contents to a file to check the file size and ensure it is under 9 MB.
   2. Configuration Template creation can fail if a connection issues occurs between vCenter and the configuration adapter. You can check the connection status of vCenter and the configuration adapter to ensure that there is a proper connection between the two. To troubleshoot, see [Cloud Proxy Troubleshooting](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_881&appid=vcf-9-0&language=&format=rendered) and [vSphere Management Pack Issues](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcfa_112&appid=vcf-9-0&language=&format=rendered).
3. What should I do if there is an error while displaying drift details?

   1. If you encounter an error while attempting to view drift details, it may be due to connectivity issues between vCenter and the configuration adapter. To troubleshoot, see [Cloud Proxy Troubleshooting](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_881&appid=vcf-9-0&language=&format=rendered) and [vSphere Management Pack Issues](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcfa_112&appid=vcf-9-0&language=&format=rendered).
4. Why is there a mismatch in the vSphere Configuration Profiles (VCP) drift status between the vCenter Console and the VCF Operations Console?

   1. The VCP drift status in the VCF Operations Console is updated through a polling mechanism that runs every 8 hours. Wait for a few hours to allow the next data collection cycle to update the status in the VCF Operations Console.
5. Why is the Drift Report PDF generated with "No drift details available for the selected resource/resources" message?

   1. This message may appear if the Detect Drift operation has never been triggered for the selected resources. To resolve this, run the Detect Drift process on the relevant resources first, and then try downloading the report again.
6. How can I remediate a vCenter if I receive a notification indicating that it has drifted from a Configuration Template?

   1. Remediation cannot be done at the VCF Operations console at this time. You must log in to the vCenter and manually revert the drifted configurations to their original values as defined in the template to make the vCenter compliant again.
   2. If you want the drifted values to be the Configuration Template values, edit the template under Configuration Drifts to match the current configuration of the vCenter.
7. How do I troubleshoot if a vCenter Drift status is in an Error state?

   1. Check the connection between VCF Operations and vCenter to ensure that vCenter is in a Collecting state within VCF Operations. If it is not collecting, start or resume the data collection for vCenter. This will restore proper drift detection and clear the error. To troubleshoot, see [vSphere Management Pack Issues](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcfa_112&appid=vcf-9-0&language=&format=rendered).
8. How can I debug when the configuration template sync fails to and from remote repository?

   1. In the VCF Operations navigate to AdministrationControl PanelSource Control and click Test Connection to verify if connection with the Git Repository is successful or not. Ensure the connection is successful before performing any action related to configuration drifts using Git. If the test fails, check the repository URL, credentials, and network connectivity.
9. How often is the cluster drift status updated?

   1. The cluster drift status is updated once every 8 hours.