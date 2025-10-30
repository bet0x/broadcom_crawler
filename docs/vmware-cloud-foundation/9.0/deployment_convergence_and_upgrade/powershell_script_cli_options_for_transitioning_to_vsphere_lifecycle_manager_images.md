---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1)/powershell-script-cli-options-for-transitioning-to-vsphere-lifecycle-manager-images.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > PowerShell Script CLI Options for Transitioning to vSphere Lifecycle Manager Images
---

# PowerShell Script CLI Options for Transitioning to vSphere Lifecycle Manager Images

A list of the all the CLI options for the PowerShell script used to transition from vSphere Lifecycle Manager baselines to vSphere Lifecycle Manager images.

You can run the script with the -Help argument to see these options.

```
PS C:\Users\Admin>.\VcfBaselineClusterTransition.ps1 -Help
```

For examples of how to use these options, see [Transition to vSphere Lifecycle Manager Images Using the PowerShell Script Command-Line Interface](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/vlcm-baseline-to-vlcm-image-cluster-transition-/transition-vlcm-baseline-clusters-to-vlcm-image-clusters-using-powercli(1)/transition-to-vsphere-lifecycle-manager-images-using-the-powershell-script-command-line-interface.html).

| Parameter | Argument | Optional/Required Argument |
| --- | --- | --- |
| -CheckTaskStatus | -TaskType SddcManagerImageUpload or -TaskType ComplianceCheck | Required |
| -Silence | Optional |
| -CheckTransitions | -ClusterName cluster\_Name  -WorkloadDomainName workload\_domain\_name | Optional |
| -Silence | Optional |
| -Connect | -JsonInput path\_to\_file | Optional |
| -ComplianceCheck | -ClusterName cluster\_Name  -SddcManagerImageName image\_name  -WorkloadDomainName workload\_domain\_name | You must provide either all of the individual arguments or use the -JsonInput argument. |
| -JsonInput path\_to\_file |
| -Parallel | Optional |
| -Silence | Optional |
| -DeleteImageFromSddcManager | -SddcManagerImageName image\_name | Required |
| -Silence | Optional |
| -DeleteTemporaryCluster | -ClusterName cluster\_Name  -VcenterName vc\_FQDN | Required |
| -Silence | Optional |
| -Disconnect | -Silence | Optional |
| -Help |  | N/A |
| -ImportImagesFromVcenter | -VcenterImageName image\_name  -VcenterName vc\_FQDN | You must provide either all of the individual arguments or use the -JsonInput argument. |
| -JsonInput path\_to\_file |
| -Parallel | Optional |
| -Silence | Optional |
| -ReviewComplianceResults | -ClusterName cluster\_Name  -WorkloadDomainName workload\_domain\_name | Optional |
| -ShowExtendedResults | Optional |
| -ShowAllClusters | Optional |
| -Silence | Optional |
| -RetryTransition | -TaskId <Task Id> | Required |
| -ShowBaselineClusters | -JsonOutput path\_to\_file | Optional |
| -Silence | Optional |
| -ShowImagesInSddcManager | -Silence | Optional |
| -ShowImagesInVcenter | -JsonOutput path\_to\_file | Optional |
| -Silence | Optional |
| -TransitionCluster | -Cluster Name cluster\_Name  -WorkloadDomainName workload\_domain\_name | You must provide either all of the individual arguments or use the -JsonInput argument. |
| -JsonInput path\_to\_file |
| -Parallel | Optional |
| -Silence | Optional |
| -Version |  | N/A |