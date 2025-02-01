# FOSDEM 2025 Schedule - Part 2 of 11

*Generated on 2025-02-01*

## Table of Contents

- [APIs: GraphQL, OpenAPI, AsyncAPI, and friends (7)](#apis:-graphql,-openapi,-asyncapi,-and-friends-7)
- [Attestation (9)](#attestation-9)
- [BSD (8)](#bsd-8)
- [Cloud Native Databases (12)](#cloud-native-databases-12)
- [Collaboration and Content Management (19)](#collaboration-and-content-management-19)
- [Community (16)](#community-16)
- [Confidential Computing (11)](#confidential-computing-11)
- [Containers (21)](#containers-21)
- [Data Analytics (13)](#data-analytics-13)

## APIs: GraphQL, OpenAPI, AsyncAPI, and friends (7)

### From DB Schema to API: A Deep Dive into Database-Driven API Tools

- **Speakers:** Erik Wrede
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6495-from-db-schema-to-api-a-deep-dive-into-database-driven-api-tools/)

#### Abstract

API schemas derived directly from internal data models represent a burgeoning trend in API development. This session will explore the process of shaping APIs based on database schemas, revealing significant advantages such as rapid prototyping, unparalleled Developer Experience (DevX), and an API schema that dynamically evolves with your project.
We will primarily focus on open-source tools tailored for GraphQL but will also highlight innovative techniques applicable to RESTful API development. Furthermore, the talk will address common challenges and prevalent misconceptions associated with database-driven API development, including issues like migrations, schema evolution, and complex business logic integration.
By the conclusion of this session, attendees will be thoroughly equipped with the insights and tools necessary to navigate their forthcoming API projects, leveraging the full potential of their underlying data models. Join us to unlock a new level of efficiency in your development practice, ensuring your APIs are as agile as your next project's demands.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-api:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-api:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3EYAVV/feedback/)

---

### Documenting your event-driven architectures with OpenAPI and AsyncAPI

- **Speakers:** David Boyne
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5144-documenting-your-event-driven-architectures-with-openapi-and-asyncapi/)

#### Abstract

Governance for event-driven architectures is always an after thought. Many companies often end up in a complex mess when building these distributed systems, including the lack of standards,  discoverability and ownership. 
If we treat schemas as a first class citizen, we can utilize OpenAPI and AsyncAPI to help us document our event-driven architectures and bring discoverability to our teams. 
In this talk we will explore how to get the most of our OpenAPI and AsyncAPI specifications, how to document queries, commands, events and even domains. We will also look at how to build a catalog of information for your teams to explore and discover your event-driven architectures.

#### Related Links

- [EventCatalog](https://www.eventcatalog.dev/)
- [AsyncAPI Generator for EventCatalog](https://github.com/event-catalog/generator-asyncapi)
- [OpenAPI Generator for EventCatalog](https://github.com/event-catalog/generator-openapi)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-api:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-api:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/USD9LK/feedback/)

---

## Attestation (9)

### Welcome to attestation devroom!

- **Speakers:** Thomas Fossati, Muhammad Usama Sardar
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5898-welcome-to-attestation-devroom-/)

#### Abstract

Introduction to attestation
Open source: a MUST for attestation
Honorable mention to all contributors, whether they are presenting or not
Thank the Confidential Computing devroom managers for guidance and support

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EQJVKD/feedback/)

---

### Binding Intel SGX Root-of-Trust to PKI to Establish High-Performant Trusted Channel Between Enclaves

- **Speakers:** Gilang Mentari Hamidy
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 09:30 - 09:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5042-binding-intel-sgx-root-of-trust-to-pki-to-establish-high-performant-trusted-channel-between-enclaves/)

#### Abstract

Intel provided a reference protocol for embedding Intel SGX attestation in the X.509 certificate to establish a TLS-based trusted channel named RA-TLS. This protocol does not use the Public Key Infrastructure (PKI) architecture of the X.509 certificate; instead, it relies solely on attestation quote verification to verify the binding between X.509 certificate to the Intel SGX root-of-trust. It may not always be desirable, as quote verification is relatively more expensive compared to certificate chain verification with PKI in place. Moreover, Intel reference implementation for DCAP requires additional infrastructure, including Provisioning Certificate Caching Services (PCCS), which the Intel DCAP reference implementation is tightly coupled with. 
In this talk, we present TC4SE, previously published in the Information Security Conference 2023, which proposed a mechanism to bind SGX root-of-trust primitives with PKI root-of-trust to establish trusted channel. We also present some alternative mechanisms to eliminate the dependency on the web-based PCCS server when developing an Intel SGX application that requires quote generation and verification.

#### Related Links

- [Source repo](https://github.com/DistriNet/TC4SE)
- [Publication (open-access)](https://lirias.kuleuven.be/4111625&lang=en)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8HUPGZ/feedback/)

---

### Integrating Intel TDX remote attestation into SSH

- **Speakers:** Fabian Wesemann
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 10:00 - 10:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4901-integrating-intel-tdx-remote-attestation-into-ssh/)

#### Abstract

In this talk, I will present a prototype integration of Intel TDX’s remote attestation feature into the SSH protocol.
By extending SSH, we ensure connections are only made to hosts within Trusted Domains. Since SSH is a widely used protocol for data transfer and network tunneling, many applications can benefit from this effort.
The focus will be on the design and principles of the challenge-response protocol, which has been prototyped using OpenSSH and the Microsoft Azure Attestation service.

#### Related Links

- [Prototype implementation](https://github.com/tufteddeer/openssh-tdx-remote-attestation)
- [Slides (web)](https://tufteddeer.github.io/remote-attestation-ssh-slides/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ERYFWQ/feedback/)

---

### Attested Noise Protocol for Low-TCB Trusted Execution Environments

- **Speakers:** Ivan Petrov, Katsiaryna Naliuka
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 10:20 - 10:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5739-attested-noise-protocol-for-low-tcb-trusted-execution-environments/)

#### Abstract

Trusted Execution Environments in combination with open-source and reproducible code provide transparency by relying on reviewers to analyze the Trusted Computing Base (TCB). And the size of the TCB directly influences the speed at which new releases and bug fixes are deployed to production, since reviews take a lot of time. So low-TCB environments are a desired solution that many teams try to achieve.
But even the main security features needed to implement a trusted workload, such as end-to-end encryption, require significant increases in the TCB. For example, more general approaches like TLS with an extensive feature set including support for many signature schemes, certificate parsing and session resumption logic may be less ideal for low-TCB environments.
To address this issue we will present a remote attestation scheme that uses Noise Protocol Framework to create an end-to-end encrypted attested channel between an end-user device and a TEE. Noise Protocol Framework allows us to minimize the amount of crypto primitives needed and only leave the logic that is necessary to establish an encrypted session and to bind it to the attestation evidence.
During this talk we will also present an open-source implementation of our approach written in Rust.

#### Related Links

- [Project Oak](https://github.com/project-oak/oak)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZHM7R7/feedback/)

---

### Secure Push Attestation with Extensible REST APIs

- **Speakers:** Jean Snyman
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 10:50 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6309-secure-push-attestation-with-extensible-rest-apis/)

#### Abstract

Until now, the Keylime attestation software has operated on a pull basis: requiring open ports on each attesting node so the verifier can request evidence at a set interval. A new push mode developed by the community brings a number of advantages and presents new opportunities for the project in areas such as extensibility, containerisation and even confidential computing.
In this talk, we will take a whirlwind tour of the new REST-based APIs and how these are composed to achieve a robust security result. We will discuss the challenges of managing state in a multi-phase HTTP protocol and building resilience in the presence of misbehaving clients. Attendees will hear how these changes open the door for increased integration in the wider ecosystem and our vision for the future of attestation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3YXYE7/feedback/)

---

### Measurement and Attestation Schemes for Container Sandboxes

- **Speakers:** Magnus Kulke
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 11:25 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4558-measurement-and-attestation-schemes-for-container-sandboxes/)

#### Abstract

The Confidential Containers project aims to introduce Confidential Computing into the kubernetes ecoystem. The premise is lift-and-shift: Users should be able to move their k8s apps into a TEE with little effort and the need make adjustments to their apps.
This means we are faced with a unique challenge to perform attestation of an application in such an environment. The TCB of a Confidential Containers stack contains a linux kernel for a utility VM and a container runtime in userland. In kubernetes Pods are a set of colocated containers that are spawned and managed in a highly dynamic Sandbox, driven by imperative APIs and subject to multiple hard-to-predict factors during their lifecycle.
We will discuss the approach that the project has taken to provide Attestation for Confidential Container Workloads (Launch Measurements, Measured Boot, Container Runtime Policies) and where they still fall short in terms of usability and security.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9CGHYA/feedback/)

---

### Virtual Machine attestation on Arm CCA

- **Speakers:** Jean-Philippe Brucker
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 11:55 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5749-virtual-machine-attestation-on-arm-cca/)

#### Abstract

During remote attestation, besides appraising the platform that runs a
Virtual Machine (VM), a verifier or relying party must also appraise
claims about the initial state of the VM: code and data loaded into the
VM, initial vCPU registers, and parameters. Those claims are compared
against Reference Values corresponding to a given VM.
Under the Arm Confidential Computing Architecture (CCA), VMs and their
workload come in all shapes and sizes, from lean containers with minimal
footprint to full machine emulators running standard distributions.
Calculating Reference Values for all use-cases is not obvious, and
sometimes requires help from VM managers (VMM).
In this talk we discuss the challenges of calculating Reference Values of
an Arm VM. We propose some options to help a Reference Value Provider come
up with the VM measurements, and present the tool and library we created
to experiment with remote attestation of VMs created by VMMs such as QEMU,
cloud-hypervisor and kvmtool.

#### Related Links

- [Realm Measurements tool and library](https://github.com/veraison/cca-realm-measurements)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FVSCHL/feedback/)

---

### Remote Attestation in the cloud

- **Speakers:** Jagannathan Raman
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 12:15 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5259-remote-attestation-in-the-cloud/)

#### Abstract

Remote attestation is becoming increasingly important for cloud tenants who want to ensure the confidentiality and integrity of their virtual machines (VMs) and workloads.
Veraison provides an open-source framework for implementing an attestation scheme. One of the main advantages of using Veraison is its compliance with IETF RATS, which establishes a standard method for representing data and performing verification.
We would like to share our journey with Veraison, detailing how we have implemented an attestation scheme for SEV-SNP, the sub-attesters we incorporated into our solution, and our future plans. Join us to learn how you can utilize this framework to achieve end-to-end attestation in the cloud.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MHBKQV/feedback/)

---

### Remote Attestation on Arm TrustZone OP-TEE with VERAISON Verifier --- current status and future plan ---

- **Speakers:** Kuniyasu Suzaki
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 12:40 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4952-remote-attestation-on-arm-trustzone-op-tee-with-veraison-verifier-current-status-and-future-plan-/)

#### Abstract

We report on the attestation mechanism implemented in OP-TEE, a trusted OS running on the Arm Cortex-A TrustZone. This mechanism generates attestation evidence accepted by VERAISON, an open-source verification platform.
The attestation mechanism measures the hash values of Trusted Applications (TAs) and generates attestation evidence using an attestation key stored in OP-TEE. It is implemented as a PTA (Pseudo Trusted Application), which functions as part of OP-TEE. The PTA is portable across different OP-TEE versions and extends attestation availability.
We report the provisioning process for both the attester and verifier in this model, emphasizing the need for secure setup. Additionally, we explain how to program TAs and Client Applications (CAs) running on Linux to leverage this remote attestation mechanism. These explanations aim to enable broader adoption of remote attestation by users.
The current source code is open and runs on QEMU and Raspberry Pi 3:
https://github.com/iisec-suzaki/optee-ra
We are working to integrate this source code into the OP-TEE mainline:
https://github.com/OP-TEE/optee_os/pull/7006
Current Security Concerns and Future Plans
The current implementation has some security concerns. To address these, we propose three future enhancements:
1) Key Management: Store the attestation key in an HSM (Hardware Security Module) for improved security.
2) Secure Boot Confirmation: Ensure OP-TEE is securely loaded into the TEE during the boot process.
3) Certificate-Based Attestation Keys: Introduce certificates for attestation keys to improve scalability.
These plans involve specific hardware requirements, and we aim to implement them using a board equipped with the NXP i.MX 8M Plus processor and the Secure Element SE050.

#### Related Links

- [OP-TEE Remote Attestation with VERAISON Verification.](https://github.com/iisec-suzaki/optee-ra)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-attestation:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-attestation:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9MJKS/feedback/)

---

## BSD (8)

### How FreeBSD security audits have improved our security culture

- **Speakers:** Pierre Pronchery, Michael Winser
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6152-how-freebsd-security-audits-have-improved-our-security-culture/)

#### Abstract

In this presentation we will review recent security audits of the Bhyve and Capsicum subsystems, lessons learned, how this work was funded, and how it's having a lasting impact on the security culture of FreeBSD.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GBLK7C/feedback/)

---

### Wake up, FreeBSD! Implementing Modern Standby with S0ix

- **Speakers:** Aymeric Wibo
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 15:35 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6390-wake-up-freebsd-implementing-modern-standby-with-s0ix/)

#### Abstract

