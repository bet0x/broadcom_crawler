---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/prevent-password-lockout-on-local-manager-nodes.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Prevent Password Lockout on Local Manager Nodes
---

# Prevent Password Lockout on Local Manager Nodes

Password lockout can occur after a Local Manager is imported to a Global Manager.

If you reset the admin password of the Local Manager, the admin account is locked out. As a result, the
connectivity between the Global Manager
cluster and the Local Manager cluster
fails with a general system error. The Global Manager nodes in both regions must be added to an allowlist of
trusted nodes for the Local Manager
cluster to avoid lockdown. This can be prevented by adjusting the
lockout\_immune\_addresses parameter on the Local Manager.

1. Log in to the host that has
   access to your data center.
2. Update the allowlist of trusted
   sources on the Local Manager
   appliance by using the Postman PUT method.

   You add the IP addresses of the
   Global Manager cluster to
   the lockout\_immune\_addresses list of the Local Manager cluster.

   1. Start the Postman
      application in your web browser and log in.
   2. On the Authorization tab, enter the following settings and
      click Update
      request.

      | Setting | Value |
      | --- | --- |
      | Type | Basic Auth |
      | User name | admin |
      | Password | nsx\_admin\_password |
   3. On the Headers
      tab, add a key by using the following details.

      | Setting | Value |
      | --- | --- |
      | Key | Content-Type |
      | Key Value | application/json |
   4. In the request pane at the top, send the following HTTP request.

      | Setting | Value |
      | --- | --- |
      | HTTP request method | GET |
      | URL | https://<nsx\_manager\_FQDN>/api/v1/cluster/api-service (change the FQDN to your local NSX Manager FQDN) |
   5. After a successful
      response (“status: 200 OK”), copy the
      JSON-formatted body response from the Body tab to
      a text-editor.
3. Add the
   lockout\_immune\_addresses information to the JSON
   response:
   1. Search for the
      lockout\_immune\_addresses line in the JSON response.
      If the line cannot be found in the JSON response, add a new line with
      lockout\_immune\_addresses,. Note that a “,” must be
      added to end of the previous line.
   2. Add the IP addresses of
      all global NSX Managers (including the VIP addresses) between the
      brackets in the following format, leaving the quotes intact:
      "lockout\_immune\_addresses”:[ “172.16.11.95”, “172.16.11.96”,
      “172.16.11.97”, “172.16.11.98” ]
4. Send the new security
   configuration to the local manager using the Postman PUT method:
   1. Take the previous
      Postman HTTP request and change the HTTP request method from
      GET to PUT.
   2. On the Body tab, paste
      the new JSON formatted security configuration from your code-/text
      editor.
   3. Send the new HTTP
      request and confirm a successful response (“status: 200
      OK”).
5. Repeat steps 2 through 4 for all
   NSX Managers.