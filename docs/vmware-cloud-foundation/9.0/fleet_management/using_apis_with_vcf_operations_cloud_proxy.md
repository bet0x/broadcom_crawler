---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/collecting-data-with-cloud-proxies-in-vrealize-operations-cloud/using-the-api-with-vmware-aria-cloud-proxy.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Using APIs with VCF Operations Cloud Proxy
---

# Using APIs with VCF Operations Cloud Proxy

You can use a browser or an HTTP client program to send requests and receive responses.

## REST Client Programs

Any client application that can send HTTPS requests is an appropriate tool for developing REST applications with the VCF Operations API. REST client plug-ins are available for most browsers and many IDEs. The following open-source programs are commonly used:

- cURL. http://curl.haxx.se
- Postman application. http://www.getpostman.com

In addition, VMware provides language-specific client bindings for the VCF Operations API.

## About the Schema Reference

The VCF Operations REST API documentation includes reference material for all elements, types, queries, and operations in the VCF Operations API. It also includes the schema definition files.

Swagger based API documentation is available with the product, with the capability of making REST API calls right from the landing page.

To access the API documentation, use the URL of your VCF Operations cloud proxy. For example, if the URL of your cloud proxy is https://cloudproxy.vmware.com, the API reference is available from: https://cloudproxy.vmware.com/suite-api/doc/swagger-ui.html

You must use your cloud proxy IP or FDQN in the url to access the API documentation.

Language-specific client bindings are available from:

```
https://cloudproxy.vmware.com/suite-api/
```

## Authorize VCF Operations API

To perform API calls, you must authorize your VCF Operations cloud proxy. You can perform basic authorization and enter the Username, Password, and the Auth Source, or perform token based authorization and enter the Ops Token (apikey) value, and then click Authorize.

## About the VCF Operations API Examples

All examples include HTTP requests and responses. These examples show the workflow and content associated with operations such as creating and querying for information about objects in your monitored environment.

Example request bodies are in JSON. Request headers required by the VCF Operations API are included in example requests that are not fragments of a larger example.

Most example responses show only those elements and attributes that are relevant to the operation being discussed. Ellipses (...) indicate omitted content within response bodies.