Modern laptops, such as the AMD Framework and newer Intel models, no longer support the traditional ACPI S3 sleep state. Instead, they rely on S0ix, a modern standby mechanism that enables low-power idle states. This is one of the only big features still missing for FreeBSD to be a first-class citizen on contemporary laptops, and this talk will explore the journey and current progress of supporting it. Attendees will learn about the nitty-gritty of the implementation including the relevant ACPI objects, tables, and DSMs, CPU and device power states, and future plans for device idleness determination to automatically put them to sleep.
Blog post tracking progress: https://obiw.ac/s0ix
FreeBSD Project website: https://www.freebsd.org/
Working GitHub repo: https://github.com/obiwac/freebsd-s0ix

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DQE8X3/feedback/)

---

### Tracking bulk builds in pkgsrc - from Cloud to NetBSD Native

- **Speakers:** Benny Siegert
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 15:55 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4927-tracking-bulk-builds-in-pkgsrc-from-cloud-to-netbsd-native/)

#### Abstract

pkgsrc, the NetBSD package collection, includes the pbulk tool to build all (or a subset of) packages. Bulk build reports are an invaluable resource for pkgsrc developers to find build breakage and its causes.
Since 2014, I have maintained a web app called Bulk Tracker (written in Go) to visualize bulk build results along different dimensions such as package name, platform and compiler. Originally written as a "serverless" App Engine application, it has recently been completely rewritten to run natively on NetBSD, on a server owned by the project.
This talk will show how bulk build data is useful and some typical use cases the app supports. It will also be about the journey out of the cloud and from a document datastore to SQLite.
https://releng.NetBSD.org/bulktracker/

#### Related Links

- [Slides](https://docs.google.com/presentation/d/e/2PACX-1vQUUgMIhsGKuFq5T3xj12Tio_FdRF5Y1XmnHSTPDcGorKYBtvKS-fLDjywDsyUEL_Ou2CCRIGWiaBOy/pub?start=false&loop=false&delayms=60000)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UASUA8/feedback/)

---

### High Performance Packet filtering in BSD. A holistic review

- **Speakers:** Emmanuel Nyarko
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 16:25 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4399-high-performance-packet-filtering-in-bsd-a-holistic-review/)

#### Abstract

Packet Filtering in BSD could be seen from several angles. There are quite a number of packet filters in the BSDs. some Implemented in the kernel, some in the user space. In this talk, we will go through a particular NetBSD packet filter, NPF, evaluate its numerous advantages and assess critical performances and share its directions going forward.

#### Related Links

- [GitHub repository](https://github.com/Emmankoko)
- [current dirty work branch on work on ALTQ integration in NPF](https://github.com/Emmankoko/altq_refactoring_gsoc)
- [netbsd blog](https://blog.netbsd.org/tnf/entry/google_summer_of_code_2024)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FJHSLG/feedback/)

---

### A packet's journey through pf

- **Speakers:** Kristof Provost
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 16:55 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4306-a-packet-s-journey-through-pf/)

#### Abstract

A walkthrough of a packet's journey through (FreeBSD's) pf, concentrating on the big picture and its implications.
We'll cover when packets are inspected, when rules are evaluated and how states are used.
Along the way we'll cover what DTrace probes can show us, what some of pfctl's counters mean and just how many times pf can look at a single packet.
This talk is intended for firewall admins looking for a deeper understanding and aspiring pf developers. It is not a "How to use pf" talk.

#### Related Links

- [Source code](https://cgit.freebsd.org/src/tree/sys/netpfil/pf)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RR77KV/feedback/)

---

### Making NetBSD as a fast(er) booting microvm

- **Speakers:** Emile 'iMil' Heitor
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 17:30 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5166-making-netbsd-as-a-fast-er-booting-microvm/)

#### Abstract

How we implemented PVH boot capability to the NetBSD kernel, allowing it to start straight from QEMU's -kernel parameter or Firecracker's VMM. In the process, we reduced boot time from 300 to 20ms, using methods borrowed from FreeBSD, and some in-house optimisations to get rid of unnecessary delays.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RMYK3Z/feedback/)

---

### Writing about FreeBSD

- **Speakers:** Tom Jones
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 18:05 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5247-writing-about-freebsd/)

#### Abstract

As a project we have notoriously great documentation. The handbook and man pages make it easy to find out how to do anything you might want to on a FreeBSD system, whether it is setting up a network or debugging kernel locking.
Explaining the changes we make to improve FreeBSD? We are less good at communicating what we are up to.
For the last 6 months I have been writing regular status reports about changes in the FreeBSD network stack using a tool guided approach to automate finding and managing what to write about.
In this talk I’ll explain how I am trying to improve communication around FreeBSD development and how you can get involved in writing about FreeBSD.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YMDTKL/feedback/)

---

### FreeBSD audit source and other syslog-ng news

- **Speakers:** Peter Czanik
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 18:35 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4553-freebsd-audit-source-and-other-syslog-ng-news/)

#### Abstract

FreeBSD is one of the most popular platforms to run syslog-ng. Recently, I was approached if we could add a FreeBSD audit source driver to syslog-ng. While developing a new C-based driver is not something we could do in the short term, thankfully, using the program() source of syslog-ng still allowed us to create a new source in just a few hours, including its documentation.
From this talk, you can learn how the freebsd-audit() source was created and how you can also easily develop similar sources yourself. A few more FreeBSD specific developments will also be mentioned.

#### Related Links

- [syslog-ng project](https://github.com/syslog-ng/syslog-ng/)
- [FreeBSD audit source in syslog-ng](https://www.syslog-ng.com/community/b/blog/posts/freebsd-audit-source-for-syslog-ng)
- [syslog-ng 4.8.0 blog with FreeBSD improvements](https://www.syslog-ng.com/community/b/blog/posts/version-4-8-0-of-syslog-ng-improves-freebsd-and-macos-support)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bsd:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bsd:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BPBW7A/feedback/)

---

## Cloud Native Databases (12)

### Devroom welcome

- **Speakers:** Ray Paik, Franck Pachot, Matthias Crauwels, Lori Lorusso
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 15:00 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6680-devroom-welcome/)

#### Abstract

Welcome session for the Cloud Native Databases devroom

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JBNNAV/feedback/)

---

### Building the next generation of Cloud Native Database

- **Speakers:** Sunny Bains
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 15:05 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5321-building-the-next-generation-of-cloud-native-database/)

#### Abstract

Cloud Native databases architecture has evolved to leverage the elasticity, reliability and scalability available in the cloud. There is a growing trend to leverage object storage systems such as  AWS S3 for architecting cost-effective, performant and scalable systems. S3 is a large-scale, high throughput key-value storage system, which it trades for a slightly higher latency. In this session we will present techniques used to leverage S3 for a low latency scalable distributed SQL database, in particular how  to get around S3’s high latency by leveraging a novel new LSM Cloud Storage Engine that uses EBS as a cache to lower latency.

#### Related Links

- [TiDB is made up of horizontally scalable storage that is a graduated CNCF project.](https://github.com/tikv/tikv)
- [The Placement Driver that is also a graduated CNCF project](https://github.com/tikv/pd)
- [The front end SQL nodes](https://github.com/pingcap/tidb)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KDXNBQ/feedback/)

---

### Reusing PostgreSQL codebase in a Distributed SQL Architecture (YugabyteDB)

- **Speakers:** Franck Pachot
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 15:35 - 16:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5036-reusing-postgresql-codebase-in-a-distributed-sql-architecture-yugabytedb-/)

#### Abstract

YugabyteDB distinguishes itself among distributed SQL databases by utilizing PostgreSQL's C code rather than building a compatibility layer from the ground up. This session will explore both the advantages and challenges of this architecture. We will drill down from PostgreSQL's familiar query layer to the distributed storage system, which stores PostgreSQL tuples and lock intents within RocksDB's LSM trees using Raft replication. 
We will be guided by analyzing execution plans that closely resemble those of PostgreSQL and adding further metrics that shed light on the underlying storage operations. We may also evaluate stack traces to identify the PostgreSQL and RocksDB functions involved in query execution. Finally, the session will discuss the rationale behind forking PostgreSQL, focusing on its benefits and trade-offs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PPQ7UQ/feedback/)

---

### Designing YDB: Constructing a Distributed cloud-native DBMS for OLTP and OLAP from the Ground Up

- **Speakers:** Evgenii Ivanov
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 16:05 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5374-designing-ydb-constructing-a-distributed-cloud-native-dbms-for-oltp-and-olap-from-the-ground-up/)

#### Abstract

Distributed systems are great in multiple aspects: they are built to be fault tolerant and reliable, can scale almost infinitely, provide low latency in geo-distributed scenarios and, finally, they are geeky and fun to explore. YDB is an open source distributed SQL database which has been running production for years. There are installations with thousands of servers storing petabytes of data. To provide these capabilities, any distributed DBMS must achieve consistency and consensus while tolerating unreliable networks, faulty hardware and absence of a global clock.
In this session, we will provide a gentle introduction to problems, challenges and fallacies of distributed computing, explaining why sharded systems like Citus are not always ACID and differ from truly distributed systems. Then, we will dive deep into the design decisions made by YDB to address these difficulties and sketch YDB's architecture layer by layer - from the bare metal disks and distributed storage up to OLTP and OLAP functionalities. At the end, we will briefly compare our approach with that of Calvin, which originally inspired YDB, and Spanner.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WR3STX/feedback/)

---

### Migrating Massive Aurora and MySQL Databases to Vitess Kubernetes Clusters with Near-Zero Downtime

- **Speakers:** Matthias Crauwels, Rohit Nayak
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 16:35 - 17:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4759-migrating-massive-aurora-and-mysql-databases-to-vitess-kubernetes-clusters-with-near-zero-downtime/)

#### Abstract

Vitess, a CNCF-graduated, open-source, MySQL-compatible database, is designed for massive scalability and cloud-native deployments. As one of the most robust solutions for managing large-scale database workloads, Vitess on Kubernetes powers some of the largest systems in the world.
Modern data teams face a growing challenge: scaling databases dynamically to handle surges, such as holiday sales or viral trends. For many, vertical scaling has reached its limits, leaving fundamental architectural changes as the only option. Vitess, with its built-in horizontal sharding capabilities, provides a seamless path for organizations to scale beyond the constraints of legacy MySQL or Aurora clusters.
This talk explores how Vitess enables smooth migrations from Aurora and MySQL into Kubernetes clusters with near-zero downtime. We will begin with an overview of Vitess’ architecture, highlighting horizontal sharding and its advantages for scaling. Next, we will dive into the powerful workflows Vitess provides for data import and live production migrations, emphasizing their safety, efficiency, and reversibility—even for massive datasets.
To ground these concepts, we will share real-world examples of successful migrations from web-scale Aurora and legacy MySQL databases, including performance metrics, data sizes, and challenges encountered. Attendees will gain practical insights and a clear blueprint for transitioning large-scale database systems to Vitess, unlocking unprecedented scalability and operational agility.

#### Related Links

- [Vitess: Scalable. Reliable. MySQL-compatible. Cloud-native. Database.](https://vitess.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FKVQVW/feedback/)

---

### Tracing the Internals of a Cloud-Native Database

- **Speakers:** Josh Lee
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 17:05 - 17:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5956-tracing-the-internals-of-a-cloud-native-database/)

#### Abstract

Have you ever wondered what happens inside a distributed database when you run a query? In this talk, we’ll explore the inner workings of ClickHouse using OpenTelemetry-compatible distributed tracing to analyze the internal workings of various ClickHouse clusters while we run a variety of queries. Perfect for database enthusiasts and cloud-native developers, this session offers practical insights into tracing tools and query optimization in distributed systems.

#### Related Links

- [ClickHouse Homepage](https://clickhouse.com)
- [OpenTelemetry](https://opentelemetry.io)
- [Altinity Operator](https://github.com/Altinity/clickhouse-operator)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VDKXWT/feedback/)

---

### Distributed SQL Technologies: Raft, LSM Trees, Time, and More

- **Speakers:** Franck Pachot, Daniël van Eeden
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 17:35 - 18:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4958-distributed-sql-technologies-raft-lsm-trees-time-and-more/)

#### Abstract

This session will focus on the open-source distributed SQL databases TiDB and YugabyteDB. We will explore their building blocks to understand how they function, highlighting their similarities and architectural differences. Key topics will include how changes are versioned (using either Time Stamp Oracle or Hybrid Logical Clocks), how data is replicated (with Raft), how they store rows, index entries, and transaction intents (utilizing RocksDB LSM trees), and how they implement ACID properties (through either Percolator or IntentsDB).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NW93NR/feedback/)

---

### Distributed Databases: Essential or Optional?

- **Speakers:** Peter Zaitsev
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 18:05 - 18:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5743-distributed-databases-essential-or-optional-/)

#### Abstract

In the era of distributed systems, many modern databases are designed to scale horizontally from the ground up. Yet, some of the most widely used databases, like MySQL and PostgreSQL, remain single-node by design, relying on third-party sharding solutions like Citus or Vitess for distribution.
This raises a critical question: do we always need to go distributed, or can replicated single-node databases meet most use cases? In this talk, we’ll explore the trade-offs between distributed and non-distributed architectures, evaluate the limits of single-node databases, and discuss when it truly makes sense to embrace distribution. Join us as we navigate the complexities of modern database design and uncover what’s best for your applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AQEEV8/feedback/)

---

### Unlocking Global Resilience using Cloud Native Distributed Datastore

- **Speakers:** Mary Grygleski
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 18:20 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6530-unlocking-global-resilience-using-cloud-native-distributed-datastore/)

#### Abstract

