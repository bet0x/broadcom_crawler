---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/operations-and-management/testing-end-to-end-workflow-tracing.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Testing End-To-End Workflow Tracing
---

# Testing End-To-End Workflow Tracing

Network workflow tracing provides access to internal NSX workflow. Tracing helps users to analyze the logs, monitor whether the
NSX Policy Manager, CCP, and host
daemons are running properly, and optimize the network traffic where needed.

Verify that your NSX host clusters are connected to the ESX host.

The workflow tracing includes management and
configuration APIs that collect execution time, API input or output parameters, and
judgment conditions. Workflow tracing at a granular level is available in
applications such as NAT and Edge. The API enables tracing, which can be stored
locally or forwarded to a third-party distributed tracing like Jaeger.

ESX
host VM shares network information with Jaeger when an NSX segment is created. The tracing dashboard
contains the following information:

- Trace the internal traffic within the segment.
- Identify any specific operations that could affect system performance.
- Troubleshoot and analyze reported errors.

Select a destination for tracing output and add
network tracing settings to the application or machine configuration file to enable
network tracing. When network tracing is enabled, you can capture calls from
NSX Policy Manager, CCP,
and host daemons. Use end-to-end workflow tracing to connect and disconnect to VIF
and install or uninstall the transport node.

1. In the vSphere Client UI, navigate to
   the host clusters.
2. Select the VM in the datacenter.
3. Right-click and select Edit Settings from the drop-down menu.
4. For Network adapter 2, select the Connected option.

   The VM is connected to the NSX segment.
5. Open your tracing tool and view the end-to-end trace workflow.

   The trace workflow starts from the configuration
   agent to NSX NestDb, ending at
   CCP.