---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-multi-tenancy/enabling-project-context-in-nsx-edge-syslog.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Enabling Project Context in NSX Edge Syslog
---

# Enabling Project Context in NSX Edge Syslog

Log messages generated for
objects created in the NSX project contain the
project (tenant) context in a label that is appended to every log message. Such a label
matches the unique short log identifier that was defined during the project
creation.

For example, log messages that are generated
in the edge syslog for the centralized services, which are running on the tier-1 gateway
of the project, contain the project context.

By default, log messages generated in the
edge syslog for the centralized services, which are running on the tier-0/VRF gateways
that are consumed by the project, do not contain the project context. The reason is that
tier-0/VRF gateways are owned by the default space and they do not belong to any
project. When you allocate a tier-0/VRF gateway to a project (say A), it does not
prevent you from allocating the same tier-0/VRF gateway to other projects (say B, C, and
D) in the system. This is the default NSX
behavior.

However, the system supports dedicating a
tier-0/VRF gateway to a single project only for logging purposes. When a tier-0/VRF
gateway is dedicated to a project, the log messages for the centralized services on this
tier-0/VRF gateway will contain the project context in the edge syslog.

A tier-0/VRF gateway that is dedicated to a
project (say A) can still be consumed by other projects (say B, C, and D) in the system.
However, the context for projects B, C, and D that consume the same tier-0/VRF gateway,
will not be stored in the edge syslog unless these projects have a different dedicated
tier-0/VRF gateway that is not already dedicated to any other project in the system.

To dedicate a tier-0/VRF gateway to a
project, an Enterprise Admin must configure the dedicated\_resources
parameter in the project configuration by using the project API.
Currently, this functionality is supported only with API. The NSX Manager UI does not support dedicating a
tier-0/VRF gateway to a project.

The following validations apply to dedicating
a tier-0/VRF gateway in a project:

- To dedicate a tier-0/VRF gateway to
  a project, it must be allocated to the project. For example, if you have
  allocated tier-0 gateways X and Y to a project, you cannot dedicate tier-0
  gateway Z to this project. To dedicate Z to this project, you must first
  allocate it to the project.
- A tier-0/VRF gateway can be
  dedicated to only a single project. However, a project can have multiple
  tier-0/VRF gateways dedicated to it. For example, assume that project A has two
  tier-0 gateways X and Y allocated to it. You can dedicate both tier-0 gateways X
  and Y to project A. However, X and Y cannot be dedicated to any other project in
  the system. But, X and Y can be consumed by other projects in the system.
- When you remove the
  dedicated\_resources configuration from a project, or
  when you delete the project, the tier-0/VRF gateway that was dedicated to this
  project can be dedicated to any other project in the system. For example, assume
  that you have allocated tier-0 gateway X to projects A and B and configured X as
  the dedicated resource in project A. If required, later, you can remove the
  dedicated\_resources configuration from project A and
  add X as the dedicated resource in project B.

Example
:   Assume that you have created two
    projects named Sales and Finance, as shown in the following diagram. The short log
    identifier of the Sales project is salespro and for
    the Finance project is finanpro. You have configured the
    dedicated\_resources parameter to dedicate the T0-Sales gateway
    to the Sales project, and the T0-Fin gateway to
    the Finance project. Both the tier-0 gateways are running on the same edge
    cluster.

    ![This diagram is described in the surrounding text.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0c0eea26-f32d-44fb-9a4d-31f0bafe03ba.original.png)

    The log messages for the tier-0
    services in the edge syslog will contain the following string to help you
    identify the project context:

    ```
    org="default" proj="salespro"
    org="default" proj="finanpro"
    ```

    For example, let's say, you have
    enabled BGP routing on both the T0-Sales and T0-Fin gateways.
    The log messages for both these tier-0 gateways in the edge syslog will have
    the project context, as follows:

    ```
    nsx-edge> 2023-06-27T03:31:38.717Z Edge NSX 6 ROUTING [nsx comp="nsx edge" subcomp="rcpm" s2comp="rcpm-db" level="INFO" org="default" proj="salespro"] BGP update request: Bgp Config
    nsx-edge> 2023-06-27T03:31:39.717Z Edge NSX 6 ROUTING [nsx comp="nsx edge" subcomp="rcpm" s2comp="rcpm-db" level="INFO" org="default" proj="finanpro"] BGP update request: Bgp Config
    ```

## API Workflow to Dedicate a Tier-0/VRF Gateway to a Project

For example, assume that you have created
a project named Sales,
and allocated two tier-0 gateways named T0Sales1 and T0Sales2 to this project.
You want to dedicate T0Sales1 to this project. To do this, you must use the
project API, and add the path to the T0Sales1 gateway in the
dedicated\_resources configuration of the Sales project.

Procedure
:   1. Retrieve the current
       project configuration by running the following GET
       API:

       ```
       GET https://<nsx-mgr>/policy/api/v1/orgs/default/projects/Sales
       ```
    2. Copy the response
       payload of the GET API and paste it in a text editor.
    3. In the response
       payload, add the path to the T0Sales1
       gateway in the dedicated\_resources
       configuration, as follows:

       ```
       "tier_0s": [
          "/infra/tier-0s/T0Sales1",
          "/infra/tier-0s/T0Sales2"
       ],
       "dedicated_resources": {
          "tier_0s": ["/infra/tier-0s/T0Sales1"]
       }
       ```

       To learn
       more about the dedicated\_resources
       parameter in the project API, see the NSX API Guide.
    4. Paste the full updated
       payload in the request body of the following PATCH
       API:

       ```
       PATCH https://<nsx-mgr>/policy/api/v1/orgs/default/projects/Sales
       ```

       When this API runs
       successfully, the Sales project is configured to use T0Sales1 as the default tier-0 gateway. The log
       messages for the tier-0 services running on this dedicated
       gateway will now have the context of the Sales project in the
       edge syslog.