In today's hyper-connected world, organizations demand database solutions that transcend traditional infrastructure limitations. This talk explores how distributed SQL databases (such as the open source based YugabyteDB) enable unprecedented global resilience and scalability. We'll dive into practical strategies for building fault-tolerant, geo-distributed systems that can withstand regional failures while maintaining data consistency and high performance.
Key insights include:
* Architectural principles of cloud-native distributed databases
* Multi-region deployment strategies
* Automatic failover and self-healing mechanisms
* Real-world implementation patterns
Open Source project that is being used in this talk:
YugabyteDB

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A8W9BN/feedback/)

---

### Running Mattermost on YugabyteDB

- **Speakers:** Jesús Espino
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 18:30 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4344-running-mattermost-on-yugabytedb/)

#### Abstract

Mattermost is an open-source collaboration platform that uses PostgreSQL for its database. As a developer heavily involved with Mattermost, I constantly explore new technologies. Recently, I came across YugabyteDB and decided to test it as a replacement for PostgreSQL. In this tech talk, I will share my previous experience with another distributed database and how it compares with my experience with YugabyteDB. Also, I will share the results of running load tests on Yugabyte and how it compares to regular Postgres.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DRJLAW/feedback/)

---

### Migrating 3B rows to TiDB for a high-traffic application

- **Speakers:** Sorin Dumitrescu
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 18:40 - 18:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4993-migrating-3b-rows-to-tidb-for-a-high-traffic-application/)

#### Abstract

A short story about why & how Omniconvert migrated from MongoDB to TiDB, with no downtime, for an application serving 15-20k requests per minute.
We will discuss the challenges that prompted the migration, why we chose TiDB, overview stress testing & performance evaluation of the application running on TiDB, as well as walk through the steps of the migration. And of course, highlight some lessons learned and the end-user perceived improvements.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M7AR9V/feedback/)

---

### I Like To Move IT, Move IT - Replication in TiDB & MySQL

- **Speakers:** Leandro Morgado
- **Room:** UA2.114 (Baudoux)
- **Day:** Saturday
- **Time:** 18:50 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5452-i-like-to-move-it-move-it-replication-in-tidb-mysql/)

#### Abstract

Replication is a cornerstone of modern database systems, enabling high availability, scalability, and seamless data transfer across environments.
In this talk, we’ll delve into the replication capabilities of TiDB and explore how they address real-world database challenges at Bolt, the fast-growing Estonian-based mobility company.
We’ll begin with an introduction to TiDB Data Migration (DM), which facilitates MySQL-to-TiDB replication. Through practical examples, we’ll demonstrate its role in migrating MySQL workloads to TiDB, including shard consolidation.
Next, we’ll highlight TiCDC (TiDB Change Data Capture), a powerful tool for real-time data streaming. We’ll explain how TiCDC captures changes in TiDB and replicates them to downstream systems such as TiDB, MySQL, Apache Kafka, and other services. Use cases include easily reversible TiDB version upgrades, cross-region high availability with standby TiDB clusters, and real-time Change Data Capture into Kafka.
Throughout the talk, we’ll share practical tips and scenarios, including simplifying database migrations, minimiing downtime during upgrades, and ensuring data integrity in complex workflows.
Whether you’re migrating from MySQL to TiDB, upgrading TiDB clusters, or building cross-region high availability environments, this talk will equip you with the knowledge and strategies to leverage replication as a powerful tool in your database operations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-databases:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-databases:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PXMLZ9/feedback/)

---

## Collaboration and Content Management (19)

### What's new in Nextcloud?

- **Speakers:** Jos Poortvliet
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 10:30 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4515-what-s-new-in-nextcloud-/)

#### Abstract

It's a tradition. A TRADITION! So, sit back, relax, and enjoy the show.
I'll share what happened in Nextcloud in 2024. It's a lot, as always. Will it be 300 slides this year? 400? Nobody knows, not even me! But you will find out.
We're still working to change the world, here at Nextcloud. We grow, fast, and serve more users with more on-premises, secure and just beautiful software that keeps their data safe from Big Tech.
Share and work on documents with Nextcloud Files and Nextcloud Office. Chat and do your video calls with Nextcloud Talk. Discuss philosophy (or do useful things) with the Nextcloud Assistant. Or automate your business with Nextcloud Flow.
And be sure: your data does NOT leave your server. Not even when you're translating text or using the AI to help answer your emails. Because we DO take privacy serious. Seriously.
See you in Brussels!

#### Related Links

- [Our website](https://nextcloud.com)
- [The Code!](https://github.com/nextcloud)
- [Nextcloud Hub 9 - the latest!](https://nextcloud.com/blog/nextcloud-hub9/)
- [Nextcloud Hub 8 - so, so close!](https://nextcloud.com/blog/nextcloud-hub8/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3ZKMJW/feedback/)

---

### Open Cloud Mesh

- **Speakers:** Michiel de Jong
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 11:15 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5094-open-cloud-mesh/)

#### Abstract

Personal cloud servers like Nextcloud, ownCloud, SeaFile and CERNBox have for several years now supported the Open Cloud Mesh protocol for inviting collaborators to a document or folder.
Open Cloud Mesh is an authorisation flow, rather than a data access protocol. In this sense it's similar to the role OAuth plays for establishing API access.
Open Cloud Mesh can be used to establish collaboration, after which the actual read/write traffic would for instance be handled via server-to-server WebDAV connections.
This means that Open Cloud Mesh can be used in combination with many other protocols, in many different scenarios, depending on document type and mode of collaboration. The protocol is agnostic about whether the collaboration that is being established concerns for instance a text file or a real-time video conference.
We recently published this protocol as an Internet Draft, we run automated tests between implementers and we recently held a technical workshop about the protocol, where implementers came together to compare notes and discuss possible features to add.
This talk will give an overview of how Open Cloud Mesh works and hopefully we can get into a discussion of how Open Cloud Mesh can be useful to others.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UTYFKN/feedback/)

---

### Why don't we have `libsync` yet?

- **Speakers:** Victor Grishchenko
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 11:45 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5867-why-don-t-we-have-libsync-yet-/)

#### Abstract

An average Linux distro has about half a dozen file syncing libs. The source code we sync with git and other SCMs.
But how can we sync some structured data?
JSON, for example. Two-way, maybe in real time, for collaboration, revision control, and simply device syncing. As it turns out, there are challenges.
I will outline the history of the question and the ongoing efforts.
Then, we will delve into the Replicated Data eXchange format (RDX) and the progress of librdx.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LZALLY/feedback/)

---

### CryptPad: Recent Advances in Privacy and Collaboration

- **Speakers:** Fabrice Mouhartem
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 12:15 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5033-cryptpad-recent-advances-in-privacy-and-collaboration/)

#### Abstract

CryptPad is an open-source and end-to-end encrypted collaborative office suite. Since its inception 10 years ago, it has been actively developed at XWiki to offer a unique combination of privacy and collaboration. In this talk I will summarise CryptPad's development to date, from a single-page prototype to a full-blown office suite. I will then give an overview of the progress made in the last year including: accessibility and mobile, performance improvements, cloud instances, and work on the OnlyOffice integration to name a few. Finally I will give a glimpse of things to expect in 2025.

#### Related Links

- [Project Website](https://cryptpad.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZRPMUQ/feedback/)

---

### Ethersync – Real-time Collaboration in Your Text Editor!

- **Speakers:** blinry
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 13:00 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4890-ethersync-real-time-collaboration-in-your-text-editor-/)

#### Abstract

We'll introduce you to our project "Ethersync," a software and protocol for real-time collaboration. The goal is to make it feel like Etherpad, but for entire projects, on the local file system, and with Neovim, VS Code, or your other favorite text editors! We’ll talk about our vision, technical implementation, and the challenges we encountered along the way.
Collaborating with software like Etherpad or Hedgedoc feels a bit like magic: you can instantly see what others are typing. The downside is that you need to be online to access the content—since the document is on a server, it disappears as soon as you disconnect.
We’re working on an open-source software called "Ethersync" to bring real-time collaboration to the file system! We want to make it possible to write notes and documentation together, and we’re also considering use cases like pair programming—directly in Neovim, VS Code, or perhaps your favorite text editor soon. We’re following a "local-first" approach, ensuring you always have control over your data since it’s stored on your own hard drive.
In this talk, we’d like to explain our vision for this type of collaboration and show you our progress and current prototype. We’ll discuss some of the problems we’ve encountered and dive into the underlying technology (like Conflict-Free Replicating Data Types and Operational Transform).
Finally, we'll discuss how you can get involved: For example, we could use help developing plugins for more text editors! We'll go over the Ethersync protocol, and discuss how it could help interoperability between collaborative projects.

#### Related Links

- [Source code](https://github.com/ethersync/ethersync)
- [Documentation](https://ethersync.github.io/ethersync/)
- [Mastodon account](https://fosstodon.org/@ethersync)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/F8H733/feedback/)

---

### NextGraph : Build collaborative, local-first and decentralized apps

- **Speakers:** Niko Bonnieure
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 13:15 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4922-nextgraph-build-collaborative-local-first-and-decentralized-apps/)

#### Abstract

NextGraph is an open source ecosystem providing solutions for end-users (a platform) and software developers (a framework), wishing to use or create decentralized apps featuring: live collaboration on rich-text and JSON documents, peer to peer communication with end-to-end encryption, offline-first, local-first, portable and interoperable data, total ownership of data and software, security and privacy.
Centered on repositories containing semantic data (RDF), rich text, and structured data formats like JSON, synced between peers belonging to permissioned groups of users, it offers strong eventual consistency, thanks to the use of CRDTs. Documents can be linked together, signed, shared securely, queried using the SPARQL language and organized into sites and containers.

#### Related Links

- [Website](https://nextgraph.org)
- [Community forum](https://forum.nextgraph.org)
- [Source code](https://git.nextgraph.org/NextGraph/nextgraph-rs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AFWNCD/feedback/)

---

### Panel : Integration between collaborative applications

- **Speakers:** Ludovic Dubost, Wieland Lindenthal, Ingo Steuwer, Björn Schießle
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 13:30 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5877-panel-integration-between-collaborative-applications/)

#### Abstract

Open Source is all about collaboration, but of course we don't all work in one big project. So projects have to work together - actively. How do collaboration and integration stack up with the competition between projects and even the forking into new ones? Should there be more distributions on distrowatch.org or should we abolish them? We can't speak for distributions, but certainly for the collaboration tools we built!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YXUJ9C/feedback/)

---

### Collabora Online - richer collaboration

- **Speakers:** Michael Meeks
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6579-collabora-online-richer-collaboration/)

#### Abstract

One of the interesting things about Collabora is the extremely powerful LibreOffice core it is built on. Come and hear how we've been
working hard to expose even more powerful browser-based collaborative functionality from it.
Hear about our new WebGL transitions, Automatic Document generation from documents + JSON, as well as exposing much of the power of our core functionality from fonts and AutoText to more powerul configuration options.
Finally have a quick summary of UI wins and other recent improvements, as well as how to get involved.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LQMBLT/feedback/)

---

### OpenProject: A Review of the Latest Features and Innovations

- **Speakers:** Wieland Lindenthal
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6657-openproject-a-review-of-the-latest-features-and-innovations/)

#### Abstract

Join us for a comprehensive review of the newest features and innovations in OpenProject, developed over the past year. This session will explore key updates, including enhancements to project portfolio management, deeper integration with the openDesk application bundle, and the exciting progress of a mobile app spike. Discover how these developments empower teams to collaborate more effectively, manage projects with greater precision, and streamline workflows. Whether you’re a long-time user or new to OpenProject, this talk will offer valuable insights into how the platform continues to evolve and create value.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AQGUFU/feedback/)

---

### Cristal - A flexible wiki UI

- **Speakers:** Manuel Leduc
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5339-cristal-a-flexible-wiki-ui/)

#### Abstract

Cristal is an innovative, modular Wiki User Interface built entirely with TypeScript. It enables navigation and content creation across multiple knowledge sources, including XWiki, local folders, GitHub or NextCloud. Designed with a focus on modularity and extensibility, Cristal offers a modern, polished interface build with VueJS. Its features include offline capabilities, and real-time collaboration.
In this talk, we will showcase the progress made over the past year, including key features and the challenges we faced. We will also discuss how the project has evolved and outline the roadmap for the upcoming year.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SWDZHT/feedback/)

---

### Collaborative editing in a MediaWiki environment

- **Speakers:** Richard Heigl, Markus Glaser, Robert Vogel
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5993-collaborative-editing-in-a-mediawiki-environment/)

#### Abstract

Real-time editing offers users many advantages, editing conflicts are reduced, writing minutes before and during the meeting is much more effective, and much more. However, the fact that real-time editing is now a standard requirement for a modern visual editor is primarily due to the fact that user expectations have changed with Google Docs and Confluence. The open source world has faced and continues to face the challenge of keeping up. 
We have therefore extended the Wikimedia VisualEditor with real-time editing for the MediaWiki distribution BlueSpice. The result is a freely available, 100% open source solution for real-time editing, which is based on the most popular wiki software. 
In this talk we will provide a first, thoroughly self-critical field report: we will show which technical problems had to be solved, we will report on use cases and initial experiences and on the impact on knowledge sharing with wikis. For example, questions of version control and accountability had to be redefined. Was it worth the effort? Definitely.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UEKTBZ/feedback/)

---

### From Open Collaboration to Customized Control: Transitioning from Wikidata to Wikibase

- **Speakers:** John Samuel
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6551-from-open-collaboration-to-customized-control-transitioning-from-wikidata-to-wikibase/)

