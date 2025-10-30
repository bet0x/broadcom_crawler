---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/managing-proactive-hardware/processing-hardware-failures.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Processing Hardware Failures
---

# Processing Hardware Failures

PHM checks for HSM generated hardware failure events every 10 minutes (600 seconds).

You can customize the time interval using the vSAN configuration file.

1. Log in to vCenter console as root.
2. Open the /usr/lib/vmware-vsan/VsanVcMgmtConfig.xml file.
3. Set the interval value using healthUpdatePollIntervalInSeconds xml tag in seconds.
4. Restart the vSAN Health service using the command service-control --restart vmware-vsan-health.

PHM uses these events to generate alarms, which appears in the vSAN Skyline Health. For more information on the vSAN Skyline Health events, see the Broadcom knowledge base article [367770](https://knowledge.broadcom.com/external/article?articleNumber=367770).