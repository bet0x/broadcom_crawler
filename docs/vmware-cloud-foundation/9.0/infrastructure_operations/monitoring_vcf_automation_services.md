---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/infrastructure-operations/connect-to-data-sources/vmware-infrastructure-health/monitoring-vrealize-automation-8-x-services-using-vmware-infra-health.html
product: vmware-cloud-foundation
version: 9.0
section: Infrastructure Operations
breadcrumb: Infrastructure Operations > Monitoring VCF Automation Services
---

# Monitoring VCF Automation Services

You can monitor the health of VCF Automation version 8.x services with the VMware Infrastructure Health.

## Resources Monitored for VCF Automation

VMware Infrastructure Health collects the health of the following VCF Automation services:

- approval-service
- assessment-service
- abx-service
- etcd-service
- health-reporting-service
- ingress-ctl
- kube-dns
- kube-apiserver
- kube-controller-manager
- kube-flannel-ds
- kube-proxy
- kube-scheduler
- kubelet-rubber-stamp
- openfaas
- predictable-pod-scheduler
- tiller-deploy
- ui
- catalog-service
- cgs-service
- cmx-service
- codestream
- docker-registry
- ebs
- form-service
- hcmp-service
- identity-service
- migration-service
- no-license
- postgres
- project-service
- provisioning-service
- proxy-service
- rabbitmq-ha
- relocation-service
- tango-blueprint-service
- tango-vro
- terraform-service
- user-profile-service
- vco
- adapter-host-service
- endpoints
- lemans-resources
- lemans-gateway
- private-cloud-gateway

By default, VMware Infrastructure Health monitors all VCF Automation 8.x services. If you do not want certain VCF Automation services to be monitored, you must add the Automation services names (such as endpoints, kube-dns, ebs, etc.) in the VMware Infrastructure Health properties file under the key CAS\_SERVICE\_TO\_IGNORE.

If the VCF Automation is attached to the load balancer, activate port forwarding to monitor Automation services with VMware Infrastructure Health. Refer to [Knowledge Base](https://kb.vmware.com/s/article/82648?lang=en_US&queryTerm=82648&queryTerm=82648) for more details. Ignore these steps if the VCF Automation is a standalone node deployment.