#### Abstract

Transition from open collaboration to customized control with Wikibase, a self-hosted platform designed for tailored data management. While Wikidata provides a robust, open, multilingual, and collaborative environment, it may not fully address the specific needs of personal or institutional data. Wikibase empowers you to structure and manage your information on your own infrastructure, combining the strengths of Wikidata with the flexibility of a self-hosted solution. By seamlessly integrating global entities, leveraging existing translations, and aligning with linked open databases, including Wikidata, Wikibase enables you to build a connected and enriched data ecosystem. Discover how Wikibase bridges collaboration and control, offering independence while staying interconnected within the open data landscape.
References:
1. Wikidata
2. Wikibase
3. Wikibase on GitHub
4. Wikibase Cloud
5. The Linked Open Data Cloud

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BC8PFZ/feedback/)

---

### Cypht integration in Tiki: Email as a first-class citizen

- **Speakers:** Jean-Marc Libs
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 17:00 - 17:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5473-cypht-integration-in-tiki-email-as-a-first-class-citizen/)

#### Abstract

Cypht is an awesome Free/Libre/Open Source webmail aggregator written in PHP and JavaScript.
Tiki is the Free/Libre/Open Source Web Application with the most built-in features, obviously including a webmail.
Cypht within Tiki expands on the collaboration possibilities.
Email handling (reading, replying and archiving) should be part of a larger collaborative workflow. Instead of one gigantic mail store, we should have a number of smaller ones that make sense to one's workflow (ex.: around projects, tasks, clients, etc.) and that can easily be shared and prioritized.

#### Related Links

- [Tiki project](https://tiki.org/)
- [Tiki source code (LGPLv2)](https://gitlab.com/tikiwiki/tiki)
- [Cypht project](https://www.cypht.org/)
- [Cypht source code (LGPLv2)](https://github.com/cypht-org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QV8T7E/feedback/)

---

### A wiki as shared collaboration arena for humans and artificial agents?

- **Speakers:** Richard Heigl, Markus Glaser, Robert Vogel
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 17:15 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6107-a-wiki-as-shared-collaboration-arena-for-humans-and-artificial-agents-/)

#### Abstract

Wikis are a place where humans collaborate to store knowledge. It excels at free-form natural language representation of knowledge which can be stored and retrieved easily by humans. It also increasingly serves as a knowledge base for chat bots and other artificial agents which are based on LLMs and their technologies. 
While interacting with humans in a chat, AI agents can also gain new knowledge. This talk proposes that the wikis can also be a place where AI agents can persist this information. In that way, it would be readable for both humans and AI agents. This would make the wiki a perfect place for human / AI collaboration.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RXR3RT/feedback/)

---

### Secure credential collaboration with Passbolt

- **Speakers:** Remy Bertot
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 17:30 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4071-secure-credential-collaboration-with-passbolt/)

#### Abstract

Passbolt is an open-source platform for secure credential management. The solution has demonstrated its effectiveness with over 400,000 daily users and thousands of companies relying on it worldwide.
In this talk, we will present real-world use cases, and discuss Passbolt strengths in centralizing, organizing, and sharing credentials without compromising security or privacy. We will also provide a sneak peek at the upcoming v5 release, which features a new security model.
This talk aims to provide insights into technical advancements while sparking discussions on the challenges and opportunities posed by the need for secure collaboration.

#### Related Links

- [Passbolt](https://www.passbolt.com)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TYYJ3T/feedback/)

---

### End-to-end Entreprise Search with Datafari Community Edition

- **Speakers:** ULMER Cédric
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 17:45 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5668-end-to-end-entreprise-search-with-datafari-community-edition/)

#### Abstract

In this talk, we will introduce Datafari Enterprise Search, in its open source Community Edition. Datafari aims at providing an end-to-end solution, from multi-sources knowledge crawling up to the search interface, including a web administration. We will be presenting its architecture, its main functionalities, and its current roadmap for integrating generative AI to the mix (including RAG).
Repositories are hosted on our gitlab:
https://gitlab.datafari.com/explore/groups
With a mirror on github for the main Datafari CE repository:
https://github.com/francelabs/datafari

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MRPLWW/feedback/)

---

### How hard is it to bring a professional level, sustainable, advanced CMS to market?

- **Speakers:** Michael Diedrick
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 18:15 - 18:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6455-how-hard-is-it-to-bring-a-professional-level-sustainable-advanced-cms-to-market-/)

#### Abstract

We started building CMSes before the days of Wordpress, and we’ve built new CMS every five years or so since. In 2020, hunkered in my covid quarters, I wanted to devise the next version that had a hosted version, a self-hosted, more customizable version, and an open source version. 
Kentico’s Petr Palas wrote a treatise in 2017 on why we shouldn’t build a new CMS. His essay basically considers custom CMSes a way to lock in clients, and suggests cloud-first headless CMSes were the future. I, as well, have built multiple versions of custom CMSes, but I see it quite the opposite – even 8 years later, now is exactly the time to create a new CMS.
In this talk I’m going to show the process, roadmap, dangers and successes of creating a content management system from the ground up. I’m going to talk through each of the parts, including errors and notification systems, issues and help systems, user and permissions systems, etc. I’m going to cover the many “required” layers of development that we just didn’t need that saved us thousands of hours and acquired a fraction of the technical debt.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PPH8RQ/feedback/)

---

### Rethinking the Web CMS and Finding the Excitement

- **Speakers:** Michael Diedrick
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 18:30 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6462-rethinking-the-web-cms-and-finding-the-excitement/)

#### Abstract

In the eyes of a site editor or administrator, web content management systems haven’t really changed much in 20 years. They all seem so similar to each other and cover the same distance as to be wholly generic. If there’s innovation in CMSes, it seems to be more about architecture, marketing, SEO and templates and less about customizations, new ideas and administrator delight. The players haven’t changed much over the years, and the newer players seem mostly focused on monetization through scale and commerce. 
What can we do as a community to rethink the humble web CMS and open new pathways and ideas that could make a web CMS exciting again? This talk hopes to open more questions than answers, drawing on my 25 years of experience working with and building CMSes, and will cover some potential ways to move the industry forward through collaboration, CMS data interoperability and collective innovation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3WHZVX/feedback/)

---

### Consent-based Secure Collaboration with Spritely Goblins Object-Capabilities

- **Speakers:** Juliana Sims
- **Room:** H.1308 (Rolin)
- **Day:** Saturday
- **Time:** 18:45 - 18:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5312-consent-based-secure-collaboration-with-spritely-goblins-object-capabilities/)

#### Abstract

The object-capability security paradigm (ocaps) is a conceptually simple, efficient model for collaboration in mutually-suspicious contexts.  Spritely is exploring concepts and building solutions in this space to solve real-world problems while encouraging the wider adoption of ocaps, including by working alongside other ocaps organizations and projects to define a standard protocol for intercommunication between ocaps systems.  This talk will explain what ocaps is and why you should use it.
Our current model of collaboration is broken.  Rather than basing our systems on granting consent, we base them on revoking authority.  Ocaps inverts this model with its "if you don't have it, you can't use it" approach, facilitated by restricted means of exchanging authority.  Meanwhile, the Object Capability Network protocol (OCapN) abstracts away transport mechanisms between objects while creating a security barrier with minimal overhead.  Altogether, this ocaps ecosystem enables secure collaboration in mutually-suspicious contexts by emphasizing and enforcing a consent-based approach to information and authority exchange.  Spritely is pioneering new tooling for ocaps with its Goblins library, which also serves as a model for other implementations; and has plans for solutions to problems like distributed storage, identity management, and even social networking.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-collaboration-and-content-management:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-collaboration-and-content-management:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UHUYFM/feedback/)

---

## Community (16)

### Compassionate Open Source Community Building (The Tauri Model)

- **Speakers:** Denjell
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 10:35 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6202-compassionate-open-source-community-building-the-tauri-model-/)

#### Abstract

We mitigate "bus-factor", proclaim "accountability", enhance "productivity", champion "transparency". We lament the financial failings of "donations", and worry about people "silently quitting". The underlying problems however, are maintainer burn-out, imposter syndrome, entitled users, and social alienation.
In my talk I want to reframe the discussion of sustaining the maintainers to be one of primarily seeking to support mental health and well being instead of focussing on fixing abstract problems with money. In my talk I will introduce open-source leadership techniques that are person-focussed instead of outcome oriented, leveraging examples from the Tauri community.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8CCBYG/feedback/)

---

### Bridging the Gap: Regional OSPO Networks as Catalysts for Open Source and Local Community Collaboration

- **Speakers:** Jonathan Starr
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 11:05 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5904-bridging-the-gap-regional-ospo-networks-as-catalysts-for-open-source-and-local-community-collaboration/)

#### Abstract

Open source is more than just code—it is a philosophy, a movement, and a framework that touches every aspect of society. However, as open source grows, there is a risk of it becoming another siloed institution, disconnected from the very communities it seeks to serve, much like academia and corporate America. To ensure open source remains inclusive and impactful, we must actively involve local communities in the process of technological development.  
This talk explores how regional OSPO (Open Source Program Office) networks can serve as catalysts for inclusive innovation by connecting local communities, tech meetups, academic institutions, and civic organizations. These networks create a framework to:
- Study problems affecting local communities.
- Develop open technologies tailored to address these issues.
- Implement solutions through open governance, ensuring transparency, equity, and sustainability.  
By dedicating resources to both regional collaboration and local focus, regional OSPO networks strike a balance that drives large-scale innovation while staying grounded in the needs of diverse communities.  
Key themes include:
- Open Source as a Societal Institution: Why open source must go beyond code and actively integrate with local communities to avoid becoming siloed.
- Regional Networks for Connection: How regional OSPO networks foster collaboration among civic institutions, academia, local communities, and the tech industry.
- Inclusive Technology Development: How to engage local voices to study problems, co-develop solutions, and ensure equitable implementation.
- The 20/80 Framework: A practical model for balancing local focus with regional collaboration to create resilient and impactful networks.  
This session offers a vision for a new kind of open source ecosystem—one that connects society’s diverse sectors, tackles real-world problems, and builds a foundation for sustainable, community-driven innovation. Whether you’re a community leader, OSPO practitioner, or open source advocate, join us to explore how we can bridge the gap between open source ideals and societal impact.  
Key Takeaways:
- The importance of integrating local communities into open source development processes.
- How regional OSPO networks can address local challenges through collaborative innovation.
- Strategies for fostering open governance and inclusive technology development.  
This talk is a call to action: let’s ensure open source remains a force for collective good, bringing all of society into the fold. Together, we can prevent open source from becoming another siloed institution and instead position it as a true bridge to a better future.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SCXB7A/feedback/)

---

### Build a Great Business on Open Source without Selling Your Soul

- **Speakers:** Robert Hodges
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 11:35 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5320-build-a-great-business-on-open-source-without-selling-your-soul/)

#### Abstract

A profitable business is one of the best protections for commercial open source projects and communities that depend on them. Our talk draws on the experience of companies that pulled it off to explain how to do it for your own projects. We’ll discuss commercial models that actually work, giving back to the community, and gracefully collecting money for free software. We'll also discuss topics for larger projects like foundations and taking VC funding. It is possible to balance a strong belief in open source communities with making payroll every two weeks. We've done it and will share our secrets.

#### Related Links

- [ClickHouse](https://github.com/ClickHouse/ClickHouse)
- [Altinity Kubernetes Operator for ClickHouse](https://github.com/Altinity/clickhouse-operator)
- [DBeaver](https://github.com/dbeaver/dbeaver)
- [Percona Server](https://github.com/percona/percona-server)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LP3UNJ/feedback/)

---

### Pick My Project! Lessons Learned from Interviewing and Writing 20+ End User Case Studies

- **Speakers:** Bill Mulligan
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 12:05 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4474-pick-my-project-lessons-learned-from-interviewing-and-writing-20-end-user-case-studies/)

#### Abstract

Open source projects can promise the moon in their READMEs, but have you ever wondered what causes end users to actually adopt a project? Bill has interviewed over 20 companies in industries ranging from media to financial services about why they picked Cilium for their cloud native platform.
In this talk, he will reveal what end users truly want when adopting open source projects and what the forcing function was for each of them. You’ll hear firsthand accounts of why companies like DigitalOcean, Rabobank, and The New York Times chose to deploy a project to production, the specific benefits these organizations are reaping, from enhanced security and observability to improved performance and cost savings, and all the triumphs and tribulations along the way.
The talk will also teach other open source projects a process for creating impactful case studies to grow their community. By the end, the audience will how to grow their project with a case study program and why end users actually pick a project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TDVHW8/feedback/)

---

### The Psychology Behind Communities: Why Do We Really Contribute?

- **Speakers:** Mia Bajić
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 12:35 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4193-the-psychology-behind-communities-why-do-we-really-contribute-/)

#### Abstract

Have you ever wondered why people get involved in community work? If you think it's just about networking, think again! Let's talk about the deeper motivations rooted in our brains: from fast and slow thinking to the role of the amygdala, our basic human needs, and the impact of collective loneliness on society.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YPVECJ/feedback/)

---

### Six Degrees of Kevin Bacon - Open Source Community Edition

- **Speakers:** Lori Lorusso
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 13:05 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4715-six-degrees-of-kevin-bacon-open-source-community-edition/)

#### Abstract

