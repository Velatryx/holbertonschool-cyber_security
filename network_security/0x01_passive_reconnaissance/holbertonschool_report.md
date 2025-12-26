# Passive Reconnaissance Report – holbertonschool.com

## Introduction

The goal of this report is to perform passive reconnaissance on the domain **holbertonschool.com**.  
All information was collected using publicly available sources, mainly **Shodan**, without directly interacting with the target infrastructure.

The objectives of this task were to:
- Identify IP addresses and IP ranges associated with the domain
- Enumerate visible subdomains
- Observe technologies and services exposed to the internet

---

## Hosting and Infrastructure

Based on the Shodan results, Holberton School’s infrastructure is hosted on **Amazon Web Services (AWS)**.  
Most of the observed systems are located in the **eu-west-3 (Paris, France)** region.

### Hosting Providers Observed

- Amazon Data Services France
- A100 ROW Inc (AWS-related)

This suggests that Holberton School relies on a cloud-based setup, likely for scalability and availability.

---

## Identified IP Addresses

The following IP addresses were observed serving different subdomains of `holbertonschool.com`:

| IP Address | Subdomain | Hosting Provider | Location |
|-----------|----------|------------------|----------|
| 15.237.205.60 | apply.holbertonschool.com | Amazon Data Services France | Paris, FR |
| 13.39.187.93 | apply.holbertonschool.com | Amazon Data Services France | Paris, FR |
| 51.44.96.144 | apply.holbertonschool.com | A100 ROW Inc (AWS) | Paris, FR |
| 13.38.203.16 | apply.holbertonschool.com | Amazon Data Services France | Paris, FR |
| 52.47.143.83 | yriry2.holbertonschool.com | Amazon Data Services France | Paris, FR |
| 52.47.114.157 | read.holbertonschool.com | Amazon Data Services France | Paris, FR |

Several IP addresses resolving to the same subdomain indicate the use of redundancy or load-balanced services.

---

## IP Ranges

Since the infrastructure is hosted on AWS, the identified IPs belong to shared cloud netblocks.  
Examples of observed AWS ranges include:

- 13.38.0.0/16  
- 13.39.0.0/16  
- 15.237.0.0/16  
- 51.44.0.0/16  
- 52.47.0.0/16  

These IP ranges are not dedicated solely to Holberton School and are shared with other AWS customers.

---

## Subdomains Discovered

Using Shodan data and passive enumeration, the following subdomains were identified:

- apply.holbertonschool.com  
- read.holbertonschool.com  
- blog.holbertonschool.com  
- www.holbertonschool.com  
- v1.holbertonschool.com  
- v2.holbertonschool.com  
- rails-assets.holbertonschool.com  
- lvl2-discourse-staging.holbertonschool.com  
- staging-apply-forum.holbertonschool.com  
- staging-rails-assets-apply.holbertonschool.com  
- yriry2.holbertonschool.com  

The presence of staging and versioned subdomains suggests active development and testing environments.

---

## Technologies Observed

### Web Server

Across multiple subdomains, the following web server was observed:

- **Nginx**
  - Version: `nginx/1.20.0`

---

### SSL / TLS Configuration

All observed services were accessible over HTTPS.

- Supported TLS versions:
  - TLS 1.2
  - TLS 1.3 (on some subdomains)

#### Certificate Authorities

- Amazon RSA 2048
- Let’s Encrypt

Certificates were issued for individual subdomains, such as:
- apply.holbertonschool.com
- read.holbertonschool.com
- yriry2.holbertonschool.com

---

### HTTP Security Headers

Several standard security headers were present, including:

- X-Frame-Options  
- X-XSS-Protection  
- X-Content-Type-Options  
- X-Download-Options  

These headers indicate basic protection against common web-based attacks.

---

## Observations

- The infrastructure is fully cloud-based and hosted on AWS.
- Multiple IPs per subdomain indicate redundancy or load balancing.
- HTTPS is consistently enforced across observed services.
- Some resources return `401 Unauthorized`, suggesting access-controlled content.
- No unusual or non-standard services were exposed through Shodan.
