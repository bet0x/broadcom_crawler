---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/monitoring-vsan-skyline-health/proactive-tests-on-vsan-cluster.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Proactive Tests on vSAN Cluster
---

# Proactive Tests on vSAN Cluster

You can initiate a health test on your vSAN cluster to verify that the cluster components are working as expected.

You must not conduct the proactive test in a production environment as it creates network traffic and impacts the vSAN workload.

Run the VM creation test to verify the vSAN cluster health. Running the test creates a virtual machine on each host in the cluster. The test creates a VM per each ESX host in the vSAN cluster. The VM gets deleted if the test is successful. VM creates and and deletes tasks that you can monitor on the task console. If the VM creation and deletion tasks are successful, assume that the cluster components are working as expected and the cluster is functional. The test results shows the last run date and time with their status. You can also view the list of all the ESX hosts where the test was run.

Run the Network performance test to detect and diagnose connectivity issues, and to make sure the network bandwidth between the ESX hosts supports the requirements of vSAN.It also allows to select Enable Network diagnostic mode which creates a ramdisk on a host to collect and save network metrics generated during the test. The test is performed between the ESX hosts in the cluster. It verifies that the network bandwidth between ESX hosts, and reports a warning if the bandwidth is less than 850Mbps. You can run the proactive test at a maximum speed limit of 10Gbps. In vSAN ESA, the proactive test reports error when the result is zero bps and the Health Status displays the test results as info when the result is a non-zero number.

To access a proactive test, select your vSAN cluster in the vSphere Client, and click the Monitor tab. Click vSAN > Proactive Tests.