The open source community can be siloed at times. People tend to ‘stay in their lane’ and don’t realize what they may be missing out on by not expanding their network. I know time is limited and it’s impossible to participate in every community so how do you become like Kevin Bacon? How do you set yourself up to be connected to people in various communities that you may be able to help or vice versa without being present at every meeting? I’m going to show you how you can channel your inner Kevin Bacon and learn how to expand your network like your funding counted on it!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J7YML7/feedback/)

---

### Unearthing the impact of survivorship bias on women in FOSS to build more inclusive communities

- **Speakers:** Imma Valls, julia lamenza
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 13:35 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5103-unearthing-the-impact-of-survivorship-bias-on-women-in-foss-to-build-more-inclusive-communities/)

#### Abstract

Open-source software thrives on diverse perspectives, yet women remain significantly underrepresented in FOSS communities.
While we celebrate women who've "made it"—and their visibility is vital—survivorship bias hides a crucial truth: up to half leave tech by age 35, women exit at a higher rate than men, and many never even join the field.
This talk delves into the concept of survivorship bias—the tendency to focus on successful individuals while ignoring those who faced barriers—and how it impacts women in open source. You’ll learn how this bias skews community perceptions, perpetuates systemic challenges, and limits opportunities.
By examining barriers like unwelcoming dynamics, recruitment biases, and a lack of mentorship, you'll understand why many are deterred before or during their FOSS journeys. You'll also learn how survivorship bias interacts with intersectionality, compounding challenges for women of color, LGBTQ+ individuals, and others.
We’ll also explore examples of communities and initiatives that successfully counter these trends, demonstrating allyship's role in building equitable environments. Finally, drawing on research and real-world examples, we’ll propose actionable steps to create a more inclusive and welcoming FOSS landscape for all.
Whether you’re a contributor, maintainer, or community leader, this session will give you a deeper understanding of the problem and tangible ways to drive change in your circles.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ANAKAL/feedback/)

---

### Open Source in Industrial Control Systems: A Cultural Challenge

- **Speakers:** Davíð Berman
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 14:05 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6528-open-source-in-industrial-control-systems-a-cultural-challenge/)

#### Abstract

My name is David Berman. I am an electrician by trade, not a programmer by profession, but I have ventured into the world of programming out of necessity and conviction. My journey into this realm has been fueled by a desire to challenge the prevailing norms of an industry heavily skewed toward proprietary, enterprise-oriented solutions. Specifically, I have worked to advocate for open-source, cost-effective methods to control city streetlights and other industrial control systems traditionally dominated by expensive and exclusive technologies.
During my talk I would like to share my newest project, Gungnir:
https://github.com/davidjrb/gungnir
This journey has been far from easy. The resistance to change in this space is significant, and the challenges are both technical and cultural. One of the key barriers is the entrenched power of profit-driven opponents, including corporate lobbyists and those with vested interests in maintaining the status quo. These forces often stifle innovation and prevent the adoption of solutions that could benefit society as a whole by reducing costs and fostering collaboration.
Another challenge comes from within the very community I advocate for. Despite the immense potential of open-source solutions, there is a tendency among many non-programmers—particularly those in traditional trades or management roles—to dismiss these solutions out of hand. This is often due to a lack of familiarity with the technology or misconceptions about its reliability and scalability. Bridging this gap requires not only technical expertise but also the ability to communicate the value and viability of open-source approaches in terms that resonate with a broader audience.
In my talk, I aim to explore these challenges in depth, sharing insights from my own experience as a non-programmer navigating a highly technical field. I will discuss the hurdles faced by the open-source community when advocating for transparency, collaboration, and cost-efficiency in an industry often resistant to such ideals. I will also highlight strategies to foster greater acceptance and collaboration between open-source advocates and those unfamiliar with or skeptical of these technologies.
Ultimately, my goal is to spark a dialogue about how we, as a community, can better advocate for open-source solutions in industrial and civic systems, ensuring that they are not only adopted but also embraced as a viable and beneficial alternative to proprietary models. By sharing stories, challenges, and strategies, I hope to inspire others—whether programmers, non-programmers, or industry professionals—to join this important movement.
Thank you for having me. 
I look forward to seeing you all 14:00, Saturday, 1. February in Baudoux - UB5.230

#### Related Links

- [Gungnir](https://github.com/davidjrb/gungnir)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9YGYYF/feedback/)

---

### How a City Platform Became a Global Community

- **Speakers:** Carolina Romero Cruz
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 14:35 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5458-how-a-city-platform-became-a-global-community/)

#### Abstract

Picture this: an open source digital democracy platform, launched by a city government, that quickly outgrows its municipal roots and becomes a global movement. Decidim started in 2016 as a tool for participatory processes in Barcelona, but its community expanded worldwide, with users in diverse cultural and political contexts. How do you scale such a project while preserving its democratic integrity?
In this session, we’ll dive into Decidim’s evolution, focusing on the governance challenges and triumphs of managing a rapidly growing, decentralized community. We’ll explore how Metadecidim—our "eat your own dog food" instance—facilitated this transition, enabling collaborative decision-making through open assemblies and processes. We’ll also discuss how Decidim’s unique social contract ensures transparency and accountability in everything from feature development to project governance.
This session is for you if you’re interested in the nuts and bolts of scaling participatory governance of free software projects.

#### Related Links

- [Metadecidim, the democratic community managing the Decidim project in all its dimensions](https://meta.decidim.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J8APLX/feedback/)

---

### From Side Projects to Sustainable Open Source

- **Speakers:** Orhun Parmaksız
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 15:05 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5498-from-side-projects-to-sustainable-open-source/)

#### Abstract

Ever wondered what it's like to maintain open source projects full-time?
In this talk, I'll share my journey from hobbyist to full-time open source maintainer, offering insight into the challenges and rewards of turning passion projects into a career.
Join me as I walk you through my journey, motivation, challenges, and tips for:

Building a community around your open source project
Increasing visibility and attracting contributors
Navigating social media and livestreaming to grow your audience

And more! Along the way, I'll share insights from other maintainers, highlighting what works and what doesn't.
Blood, sweat, and code — it's all here, for the love of open source!

#### Related Links

- [GitHub (@orhun)](https://github.com/orhun)
- [YouTube (@orhundev)](https://www.youtube.com/@orhundev)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QH8YKC/feedback/)

---

### Empowering Communities and Local Tech Companies with Government-Supported FOSS Localization Project

- **Speakers:** Open Culture Foundation, Ian Liu
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 15:35 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6178-empowering-communities-and-local-tech-companies-with-government-supported-foss-localization-project/)

#### Abstract

Since 2022, the Open Culture Foundation (OCF) has been collaborating with Taiwan’s Ministry of Digital Affairs (MoDA) and STEPS (a local tech company) on government-funded localization projects. These initiatives aim to make civic tech and open-source tools more accessible in Taiwan while enabling international projects to take root and thrive locally.
As a coordinator, OCF has completely localized projects such as GOV.UK Notify, GOV.UK Forms, Matrix Client (Element Series), IRMA, Yivi, Standard for Public Code, Bitwarden, Nextcloud, FreeOTP, GIMP, and Mattermost. Some of these projects have been contributed back to their upstream repositories, while others have evolved into localized solutions tailored to Taiwan's needs. OCF’s efforts focus on three key areas to ensure government funding provides not only financial support but also a foundation for sustainable development.
This talk will explore these three main focus areas:


Optimizing the Government Perspective on Open Source
    Educating government officials about the nature of open-source communities, their collaboration models, and the unique attributes of various international open-source projects. OCF also developed a collaborative glossary process to bridge communication gaps among stakeholders and ensure consistent terminology usage.


Collaboration Among Taiwan’s Communities
    Partnering with Taiwan’s L10N community, OCF established structured review processes to meet the government’s high standards for quality and timeliness. Over three years, OCF conducted two major surveys during COSCUP. One survey identified critical open-source projects needed in Taiwan, while the other focused on addressing challenges that hinder contributions, aiming to encourage broader participation.


Engagement with Local Industry and International Communities
    Although Taiwanese tech teams are highly skilled, many are unfamiliar with the culture of open-source contributions. OCF facilitated understanding of licensing, contribution practices, and engagement with upstream communities. For example, OCF helped Mattermost report and resolve a date display bug in Chinese (CJK) scripts and worked with upstream communities to address significant differences between Simplified and Traditional Chinese, including grammar and linguistic nuances.


Localization is not merely about technical translation; it is a strategic approach to connecting governments, communities, and international open-source projects. This talk will share OCF’s experiences in bridging these gaps and invite Community DevRoom participants to exchange ideas on how to effectively integrate open-source projects into their respective countries.

#### Related Links

- [Weblate for This Project](https://weblate.steps.tw/)
- [FreeOTP Andriod merged Pull-Request](https://github.com/freeotp/freeotp-android/pull/415#event-15353569855)
- [GitHub account for this Project](https://github.com/moda-l10n)
- [Standard-for-public-code community-translations-standard 0.7 merged Pull-Request](https://github.com/standard-for-public-code/community-translations-standard/pull/43#event-15434376526)
- [Moda / L10n Project Contribution for Mattermost](https://translate.mattermost.com/user/moda-l10n/)
- [Moda / L10n Contribution for Bitwarden](https://crowdin.com/profile/moda-l10n)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8KPWUR/feedback/)

---

### Disability Inclusion is Us: Building Inclusive Open Source Communities Through Intentional Action

- **Speakers:** Brayan Kai Mwanyumba
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 16:05 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4782-disability-inclusion-is-us-building-inclusive-open-source-communities-through-intentional-action/)

#### Abstract

In today's world, where disability affects a significant percentage of the population, it is crucial for open-source communities to address the challenges faced by persons with disabilities (PWDs) and work towards their inclusion. This talk will delve into practical measures such as referral programs, internal disability disclosures, and integrating disability into existing agendas rather than treating it as a separate issue. We will dive into disability mainstreaming with a focus on its role in promoting universal design and inclusivity. Attendees will gain insights into establishing disability mainstreaming committees, formulating action plans, implementing best practices, and monitoring and evaluating progress.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/H7RLK3/feedback/)

---

### Talking to Robots: Uses and Abuses of LLMs in Communities

- **Speakers:** David Allen
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 16:35 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5215-talking-to-robots-uses-and-abuses-of-llms-in-communities/)

#### Abstract

Large language models (LLMs) may represent a shift in how open source communities support their members. This talk explores the nuanced and evolving role of LLMs in fostering community engagement. Specialized companies offer tailoring of LLM and automation of responses to technical questions. We will explore a range of adoption options from cautious, opt-in approaches confined to specific channels to fully embracing LLMs for first-line support across forums. These strategies raise questions like:

Could automation stifle organic, person-to-person connections in communities, or can it expedite learning and enable meaningful contributions from newcomers?
How do LLMs reshape the balance between in-person and digital interactions, and what does this mean for the future of community building?
Are LLMs the natural evolution of IRC-era bots, or will they alter the patterns of open source collaboration?

We’ll look at case studies from real communities. Attendees will get actionable insights for navigating the adoption of LLMs in their own communities, striking a balance between automation and authentic human connection.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3DNYE7/feedback/)

---

### Open Source Governance for Software Engineers

- **Speakers:** Tobie Langel
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 17:05 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6118-open-source-governance-for-software-engineers/)

#### Abstract

The goal of this presentation is twofold:
Firstly, we want to demystify open source project governance. Do you freeze when you hear the term governance? Do you blindly copy and paste the governance of other projects hoping it works for your project too? Do you struggle to keep governance up to date or aligned with what’s actually going on in the project? You’re not alone.
Secondly, we want to provide a simple, practical, and proven approach to writing governance that’s directly inspired from coding best practices. The very same concepts that are used when writing code (e.g. Don’t Repeat Yourself, Keep It Simple, or Separation of Concerns) have direct application when authoring governance documents and create the same kind of positive outcomes: governance that is simple to understand, flexible, and and easy to maintain. You’ll never come back from thinking about governance as code.
By the time you leave this presentation, you’ll have an entirely new perspective on governance and will feel empowered by your ability to leverage your existing software engineering skills in this new domain.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DVMLDN/feedback/)

---

### Digital Public Goods - Incentivizing Collaboration

- **Speakers:** Mike Gifford
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 17:35 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4633-digital-public-goods-incentivizing-collaboration/)

#### Abstract

Digital Public Goods are often celebrated as open-source software, open data, open AI models, open standards, and open content. However, true public goods require more than openness—they demand active community governance, collective stewardship, and responsible contributions to thrive as shared resources.
While proprietary software sustains itself through licensing, support, and vendor lock-in, open-source software relies on a delicate balance of professional firms, organizational backing, and dedicated enthusiasts. The open model has fueled flexibility, innovation, and the global adoption of open technologies.
Yet, the rapid growth of "open" has not been matched by an equivalent rise in contributions or investments in maintenance. Discussions often prioritize licensing over the essential question: How do we, as a community, ensure that digital public goods are sustainable? This talk explores the responsibility of contributors, organizations, and users in building a resilient ecosystem for open technologies.

#### Related Links

- [UN: Digital Public Goods - Promoting open-source solutions for a more equitable world](https://www.un.org/techenvoy/content/digital-public-goods)
- [Digital Public Goods Alliance](https://www.digitalpublicgoods.net/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L9JGY9/feedback/)

---

### Become a Hiro

- **Speakers:** Addie Girouard
- **Room:** UB5.230
- **Day:** Saturday
- **Time:** 18:05 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5297-become-a-hiro/)

#### Abstract

Over 30 years ago, Neal Stephenson wrote about a pizza-delivering hacker who saved the digital world. Today, we're all facing our own L. Bob Rife – not through ancient Sumerian viruses, but through corporate consolidation and regulatory pressure threatening to end open source as we know it.
Our digital commons began as a frontier of freedom and innovation. Today giants are consolidating control over the infrastructure that shapes our digital world. The dark future seen in the franchise-owned streets of Snow Crash's America is coming. But Hiro showed us how to fight back: with skill, with allies, and with unwavering dedication to freedom. 
We're facing our own daemon – not ancient Sumerian, but modern corporate and regulatory control. The question is: Will you remain a pizza delivery driver, or will you become a Hiro?
The future of open source depends on your answer.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-community:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-community:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9XXYS/feedback/)

---

## Confidential Computing (11)

### Confidential Computing devroom welcome

- **Speakers:** Fritz Alder, Jo Van Bulck, Fabiano Fidêncio, Ilaria Battiston, Steffen Eiden
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 10:30 - 10:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6642-confidential-computing-devroom-welcome/)

