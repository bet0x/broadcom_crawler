---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/uploading-vsan-support-bundle.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Uploading a vSAN Support Bundle
---

# Uploading a vSAN Support Bundle

You can upload a vSAN support bundle so VMware service personnel can analyze the diagnostic information.

Broadcom Technical Support routinely requests diagnostic information from your vSAN cluster when a support request is addressed. The support bundle is an archive that contains diagnostic information related to the environment, such as product specific logs, configuration files, and so on.

The log files, collected and packaged into a zip file, include the following:

- vCenter support bundle
- Host support bundle

The host support bundle in the cluster includes the following:

```
["Userworld:HostAgent", "Userworld:FDM",
 "System:VMKernel", "System:ntp", "Storage:base", "Network:tcpip",
 "Network:dvs", "Network:base", "Logs:System", "Storage:VSANMinimal",
 "Storage:VSANHealth", "System:BaseMinmal", "Storage:VSANTraces"]
```

vSAN performs an automated upload of the support bundle, and does not allow you to review, obfuscate, or otherwise edit the contents of your support data prior to it being sent to VMware. vSAN connects to the FTP port 21 or HTTPS port 443 of the target server with the domain name vmware.com, to automatically upload the support bundle.

Data collected in the support bundle may be considered sensitive. If your support data contains regulated data, such as personal, health care, or financial data, you may want to avoid uploading the support bundle.

1. Right-click the vSAN cluster in the vSphere Client.
2. Choose menu vSAN > Upload support bundle...
3. Enter your service request ID and a description of your issue.
4. Click Upload.