#### Abstract

Welcome to the 6th iteration of the confidential computing devroom! In this welcome session, we will give a very brief introduction to confidential computing and the devroom, and we will give an honorable mention to all the folks that contributed to this devroom, whether they are presenting or not.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8BTXT8/feedback/)

---

### Confidential Computing’s Recent Past, Emerging Present, and Long-Lasting Future

- **Speakers:** Sal Kimmich
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 10:40 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5002-confidential-computing-s-recent-past-emerging-present-and-long-lasting-future/)

#### Abstract

As Confidential Computing (CC) continues to gain traction as a cornerstone of modern cybersecurity, understanding its trajectory—past, present, and future—is critical to its adoption and impact. This talk explores the evolution of CC, from its origins in securing sensitive workloads with Trusted Execution Environments (TEEs), to its growing intersection with broader cybersecurity disciplines such as supply chain security and threat modeling.
The session will highlight the need to effectively communicate CC's value across these disciplines, bridging technical advancements with practical applications. With the latest EU DORA directive mandating runtime data security, and the increasing need for mathematical unicity in sensitive data comparisons, the relevance of CC is more pressing than ever.
Attendees will learn:
A concise history of CC and its early drivers.
Current challenges and successes in embedding CC within complex cybersecurity frameworks.
Strategies for fostering adoption across diverse industries and regulatory landscapes.
A forward-looking vision for CC’s role in addressing the evolving threat landscape, particularly in areas demanding high assurance of data integrity and confidentiality.
Join us for a compelling narrative that positions Confidential Computing as a key enabler of secure and trustworthy systems in a rapidly changing world. Whether you’re a seasoned practitioner or new to CC, this session will provide actionable insights to integrate and advocate for CC in your security workflows.

#### Related Links

- [Confidential Computing Open Source Projects](https://confidentialcomputing.io/projects/current-projects/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QYVLDD/feedback/)

---

### Confidential Virtual Machines Demystified: A Technical Deep Dive into Linux Guest OS Enlightenment

- **Speakers:** Ankita Pareek, Archana Choudhary
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 11:05 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6168-confidential-virtual-machines-demystified-a-technical-deep-dive-into-linux-guest-os-enlightenment/)

#### Abstract

In an era where data breaches make headlines daily and cyber threats continue to evolve, Confidential Computing emerges as a game-changing paradigm for protecting sensitive workloads in the cloud. With the upcoming Digital Operational Resilience Act (DORA) in Europe mandating data protection in use, understanding Confidential Computing solutions is crucial for regulatory compliance. This talk explores the cornerstone of this technology: Confidential Virtual Machines (VMs), focusing on the two leading hardware technologies: AMD SEV-SNP and Intel TDX.
We delve into the intricacies of enlightening Linux guest OS images to work with these platforms, examining the architectural differences and specific requirements for each technology. Key technical aspects covered include secure boot implementation, measured boot processes, attestation mechanisms, and memory encryption strategies within Linux guest OS images. The discussion encompasses essential modifications needed for compatibility, current industry support, implementation challenges, and emerging trends. This comprehensive overview provides insights into the state-of-the-art of enlightened guest OS images for various Linux distros like Azure Linux, RHEL, Ubuntu, etc. and explores future directions in this rapidly evolving field of confidential computing.
This talk is designed for everyone - from developers, cloud architects and platform vendors to confidential computing enthusiasts.

#### Related Links

- [Azure Linux distribution in the process to support CVMs](https://github.com/microsoft/azurelinux)
- [Canonical's CVM support for tdx](https://github.com/canonical/tdx)
- [CVM introduction](https://www.redhat.com/en/blog/introduction-confidential-virtual-machines)
- [Azure cvm-guest attestation](https://github.com/Azure/confidential-computing-cvm-guest-attestation)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BXMGLE/feedback/)

---

### ManaTEE: an Open-Source Private Data Analytics Framework with Confidential Computing

- **Speakers:** Dayeol Lee
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 11:30 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5044-manatee-an-open-source-private-data-analytics-framework-with-confidential-computing/)

#### Abstract

In this talk, we introduce ManaTEE, an open-source framework designed to enable private data analytics for public research. Private data holds immense value not only for businesses but also for critical research domains like public health, economics, social sciences, and civic engagement. However, leveraging such data for analytics comes with significant privacy risks. ManaTEE aims to address these challenges by integrating a set of Privacy Enhancing Techniques (PETs), including confidential computing, to safeguard data privacy without compromising usability. The framework provides an interactive interface through JupyterLab, ensuring an intuitive experience for researchers and data scientists. We will showcase how Trusted Execution Environments (TEEs) ensure both data confidentiality and execution integrity, fostering trust between data owners and analysts. Furthermore, we will highlight how confidential computing can offer additional properties such as proof of execution, enabling researchers to demonstrate the reproducibility and integrity of their results through attestation. Finally, we discuss how ManaTEE simplifies deployment across various confidential computing backends, making secure and private data analytics both accessible and scalable for diverse use cases.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PDZVUU/feedback/)

---

### Supporting Confidential Computing on Arm with Open Source Software

- **Speakers:** Poirier Mathieu
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 11:55 - 12:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5761-supporting-confidential-computing-on-arm-with-open-source-software/)

#### Abstract

This session will present an end-to-end scenario to support confidential computing on Arm (CCA).  The first part will focus on a reference implementation stack that integrates firmware, operating system, virtual machine monitor and container environment on QEMU's SBSA platform.  From there we will present the verifier that runs in the cloud to attest security claims generated by the reference stack.  We will conclude by going over the tooling needed to compute initial Realm measurements and give an overview of a key broker proof-of-concept that works with the stack and verifier to deliver a secret payload.

#### Related Links

- [Documentation to build the CCA stack](https://linaro.atlassian.net/wiki/spaces/QEMU/pages/29051027459/Building+an+RME+stack+for+QEMU)
- [Project Veraison](https://github.com/veraison)
- [Realm measurement tool](https://github.com/veraison/cca-realm-measurements)
- [Key broker demonstration](https://github.com/veraison/keybroker-demo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9EFRN8/feedback/)

---

### Updates on Coconut SVSM: Secure Services and Stateful Devices for Confidential Virtual Machines

- **Speakers:** Stefano Garzarella, Oliver Steffen
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 12:20 - 12:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5412-updates-on-coconut-svsm-secure-services-and-stateful-devices-for-confidential-virtual-machines/)

#### Abstract

The Coconut community is actively developing the Secure VM Service Module (SVSM) to provide secure services and trusted device emulation for guest operating systems running in Confidential Virtual Machines (CVMs). Originally designed for AMD SEV-SNP, Coconut SVSM is evolving into a multi-platform solution, with ongoing efforts to integrate support for Intel TDX Partitioning.
This talk will dive into the current progress of Coconut SVSM, focusing on the emulation of devices such as the virtual Trusted Platform Module (vTPM), based on the reference implementation from the Trusted Computing Group (TCG). At this stage, the vTPM in Coconut SVSM is ephemeral, being re-manufactured with each boot. To unlock broader use cases, the community is working on introducing a persistent state for SVSM, enabling the vTPM to preserve its state across reboots. This enhancement will also allows us to support UEFI variable store to support Secure Boot.
Achieving this persistence requires storing encrypted state securely on the untrusted host, with early boot-time attestation to decrypt and validate the state. This process raises several technical challenges that we are actively tackling.
Join us to explore the latest progress in Coconut SVSM, the challenges we’ve overcome, and the exciting opportunities still ahead.

#### Related Links

- [COCONUT SVSM](https://github.com/coconut-svsm/svsm)
- [PoC with SVSM, KBS proxy, virtio-blk device, and stateful vTPM](https://github.com/stefano-garzarella/snp-svsm-vtpm)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MLWPFY/feedback/)

---

### Trust No One: Secure Storage with Confidential Containers

- **Speakers:** Aurélien Bombo
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 12:45 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5299-trust-no-one-secure-storage-with-confidential-containers/)

#### Abstract

If you are processing and storing sensitive data in the cloud, can you really trust anyone (including the cloud)? The answer is no. Confidential Containers (CoCo) is a CNCF project that leverages Trusted Execution Environments (TEEs) to tackle this challenge. A critical aspect in this effort is providing secure and confidential storage solutions that can be seamlessly deployed across cloud providers.
This session explores the implementation of trusted storage in CoCo, highlighting key aspects such as Kubernetes storage drivers, device virtualization, and the role of attestation in secure key release and data encryption. We also demonstrate how we prevent attackers from injecting data into the TEE using the CNCF Rego policy language.
Overall, we aim to show how cloud providers and end users can securely store and protect sensitive data, enabling the adoption of confidential computing across numerous use cases.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QLULHW/feedback/)

---

### RA-WEBs: Remote Attestation for WEB services

- **Speakers:** Yoshimichi Nakatsuka
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 13:10 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4529-ra-webs-remote-attestation-for-web-services/)

#### Abstract

Data theft and leakage, caused by external adversaries and insiders, demonstrate the need for protecting user data. Trusted Execution Environments (TEEs) offer a promising solution by creating secure environments that protect data and code from such threats. The rise of confidential computing on cloud platforms facilitates the deployment of TEE-enabled server applications, which are expected to be widely adopted in web services such as privacy-preserving LLM inference and secure data logging. One key feature is Remote Attestation (RA), which enables integrity verification of a TEE. However, compatibility issues with RA verification arise as no browsers natively support this feature, making prior solutions cumbersome and risky. 
To address these challenges, in this talk, we present RA-WEBs (Remote Attestation for Web services), a novel RA protocol designed for high compatibility with the current web ecosystem. RA-WEBs leverages established web mechanisms for immediate deployability, enabling RA verification on existing browsers. We will show preliminary evaluation results and highlight open challenges when introducing RA to the web.

#### Related Links

- [RA-WEBs preprint](https://arxiv.org/abs/2411.01340)
- [RA-WEBs repository](https://github.com/akakou/ra-webs/tree/release/achive-for-paper-v1)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UULG8K/feedback/)

---

### Spock : a software-based RISC-V TEE

- **Speakers:** jip helsen
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 13:35 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5966-spock-a-software-based-risc-v-tee/)

#### Abstract

Securing embedded devices, particularly those with minimal resources, presents a unique and pressing challenge. Conventional approaches to Trusted Execution Environments (TEEs) often require specialized hardware or substantial system resources, leaving low-end devices vulnerable to breaches. The need for a lightweight, efficient solution that bridges this gap is greater than ever in today’s interconnected world.  
Introducing Spock
Through the development of Spock, we have created a versatile and efficient Trusted Execution Environment (TEE) tailored for RISC-V embedded devices. By relying solely on Physical Memory Protection (PMP) for isolation and requiring only machine and user modes as specified in the RISC-V privileged instruction set, Spock delivers robust security without relying on any specialized hardware.  
At the core of Spock’s architecture is the Security Manager (SM), which plays a key role in managing enclave data and buffer permissions. The SM enables Spock to efficiently virtualize buffers and dynamically allocate PMP entries, providing a flexible and scalable approach to memory isolation. By leveraging this abstraction, Spock can create virtual enclaves that surpass hardware-imposed limitations, such as the number of PMP entries.  
Core Features and Capabilities
Spock’s minimalist API design delivers essential security functions, including secure execution and attestation. This design supports:  

Virtualization of critical operations while maintaining a minimal Trusted Computing Base (TCB).  
Integration into very low resource embedded devices. 
Both relocatable and fixed enclaves, offering flexibility for diverse use cases.  

Why Spock Matters
Spock’s design represents a modern, efficient solution for secure computing in low-resource embedded devices. Its ability to combine robust security with minimal hardware requirements makes it uniquely suited for the demands of today’s connected world, ensuring that even the smallest devices can operate securely.
Available at : https://github.com/jiphelsen/Spock

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZAXWJU/feedback/)

---

### Running Mushroom on Intel TDX

- **Speakers:** Tom Dohrmann
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 14:00 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5864-running-mushroom-on-intel-tdx/)

#### Abstract

Mushroom is a project for securely running Linux workloads in attestable, integrity-protected environments with a minimalistic TCB. Mushroom depends on TEEs to provide integrity guarantees for data in use. It was initially developed for AMD SEV-SNP, but it recently gained support for running on Intel TDX as well. This talk will explore some of the required changes and discuss how the differences between AMD SEV-SNP and Intel TDX informed some of the design decisions.

#### Related Links

- [Mushroom on GitHub](https://github.com/Freax13/mushroom)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YTLNAE/feedback/)

---

### Confidential Computing devroom lightning talks

- **Speakers:** Claudio Imbrenda, Steffen Eiden, Kuniyasu Suzaki
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 14:20 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6727-confidential-computing-devroom-lightning-talks/)

#### Abstract

We will close the devroom with lightning talks that will serve as a great conversation starter during the lunch break.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-confidential:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-confidential:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PDZ9J3/feedback/)

---

## Containers (21)

### Cache me if you can: P2P Image Sharing in Kubernetes with Spegel

- **Speakers:** Philip Laine
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4934-cache-me-if-you-can-p2p-image-sharing-in-kubernetes-with-spegel/)

#### Abstract

The ability to pull container images quickly and reliably is critical for workload deployment and scaling. Pulling images from external registries can be slow, inefficient, and prone to failure due to network issues or downtime. In this session, we will explore different strategies for speeding up container image pulling in Kubernetes. We will compare the benefits and trade-offs of different image caching approaches, such as leveraging Harbor, preloading images on machine images, or adopting Spegel. 
We will uncover how Spegel works seamlessly with Kubernetes to provide automatic local caching of images without explicit configuration, reducing the impact of external registry downtime and avoiding rate-limiting issues. Then, demonstrate how Harbor can be used as a pull through mirror.  Attendees will learn to deploy these solutions to optimize their Kubernetes workloads, decrease pod startup times, and improve the performance of edge node deployments.

#### Related Links

- [Spegel](https://github.com/spegel-org/spegel)
- [Containerd](https://github.com/containerd/containerd)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/77VSPL/feedback/)

---

### A new cgroup cpu.max.concurrency controller interface file

- **Speakers:** Mathieu Desnoyers
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 11:00 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6283-a-new-cgroup-cpu-max-concurrency-controller-interface-file/)

#### Abstract

This lightning talk discusses an ongoing effort to add a new cpu.max.concurrency interface file to the Linux cgroup CPU controller to facilitate expressing constraints on the number of CPUs which can be used concurrently by threads belonging to the cgroup.
This new interface file will define the maximum number of concurrently running threads for the cgroup. Extend the scheduler to track the number of CPUs concurrently used by the cgroup, and prevent migration when the number of concurrently used CPUs is above the maximum threshold.
The purpose of this new interface is to limit the amount of resident memory needed for userspace per-CPU data, and tune the number of worker threads to the cgroup constraints.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EUTATU/feedback/)

---

### Bringing application containers to Incus

- **Speakers:** Stephane Graber
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 11:10 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5742-bringing-application-containers-to-incus/)

#### Abstract

At last year's FOSDEM, I introduced the Incus project, what it was and what it would become over the following year. One of the main highlights and that which gathered the most interest was the support for OCI application containers.
It's now been a few months since Incus first gained support for running application containers, alongside its existing system container and virtual machine support. The work needed to get this done was actually pretty simple thanks to other projects like skopeo and umoci which Incus leverages to handle the OCI images.
In this presentation, we'll be looking at why we wanted to add OCI containers to Incus in the first place, how it was implemented, some of the differences from other implementations and what's planned next to make this even more useful.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/H9YKCQ/feedback/)

---

### Writing a kubernetes controller… But in Rust

- **Speakers:** Danil
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 11:30 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4189-writing-a-kubernetes-controller-but-in-rust/)

#### Abstract

Kubernetes API server provides a standardized extension layer, called CustomResourceDefinitions (CRDs). This is a go-to contract, used to implement a controller with added functionality. There are some standard libraries, like controller-runtime and kubebuilder, written in Go, built to integrate with it natively. But what about other languages, like Rust?
How would a controller look like written in Rust? Why would you want to consider writing one? What benefits or downsides this approach might have? And how can a Rust controller still benefit from an established Go ecosystem? 
We will explore these topics, compare implementations and share experience over other projects using Rust within kubernetes.
Projects:
- https://github.com/kube-rs/kube
- https://github.com/kube-rs/kopium
- https://github.com/rancher-sandbox/cluster-api-addon-provider-fleet
- https://github.com/crust-gather/crust-gather

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XUG8UM/feedback/)

---

### State of Checkpoint/Restore in Kubernetes

- **Speakers:** Adrian Reber
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 11:50 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4326-state-of-checkpoint-restore-in-kubernetes/)

#### Abstract

In 2015 a ticket was opened asking for container migration support in Kubernetes. In 2022 the first minimal support to checkpoint and restore containers was added to Kubernetes 1.25 as an Alpha feature. In Kubernetes 1.30 (2024 ) the checkpoint/restore support graduated to the Beta phase.
In this session I want to give an overview what is currently possible in regards to checkpointing and restoring containers in Kubernetes. I want to give details in what way the containerd and CRI-O implementations differ and I want to describe the future plans for checkpoint/restore in Kubernetes.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DGJGUH/feedback/)

---

### Immutable All the Way Down - using System Extensions to ship Kubernetes

- **Speakers:** Thilo Fromm
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 12:20 - 12:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4677-immutable-all-the-way-down-using-system-extensions-to-ship-kubernetes/)

#### Abstract

There are many ways to get container runtimes and Kubernetes on a node, all with their benefits and drawbacks. This talk will present shipping Kubernetes as a system extension with systemd-sysext – a self-contained, immutable, verifiable, distribution independent disk image. We’ll also look into automated in-place updates, both from the OS as well as the Kubernetes side. 
The talk includes multiple live demos, from a single node deployment to cover sysext basics to a full-blown Kubernetes cluster deployed with ClusterAPI which we’ll then update live. While all demos will use Flatcar Container Linux - an immutable special purpose OS optimised for container workloads – the mechanisms demonstrated are distro independent and cloud be used on any Linux distribution.

#### Related Links

- [Project landing page](https://www.flatcar.org/)
- [Flatcar documentation](https://www.flatcar.org/docs/latest)
- [Flatcar Linux Distribution Development landing page](https://github.com/flatcar/flatcar)
- [Code and scripts for the talk's demos](https://github.com/flatcar/flatcar-demos/tree/main/CAPO-sysext)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/E9HWGD/feedback/)

---

### Play with Kube using Podman

- **Speakers:** Mario Loriedo
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 12:50 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5759-play-with-kube-using-podman/)

#### Abstract

Accessing a Kubernetes cluster for the first time can be daunting. But that’s the price for testing Deployments, Volumes, and other Kubernetes objects, right? Nope. There is an easier way that doesn’t entail learning how to deploy a Kubernetes cluster.
One of the least-known commands of Podman is kube play, and it’s fantastic. It works as kubectl apply and supports the same objects but doesn’t need a Kubernetes cluster. It supports Pods, Deployments, Volumes, ConfigMaps, and many other Kubernetes resources and runs on Linux, macOS, and Windows. It has some additional features compared to kubectl, such as using local images.
This talk will discuss using kube play and its alter-ego kube generate to simplify Kubernetes’ first experiences.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3JHRGU/feedback/)

---

### Comparing Fuchsia components and Linux containers

- **Speakers:** Claire Gonyeo
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 13:10 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5381-comparing-fuchsia-components-and-linux-containers/)

#### Abstract

Fuchsia is a new (non-Linux) operating system from Google, and one of the key pieces of Fuchsia's design is the component framework. Components on Fuchsia have many similarities with some of the container solutions on Linux (such as Docker): they both fetch content addressed blobs from the network, assemble those blobs into an isolated filesystem structure that holds all the dependencies necessary to run some piece of software, and launch namespaced processes with that created directory as its root.
The most interesting details are where these two projects diverge. Both have different use cases and requirements, which leads to different strengths between the systems. This talk will largely be focusing on where and why these two similar technologies diverge.
Relevant links:
- Fuchsia's source code
- Fuchsia's code review
- Getting started page

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JXADEZ/feedback/)

---

### Declarative Networking in Declarative World, ver. 2025

- **Speakers:** Mateusz Kowalski
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 13:40 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4077-declarative-networking-in-declarative-world-ver-2025/)

#### Abstract

Since the beginning of time, declarative APIs have been driving everything that can happen inside a Kubernetes cluster. Predefined CRDs, operators defining custom CRDs, everything is about declarative APIs. Write your YAML once, deploy it, forget it. That’s how you create a cluster, that’s how you deploy your workload.
But is it, for real, as simple as it sounds? How do you bring declarativeness to the imperative world? In the current state of things, host networking is one huge imperative nightmare. So how to happily marry an old-school Network Manager and brand new Kubernetes API?
Over the years we were working on the NMstate project to provide you with a Declarative Network API, allowing you to manage host networking in a declarative manner.
In 2025 we are coming back with brand new features. Based on the feedback, we focused on air-gapped and big clusters – think hundreds of nodes with hundreds of VLANs each. We also happily married K8s and KubeVirt – no matter what your workload is, containers or VMs, NMstate is there for you.
Not only a project update – we will also show you how the Kubernetes cluster with NMState Operator manages networking on the nodes it deploys. It may sound like a chicken and egg situation, but trust us, it is not. Last but not least, we show how it protects itself from applying destructive network changes potentially taking your cluster down.
Join us and discover what’s new in the world of complex network topologies.

#### Related Links

- [Nmstate - CLI tool that manages host networking settings](https://github.com/nmstate/nmstate)
- [kubernetes-nmstate - Declarative node network configuration driven through Kubernetes API](https://github.com/nmstate/kubernetes-nmstate)
- [NetworkManager - Linux network configuration tool suite](https://networkmanager.dev)
- [KubeVirt - Virtualization API for Kubernetes](https://kubevirt.io)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8TDUDH/feedback/)

---

### Incus cluster: private cloud with system containers

- **Speakers:** Jérémie Grauer
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6420-incus-cluster-private-cloud-with-system-containers/)

#### Abstract

Incus is a next-generation manager for system containers, application containers, and virtual machines, forked from Canonical's LXD in August 2023.
This presentation explores the evolution of LXD/Incus, with a focus on clustering and its capabilities for natively managing both stateless and stateful workloads.
Drawing on real-world experience as a system architect at a cloud provider using LXD/Incus since 2016, we will examine the technologies underpinning Incus, including OVN-based networking and flexible storage configurations. The session will also showcase the key commands and workflows for building and managing an Incus cluster, with practical examples to highlight best practices.
This session is intended for system administrators, DevOps engineers, and container enthusiasts seeking to enhance their understanding of Incus and its role within the modern container ecosystem.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7USMAZ/feedback/)

---

### Implementing a rootless container manager from scratch

- **Speakers:** Luca Di Maio
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5022-implementing-a-rootless-container-manager-from-scratch/)

#### Abstract

An introduction on the basic concepts underpinning a container manager:
understanding what OCI images are, how they’re structured, and how to use them as rootfs. From there, we’ll dive into the core Linux primitives that make rootless containers possible: namespaces for isolation, UID/GID mappings and dropping privileges.
The talk will use my project Lilipod https://github.com/89luca89/lilipod as an example on what and how all of this has been implemented

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VAZSTL/feedback/)

---

### Sandbox IDs with Landlock

- **Speakers:** Mickaël Salaün
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6071-sandbox-ids-with-landlock/)

#### Abstract

Landlock is an unprivileged access control designed to create security sandboxes (i.e. Landlock domains). We are working on observability interfaces to identify the cause of denied requests, which require logging (audit) and a dedicated user space interface to get information about Landlock domains.
In this talk, we'll explain the challenges to tie log entries with running processes and their properties, considering the unprivileged approach of Landlock. This led us to create a new kind of ID to tie processes to Landlock domains. We are now working on a new user space interface to safely get information about these Landlock domains. Thanks to its flexibility, Landlock could be leveraged by container runtimes to better isolate processes and now also to cleanly identify them. We'll talk about the container labels/IDs challenges, how Landlock could help, and the potential limitations.

#### Related Links

- [Landlock website](https://landlock.io/)
- [Landlock documentation](https://docs.kernel.org/userspace-api/landlock.html)
- [GitHub issue: Identify tasks' domain](https://github.com/landlock-lsm/linux/issues/26)
- [LPC 2018: Container IDs](https://lpc.events/event/2/contributions/215/)
- [LPC 2024: Immutable process tags for container tracking](https://lpc.events/event/18/contributions/1805/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VD8TZC/feedback/)

---

### Running Containers Under Systemd: Exploring Podman Quadlet

- **Speakers:** Axel STEFANINI
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 15:30 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5383-running-containers-under-systemd-exploring-podman-quadlet/)

#### Abstract

Containers are typically deployed in Kubernetes clusters. But at a smaller scale, on a single-node server, or for development purposes, Kubernetes will be overkill. What’s the recommended way to run a fully autonomous application with several interacting containers in these cases?
The answer is systemd. It can orchestrate containers as is an already running process manager, and containers are just child processes. It’s a perfect fit for running containerized workloads without human intervention.
The concept of Quadlet has been introduced in Podman v4.4.0. It’s a systemd-generator that writes and maintains systemd services using Podman. It can manage containers lifecycle (start, stop, restart), volumes, pods, deployments etc. via systemd. The name comes from the following: “What do you get if you squash a Kubernetes kubelet? A quadlet”. Both system and user systemd units are supported to deploy applications without root privileges.
In this presentation, we will discuss what are Podman Quadlets and demonstrate how Podman Kubernetes features can be associated with it to deploy a fully autonomous application.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/88WUVF/feedback/)

---

### Could we actually replace containers?

- **Speakers:** Dan Phillips
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 15:50 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6123-could-we-actually-replace-containers-/)

#### Abstract

The now infamous quote: 
“Webassembly on the server is the future of computing” – Solemn Hykes, creator of Docker
But really, what would it take? I'm talking about FULL feature parity. This talk will go deep into how we looked at and attempted to solve every single piece of this very large problem.
While containers have been pivotal in cloud computing, offering isolated environments for applications, they bring notable drawbacks. These include substantial overhead, resulting in larger, less efficient deployments and startup times, and a dependency on the underlying OS for security, posing potential vulnerabilities.
WebAssembly (Wasm) addresses these challenges, and this talk will introduce the open-source project Boxer (https://boxer.dev), which offers tooling for taking existing containerized workloads and definitions, and creating near-universally deployable Wasm distributions (“Boxes”) offering roughly the same environment, with all the benefits of the WebAssembly target. Wasm, a compact binary instruction format, enables lightweight, sandboxed execution, significantly reducing overhead compared to traditional containers. This leads to enhanced performance and smaller, more efficient deployments, ideal for cloud computing. Additionally, Wasm's memory-safe, isolated execution environment provides superior security, independent of the OS. Thus, Wasm, with its blend of efficiency and security, emerges as not just an alternative, but a substantial improvement over container technology for cloud deployments.
Marcotte (https://github.com/dphilla/marcotte) -- the underlying tool for virtualizing layers of system functionality -- allows us to make safe, sandboxed, discrete, and composable system functionality, by leveraging Rust's memory safety model, and the inherent properties of WebAssembly.
This talk will critically examine this new technology, its approach, benefits, and existing limitations compared with containers, and its path forward as a new standard in cloud infrastructure.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XYU3HW/feedback/)

---

### DNF manifest: A new way to replicate your package configuration, debug customer issues, manage container files and more

- **Speakers:** Jan Kolarik
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 16:10 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5354-dnf-manifest-a-new-way-to-replicate-your-package-configuration-debug-customer-issues-manage-container-files-and-more/)

#### Abstract

Managing packages across systems and containers can be complex, especially when debugging issues or ensuring consistent deployments.
This short presentation introduces the manifest plugin for the DNF package manager, a tool that simplifies such workflows by capturing system package states into YAML-based manifest files. These files enable users to replicate environments, debug customer issues by mirroring setups, and streamline container builds with transparent, manifest-driven package management.

#### Related Links

- [libpkgmanifest](https://github.com/rpm-software-management/libpkgmanifest)
- [dnf](https://github.com/rpm-software-management/dnf)
- [Testing COPR repository](https://copr.fedorainfracloud.org/coprs/rpmsoftwaremanagement/manifest-plugin-testing/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DUES3C/feedback/)

---

### Kubernetes outside of the cloud: Lessons learned after 3 years

- **Speakers:** Nadia Santalla
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 16:20 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4387-kubernetes-outside-of-the-cloud-lessons-learned-after-3-years/)

#### Abstract

Kubernetes is commonly run on cloud, and even more commonly on its managed form. However, self-managing k8s on your own metal is also fun!
In this talk I will walk through some of the challenges I've found while doing this for the last three years, and share what are the tools I've used to conquer them, such as kubeadm, cilium, metallb, stateless-dns (external-dns + powerdns), and others.

#### Related Links

- [MetalLB](https://metallb.io/)
- [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
- [Cilium](https://docs.cilium.io/en/stable/)
- [Stateless-dns](https://github.com/txqueuelen/stateless-dns)
- [Kine](https://github.com/k3s-io/kine)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DTPAXH/feedback/)

---

### Syd+Youki=Syd-OCI: Introduction to a Secure Container Runtime for Linux

- **Speakers:** Ali Polatel
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 16:50 - 17:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4920-syd-youki-syd-oci-introduction-to-a-secure-container-runtime-for-linux/)

#### Abstract

In this talk, I will introduce Syd-OCI, a secure OCI container runtime for Linux systems (version 5.19 and above). Syd-OCI seamlessly integrates the advanced sandboxing capabilities of Syd -- our rock-solid application kernel designed for sandboxing applications -- into containerized environments by leveraging Youki, a modern container runtime written in Rust.
Syd-OCI operates as a thin wrapper around Youki, utilizing Youki's robust OCI implementation while replacing its default executor with a custom one that runs container processes under Syd's comprehensive sandboxing framework. This integration allows Syd-OCI to provide enhanced security features -- such as Path Sandboxing, Execution Control with SegvGuard, Network Sandboxing, and advanced mechanisms like Lock Sandboxing and Proxy Sandboxing -- within standard OCI-compliant containers.
The presentation will cover Syd-OCI's key features:

Integration of Syd and Youki: How Syd-OCI combines Syd's advanced sandboxing mechanisms with Youki's efficient OCI runtime, creating a secure container runtime without requiring extra privileges, SETUID binaries, or privileged kernel context.
Technical Architecture: An in-depth look at how Syd-OCI replaces Youki's default executor with a custom executor that runs commands under Syd, enabling seamless integration of Syd's security features into container workflows.
Configuration and Usage: Guidance on setting up Syd-OCI with container platforms like Docker, Podman, and CRI-O, including configuring the Syd sandbox using profiles and integrating sandbox configurations into container images.
Advanced Sandboxing and Verified Images: Showcasing practical use cases where Syd-OCI enhances container security through advanced features like Force Sandboxing for verified execution and Crypt Sandboxing for transparent file encryption using AES-CTR. We will explore how these mechanisms provide integrity verification for container images and binaries, ensuring that only trusted and securely encrypted code is executed within containers, thereby strengthening protection against unauthorized modification and data breach.

Attendees will gain insights into the design and implementation of Syd-OCI, understanding how the integration of Syd and Youki provides a secure, efficient, and practical solution for container security. This talk will illustrate how Syd-OCI can be seamlessly integrated into existing container workflows, enhancing security without compromising performance or compatibility, and adhering to the UNIX philosophy of doing one thing well with the least privilege necessary.

#### Related Links

- [Syd homepage](https://sydbox.exherbolinux.org)
- [Syd-OCI manpage](http://man.exherbolinux.org/syd-oci.1.html)
- [Syd source code](https://gitlab.exherbo.org/sydbox/sydbox)
- [Syd CTF](https://ctftime.org/event/2178)
- [Article: State of Sandboxing on Linux](https://git.sr.ht/~alip/syd/tree/main/item/doc/toctou-or-gtfo.md)
- [PDF](https://gitlab.exherbo.org/sydbox/sydbox/-/blob/main/doc/talks/2025-Syd-OCI-FOSDEM/Syd-OCI-FOSDEM.pdf?ref_type=heads)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9LE7ZF/feedback/)

---

### Less overhead, strong isolation: Running containers in minimal specialized Linux VMs

- **Speakers:** Charalampos Mainas, Anastassios Nanos
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 17:20 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6284-less-overhead-strong-isolation-running-containers-in-minimal-specialized-linux-vms/)

#### Abstract

Containers have become the preferred solution for cloud-native applications due to their lightweight nature and scalability. However, their security limitations, particularly from shared kernel access, have led to a renewed interest in traditional VMs for stronger isolation. Technologies like kata-containers enhance security by running containers inside microVMs, offering better isolation, but they introduce complexity and overhead. Specifically, the container runtimes spawn additional processes to manage the container within the VM, adding extra layers of complexity and resource consumption.
This talk examines the pros and cons of sandboxed container runtimes, focusing on the added complexity of auxiliary processes. It then proposes a more efficient and streamlined approach based on the unikernel paradigm, where only the application and its dependencies are running. Rather than using strict unikernels, it explores how containers can run inside specialized, stripped-down Linux VMs, containing only the components required by the application and without additional services. This is achieved through urunc, a CRI-compatible container runtime that treats unikernels like standard containers, managing the user application via the VM process.

#### Related Links

- [Repository](https://github.com/nubificus/urunc)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7NHNTF/feedback/)

---

### Dangerzone: Containers that contain containers that contain attackers

- **Speakers:** Alex Pyrgiotis
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 17:40 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6251-dangerzone-containers-that-contain-containers-that-contain-attackers/)

#### Abstract

Dangerzone is a multi-platform project that performs a simple task; give it an untrusted document, and get back a sanitized one. Qubes did it first with disposable Xen VMs (see TrustedPDF), but Dangerzone is doing it with containers across all major platforms. How secure are containers though, and can you achieve VM-level parity with them?
In this talk we’ll discuss the attack surface of Linux containers, and how Dangezone uses gVisor to contain RCEs in document viewers. Even if you don’t use gVisor or are not interested in it, we’ll show some easy ways to harden your security-sensitive containers right now, for harm reduction purposes.

#### Related Links

- [gVisor source](https://github.com/google/gvisor)
- [Dangerzone source](https://github.com/freedomofpress/dangerzone)
- [Dangerzone's Mastodon account](https://social.freedom.press/@dangerzone)
- [Blog post on how Dangerzone handles defense-in-depth with gVisor](https://dangerzone.rocks/news/2024-09-23-gvisor/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PTVLYR/feedback/)

---

### D4C: Leveraging Delta Encodings for Faster and Lighter Container Image Updating

- **Speakers:** Naoki Matsumoto
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 18:10 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5946-d4c-leveraging-delta-encodings-for-faster-and-lighter-container-image-updating/)

#### Abstract

Container images sometimes take tens to hundreds of megabytes in size and require many network resources to be transferred.
Especially in low-bandwidth network environments like edge computing, frequent image updating will be difficult and increase the network cost.
In this talk, I will present "D4C", a software that provides faster and lighter image updating with delta encodings.
Delta encodings reduce data size, but generating and applying deltas is a time-consuming operation.
D4C utilizes some techniques to reduce them including merge-based delta management and applying deltas lazily.
D4C reduces the data size to update images by up to 95% and provides about 10x faster updating in low-bandwidth networks than the state-of-the-art approach.
Benchmarks with PostgreSQL and PyTorch showed that their performance degradation caused by D4C is negligible.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9PHCW7/feedback/)

---

### TuxWrangler: Image Wrangler

- **Speakers:** Kavitha Daula, Ethan Pullen
- **Room:** UD2.218A
- **Day:** Saturday
- **Time:** 18:30 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5763-tuxwrangler-image-wrangler/)

#### Abstract

TuxWrangler is a framework designed to simplify the creation and management sets of containers, focusing on automation, scalability, and flexibility. Unlike Packer, which excels at building single "golden images" for immutable infrastructure, TuxWrangler is tailored for environments requiring multiple lightweight, highly-configured images, such as GEICO's. It automates dependency updates by dynamically fetching and locking versions from container repositories, reducing manual effort and ensuring consistency. With its centralized configuration management and integration with CI/CD pipelines, TuxWrangler streamlines complex workflows, automates testing, and publishes validated images efficiently.
TuxWrangler addresses use cases requiring dynamic updates and multiple image variations without duplicated build logic. Its ability to manage dependencies dynamically, scale configurations efficiently, and integrate seamlessly with DevOps ecosystems makes it ideal for modern, fast-paced environments. 
We will present a demo of TuxWrangler, which is currently being used by us to solve our engineering needs. We will focus on its ability to simplify multi-image builds, automate dependency management, and integrate seamlessly with existing workflows. We would like to receive feedback from the community regarding its future iterations, ensuring TuxBake remains a valuable tool for evolving infrastructure needs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-containers:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-containers:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VMGKMM/feedback/)

---

## Data Analytics (13)

### What the Spec?!: New Features in Apache Iceberg™ Table Format V3

- **Speakers:** Danica Fine, Russell Spitzer
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4707-what-the-spec-new-features-in-apache-iceberg-table-format-v3/)

#### Abstract

Apache Iceberg™ made great advancements going from Table Format V1 to Table Format V2, introducing features like position deletes, advanced metrics, and cleaner metadata abstractions. But with Table Format V3 on the horizon, Iceberg users have even more to look forward to.
In this session, we’ll explore some of the exciting new user-facing features that V3 Iceberg is about to introduce and see how they’ll make working with Open Data Formats easier than ever! We’ll go through the high-level details of the new functionality that will be available in V3.  Then we’ll dive deep into some of the most impactful features. You’ll learn what Variant types have to offer your semi-structured data, how Row Lineage can enhance CDC capabilities, and more. 
The community has come together to build yet another great release of the Iceberg spec, so attend and learn about all of the changes coming and how you can take advantage of them in your teams.

#### Related Links

- [Apache Iceberg](https://iceberg.apache.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SKTWMA/feedback/)

---

### Graph Databases after 15 Years – Where Are They Headed?

- **Speakers:** Gábor Szárnyas
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 11:10 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5413-graph-databases-after-15-years-where-are-they-headed-/)

#### Abstract

Neo4j had its first stable release in 2010 and soon became one of the defining NoSQL systems, establishing "graph databases" as a new category. These systems represent data as nodes and edges, allowing for intuitive querying and visualization, as well as performance benefits on certain types of queries (e.g. path finding).
In this talk, I give a brief overview of the past, present, and future of graph databases. I first summarize the history of graph database systems, focusing on their main categories and use cases. Then, I discuss the key challenges that continue to hinder the adoption of graph databases, including a fragmented landscape and performance limitations.
I end the talk with recent positive developments: (1) Advances in standardization that led to the ISO GQL and SQL/PGQ languages, (2) Performance increases driven by competition on the LDBC benchmark suite, (3) A new generation of open-source graph database systems such as Kùzu and DuckPGQ

#### Related Links

- [LDBC website](https://ldbcouncil.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WHJXDY/feedback/)

---

